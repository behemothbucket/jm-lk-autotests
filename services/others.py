import json
import random
import time

from services.client_interface import ClientInterface as cl
from services.emulator import Emulator as em
from utils.sql import SQL


class Other:
    @staticmethod
    def check_bulk_full_success(payload, cookie):
        bulk = json.loads(cl.bulk(payload, cookie).text)
        # assert bulk["friendFIO"]["success"] == True
        assert bulk["addressRegFlat"]["success"] == True
        assert bulk["birthdate"]["success"] == True
        assert bulk["passportIssuerName"]["success"] == True
        assert bulk["bankruptcyProcessed"]["success"] == True
        assert bulk["jobTitle"]["success"] == True
        assert bulk["addressRegHouse"]["success"] == True
        assert bulk["salary"]["success"] == True
        assert bulk["passportIdentifier"]["success"] == True
        assert bulk["addressFactFlat"]["success"] == True
        assert bulk["birthPlace"]["success"] == True
        assert bulk["patronymic"]["success"] == True
        assert bulk["passportIssuerCode"]["success"] == True
        assert bulk["friendType"]["success"] == True
        assert bulk["addressFactHouse"]["success"] == True
        assert bulk["jobCompanyName"]["success"] == True
        assert bulk["friendPhone"]["success"] == True
        assert bulk["addressRegId"]["success"] == True
        assert bulk["passportIssueDate"]["success"] == True
        assert bulk["addressFactId"]["success"] == True
        assert bulk["jobType"]["success"] == True
        assert bulk["snils"]["success"] == True
        assert bulk["email"]["success"] == True
        assert bulk["expensesAmount"]["success"] == True
        return True

    @staticmethod
    def create_agree(phone, status_id):
        #  Добавить проверку на то, какой сейчас статус у заявки и договора
        auth = cl.authorize(phone, "5000", "15")
        person_type = json.loads(auth.text)["personType"]
        if person_type == "NEW":
            person_check_id = json.loads(auth.text)["personCheckId"]
            login = cl.login(person_check_id=person_check_id)
            cookie = login[0]
            create = cl.create_newClient("Test", person_check_id, cookie)
            app_id = create[1]
            payload = json.dumps(
                dict(
                    surname="Фамилия ",
                    patronymic="Отчество",
                    birthdate="12.12.1987",
                    email="testqaqa" + str(random.randint(1, 500)) + "@api.api",
                    passportIdentifier="5402 328458",
                    passportIssueDate="12.12.2020",
                    passportIssuerCode="123-123",
                    passportIssuerName="тест0 тест0 тест0",
                    birthPlace="место рождения",
                    snils="012-345-678 19",
                    addressFactHouse="12",
                    addressRegHouse="12",
                    addressFactFlat="1212",
                    addressRegFlat="1212",
                    bankruptcyProcessed="false",
                    addressFactId="9decf710-1352-4164-b6e3-88158517d67a",
                    addressRegId="9decf710-1352-4164-b6e3-88158517d67a",
                    jobType="26",
                    jobCompanyName="Организация",
                    jobTitle="Должность",
                    salary="10000",
                    expensesAmount="7000",
                    # friendFIO="Фамилия Имя Друга",
                    friendType="22",
                    friendPhone="79344213212",
                )
            )
            cl.bulk(payload, cookie)
            cl.documents(cookie)
        else:
            person_id = json.loads(auth.text)["personId"]
            login = cl.login(None, person_id)
            cookie = login[0]
            if (
                json.loads(cl.info(cookie).text)["application"]["status"] != 8
                or json.loads(cl.info(cookie).text)["agreement"]["status"] != 19
            ):
                em.refuse_by_client(phone)
            cre = cl.create(5000, 15, cookie)
            app_id = json.loads(cre.text)["id"]
        # app_id = json.loads(cl.create(5000, 15, cookie).text)["id"]
        cl.bulk_application(
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
        cl.send_credit_history(cookie)
        cl.check_credit_history(cookie)
        sta = json.loads(cl.info(cookie).text)["application"]["status"]
        if status_id == json.loads(cl.info(cookie).text)["application"]["status"]:
            return cookie
        cl.pending(cookie)
        if status_id == json.loads(cl.info(cookie).text)["application"]["status"]:
            return cookie
        em.approve_application(app_id)
        if status_id == json.loads(cl.info(cookie).text)["application"]["status"]:
            return cookie
        cl.insurance(cookie)
        bind_new = cl.bind_new(cookie, app_id)
        em.submit_payment(
            1, json.loads(bind_new.text)["requestParams"]["requestId"], "40000000000"
        )
        payments_tool = cl.for_payment(cookie, True)
        id_card = json.loads(payments_tool.text)[0]["id"]
        cl.bulk_application(json.dumps({"currentPaytool": id_card}), app_id, cookie)
        cl.send_signAgreement(cookie)
        cl.check_signAgreement(cookie)
        issue = cl.issue(cookie)
        if issue.status_code == 400:
            SQL.update_app_status(8, app_id)
            cl.issue(cookie)
        if status_id == json.loads(cl.info(cookie).text)["application"]["status"]:
            return cookie
        if status_id == json.loads(cl.info(cookie).text)["agreement"]["status"]:
            return cookie
        # sta = json.loads(cl.info(cookie).text)
        active = cl.active(cookie)
        # для просроченного договора добавить проверки
        if status_id == json.loads(cl.info(cookie).text)["agreement"]["status"]:
            return cookie
        loan_money = json.loads(active.text)["loanMoney"]
        pan = json.loads(active.text)["pan"]
        pay = cl.pay(loan_money, cookie)
        request_id = json.loads(pay.text)["requestParams"]["requestId"]
        em.submit_payment(loan_money, request_id, pan)
        time.sleep(1)
        if status_id == json.loads(cl.info(cookie).text)["agreement"]["status"]:
            return cookie

    # @staticmethod
    # def authorize_for_cookie():
