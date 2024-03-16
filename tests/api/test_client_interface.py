import json
import os
import unittest
from time import sleep

import allure
import pytest
from dotenv import load_dotenv

from models.client import Client
from services.client_interface import ClientInterface as client
from services.emulator import Emulator as em
from services.others import Other
from utils.constants.features import Payment
from utils.sql import SQL
from utils.webdriver.logger import logger

load_dotenv()


@pytest.mark.api
class TestClientInterface(unittest.TestCase):
    @allure.step("Создание нового клиента")
    def setUp(self) -> None:
        amount: str | None = os.getenv("API_TESTS_AMOUNT", default="")
        days: str | None = os.getenv("API_TESTS_DAYS", default="")

        if amount == "" or days == "":
            logger.error(f"Переменная окружения {amount} или {days} не установлена")

        self.client = Client.create(amount=amount, days=days)
        self.phone_number = self.client.phone_number
        with allure.step(f"Номер телефона: {self.phone_number}"):
            logger.info(f"Номер телефона: {self.phone_number}")

    # TODO рещить надо или нет
    # @allure.step("Удаление учетной записи")
    # def tearDown(self) -> None:
    #     with allure.step(f"Номер телефона: {self.client.phone_number}"):
    #         em.delete_person(self.phone_number)

    @pytest.mark.flow
    @allure.step("Полный флоу: оформление заявки, одобрение, погашение")
    def test_flow(self) -> None:
        # assert json.load(delete_person.text) == 'true', 'person was deleted'
        auth = client.authorize(self.phone_number, self.client.amount, self.client.days)
        person_type = json.loads(auth.text)["personType"]
        assert person_type == "NEW", "client_interface/authorize.. FAILED"
        person_check_id = json.loads(auth.text)["personCheckId"]

        login = client.login(person_check_id=person_check_id)
        cookie = login[0]
        assert login[1] == True, "/login... FAILED"  # Success == True

        create = client.create_newClient(self.client.name, person_check_id, cookie)
        app_id = create[1]
        assert create[0] == True, "/newClient/create... FAILED"  # success == True

        # TODO почему surname отдельно?
        apply_data = client.applydata("surname", self.client.surname, cookie)
        assert (
            json.loads(apply_data.text)["success"] == True
        ), "/client/applyData... FAILED"

        # TODO попробовать брать ID адресов, отправляя запросы в DaData
        # TODO случайный выбор jobType, friendType

        client_data = dict(
            patronymic=self.client.patronymic,
            birthdate=self.client.birthdate,
            email=self.client.email,
            passportIdentifier=self.client.passport_issuer_identifier,
            passportIssueDate=self.client.passport_issue_date,
            passportIssuerCode=self.client.passport_issuer_code,
            passportIssuerName=self.client.passport_issuer_name,
            birthPlace=self.client.birthplace,
            snils=self.client.snils,
            addressFactHouse="12",
            addressRegHouse="12",
            addressFactFlat="1212",
            addressRegFlat="1212",
            bankruptcyProcessed="false",
            addressFactId="9decf710-1352-4164-b6e3-88158517d67a",
            addressRegId="9decf710-1352-4164-b6e3-88158517d67a",
            jobType="26",
            jobCompanyName=self.client.job_company_name,
            jobTitle=self.client.job_title,
            salary=self.client.salary,
            expensesAmount=self.client.expenses_amount,
            friendType="22",
            friendPhone=self.client.friend_phone_number,
        )
        logger.info(
            f"\namount: {self.client.amount}\n"
            + f"days: {self.client.days}\n"
            + f"name: {self.client.name}\n"
            + f"surname: {self.client.surname}\n"
            + json.dumps(client_data, ensure_ascii=False, indent=4)
        )
        payload = json.dumps(client_data)
        bulk = Other.check_bulk_full_success(payload, cookie)
        assert bulk == True, "/bulk... FAILED"

        photos = client.documents(cookie)
        assert photos.status_code == 200, "Фото загружены \n /documents... FAILED"

        bulk_fill_time_page = client.bulk_application(
            json.dumps(
                {
                    "personalPageFillDate": "",
                    "passportPageFillDate": "",
                    "jobPageFillDate": "",
                }
            ),
            app_id,
            cookie,
        )
        assert (
            json.loads(bulk_fill_time_page.text)["passportPageFillDate"]["success"]
            == True
        ), "/application/bulk... FAILED"

        credit_history = client.send_credit_history(cookie)
        assert (
            json.loads(credit_history.text)["success"] == True
        ), "/sms/send/applyCreditHistoryRequest... FAILED"

        credit_history_check = client.check_credit_history(cookie)
        assert (
            json.loads(credit_history_check.text) == True
        ), "/sms/check/applyCreditHistoryRequest... FAILED"

        pending = client.pending(cookie)
        assert json.loads(pending.text)["success"] == True, "/pending... FAILED"

        approve = em.approve_application(app_id).json()
        assert approve["success"] == True, "/qa/approve/default... FAILED"

        insurance = client.insurance(cookie)
        assert json.loads(insurance.text)["success"] == True, "/insurance... FAILED"

        bind_new = client.bind_new(cookie, app_id)

        match Payment.PROVIDER:
            case "TKB":
                bind_response = em.submit_payment_qiwi(
                    1, json.loads(bind_new.text)["requestParams"]["requestId"]
                )
                assert (
                    json.loads(bind_response.text)["success"] == True
                ), "/paymentTools/bindNew.. FAILED"
            case "QIWI":
                bind_response = em.submit_payment_tkb(
                    1, json.loads(bind_new.text)["requestKey"]
                )
                assert (
                    json.loads(bind_response.text)["success"] == True
                ), "/paymentTools/bindNew.. FAILED"

        payments_tool = client.for_payment(cookie, True)
        id_card = json.loads(payments_tool.text)[0]["id"]
        assert (
            payments_tool.status_code == 200
        ), "/paymentTools?forPayment=true... FAILED"

        bulk_card = client.bulk_application(
            json.dumps({"currentPaytool": id_card}), app_id, cookie
        )
        assert (
            json.loads(bulk_card.text)["currentPaytool"]["success"] == True
        ), "/applyData/bulk...(currentPaytool) FAILED "

        send_agreement = client.send_signAgreement(cookie)
        assert (
            json.loads(send_agreement.text)["success"] == True
        ), "/sms/send/signAgreement.. FAILED"

        check_agreement = client.check_signAgreement(cookie)
        assert (
            json.loads(check_agreement.text) == True
        ), "sms/check/signAgreement... FAILED"

        issue = client.issue(cookie)
        if issue.status_code == 400:
            SQL.update_app_status(8, app_id)
            issue = client.issue(cookie)
        assert json.loads(issue.text)["success"] == True, "/application/issue... FAILED"

        if os.getenv("FULL_FLOW", "True").lower() in ("true", "1", "t"):
            active = client.active(cookie)
            loan_money = json.loads(active.text)["loanMoney"]

            pay = client.pay(loan_money, cookie)
            request_id = json.loads(pay.text)["requestParams"]["requestId"]
            assert (
                json.loads(pay.text)["success"] == True
            ), "/payment/card/pay?amount... FAILED"

            em.submit_payment_qiwi(loan_money, request_id)
            sleep(
                1
            )  # задержка, чтобы оплата прошла и процесс закрытия договора завершился
            agree_end = client.info(cookie)
            assert (
                json.loads(agree_end.text)["application"]["status"] == 8
                and json.loads(agree_end.text)["agreement"]["status"] == 19
            )

        logger.info("FLOW DONE")

    @pytest.mark.get_requests
    @allure.step("Проверка: GET-запросы")
    def test_get_requests(self) -> None:
        logger.info("---GET - requests---")
        phone = self.phone_number
        auth = client.authorize(phone, self.client.amount, self.client.days)
        person_check_id = json.loads(auth.text)["personCheckId"]
        login = client.login(person_check_id, None)
        cookie = login[0]
        client.create_newClient(self.client.name, person_check_id, cookie)
        # person_id = json.loads(auth.text)["personId"]
        # login = client.login(None, person_id)

        assert (
            json.loads(client.status(cookie).text) == 5
        ), "/application/status... DONE"

        assert (
            client.for_payment(cookie, False).status_code == 200
        ), "/paymentTools?forPayment=false... DONE"

        assert client.active(cookie).status_code == 200, "/agreement/active.. DONE"

        assert (
            json.loads(client.check(cookie).text)["active"] == True
        ), "/login/check... DONE"

        assert (
            json.loads(client.info(cookie).text)["success"] == True
        ), "/client/info... DONE"

        # requests.post('http://api-preprod.joy.money:9099/emulator/qa/person/phone/79431206740/refuseByClient') ЗАЧЕМ?

        assert (
            json.loads(client.tarif_info_list(cookie).text)[0]["tariffId"] == 45
        ), "/client/tariffInfoList... DONE"

    @pytest.mark.api_recovery
    @allure.step("Проверка: Восстановление пароля")
    def test_forgot_password(self):
        logger.info("---FORGOT PASSWORD---")
        phone = "75258453256"
        auth = client.authorize(self.phone_number, self.client.amount, self.client.days)
        person_check_id = json.loads(auth.text)["personCheckId"]
        login = client.login(person_check_id=person_check_id)
        cookie = login[0]
        client.create_newClient(self.client.name, person_check_id, cookie)
        forgot_password = client.forgot_password(phone)
        if json.loads(forgot_password.text)["success"] == True:
            pass
        else:
            logger.info("/forgotPassword... FAILED ERROR: too many retries")
            return

        check_field = client.forgot_password_check_field(phone, 123)
        cookie = str(check_field.cookies)[27:83]  # cookie = cookie[27:83]
        assert (
            json.loads(check_field.text)["success"] == True
        ), "/forgotPassword/checkField... FAILED"

        check_sms = client.forgot_password_check_sms(1234, phone, cookie)
        assert json.loads(check_sms.text) == True, "/forgotPassword/checksums... FAILED"

        set_new_pass = client.forgot_password_set_new_pass("Test123", cookie)
        assert (
            json.loads(set_new_pass.text)["success"] == True
        ), "/setNewPassword... FAILED"

    @pytest.mark.prolongation
    def test_prolongate(self) -> None:
        logger.info("-- PROLONGATE --")
        phone = "77258453256"
        cookie = Other.create_agree(phone, 16)
        info = client.info(cookie)
        agree_id = json.loads(info.text)["agreement"]["id"]
        days = json.loads(info.text)["agreement"]["loanDays"]
        em.expired_agreement(agree_id, days + 5)
        id_card = json.loads(client.for_payment(cookie, True).text)[0]["id"]
        assert (
            json.loads(client.prolongation(10, cookie).text)["success"] == True
        ), "/agreement/prolongate... FAILED"
        assert (
            json.loads(client.prolongation_send_sms(cookie).text)["success"] == True
        ), "sms/send/prolongation... FAILED"
        assert (
            json.loads(client.prolongation_check_sms(1234, cookie).text) == True
        ), "/sms/check/prolongation... FAILED"
        assert (
            json.loads(client.prolongation_paytool(id_card, cookie).text)["result"]
            == "success"
        )
        sleep(1)

    def pay_qiwi(self, request_key: str, bind_new_response):
        em.submit_payment_qiwi(1, request_key)
        assert (
            json.loads(bind_new_response.text)["success"] == True
        ), "/paymentTools/bindNew.. FAILED"

    def pay_tkb(self, request_key: str, bind_new_response):
        em.submit_payment(1, request_key)
        assert (
            json.loads(bind_new_response.text)["success"] == True
        ), "/paymentTools/bindNew.. FAILED"
