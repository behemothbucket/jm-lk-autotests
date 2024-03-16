import json

import requests
import urllib3

from utils.constants.routes import Path

""" БЫЛО БЫ НЕПЛОХО УПОРЯДОЧИТЬ ЗАПРОСЫ ПО КОНТРОЛЛЕРАМ"""


class ClientInterface:
    def __init__(self, payload, cookie):
        self.payload = payload
        self.cookie = cookie

    @staticmethod
    def authorize(phone: str, amount: str, days: str):
        payload = json.dumps({"phone": phone, "amount": amount, "days": days})
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/authorize",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

    @staticmethod
    def login(
        person_check_id: str | None = None, person_id: str | None = None
    ) -> tuple:
        if person_id == None:
            payload = json.dumps(
                {"password": "123456", "personCheckId": person_check_id}
            )
        else:
            payload = json.dumps({"password": "123456", "personId": person_id})
        login = requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/login",
            headers={"Content-Type": "application/json"},
            data=payload,
        )
        cookie = str(login.cookies)
        cookie = cookie[27:83]
        success = json.loads(login.text)["success"]
        return cookie, success

    @staticmethod
    def create_newClient(name: str, personCheckId, cookie) -> tuple:
        payload = json.dumps({"name": name, "personCheckId": personCheckId})
        create = requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/newClient/create",
            headers={"Content-Type": "application/json", "cookie": cookie},
            data=payload,
        )
        return (
            json.loads(create.text)["success"],
            json.loads(create.text)["applicationId"],
        )

    @staticmethod
    def applydata(field_name, field_value, cookie):
        payload = json.dumps(
            {"fieldName": str(field_name), "fieldValue": str(field_value)}
        )
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/client/applyData",
            headers={"Content-Type": "application/json", "cookie": cookie},
            data=payload,
        )

    @staticmethod
    def bulk(payload, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/client/applyData/bulk",
            headers={"Content-Type": "application/json", "cookie": cookie},
            data=payload,
        )

    @staticmethod
    def documents(cookie):
        url = "https://my-preprod.joy.money/client-interface/documents"
        img = open(Path.WORKSPACE_DIR + "/resources/img/passport/2190.jpg", "rb")
        headers = {"cookie": cookie}
        payload, header = urllib3.encode_multipart_formdata(
            {
                "files": ("test", img.read(), "image/jpg"),
                "files": ("tost", img.read(), "image/jpg"),
                "files": ("tast", img.read(), "image/jpg"),
            }
        )
        img.close()
        headers["content-type"] = header
        return requests.post(url, data=payload, headers=headers)

    @staticmethod
    def check_credit_history(
        cookie,
    ):  # Можно заморочиться и смотреть в табличку на то, какая СМСка пришла
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/sms/check/applyCreditHistoryRequest?code=1234",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def pending(cookie):
        payload = json.dumps({"url_link": "https%3A%2F%2Fmy-preprod.joy.money%2Flogin"})
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/application/pending",
            headers={"Content-Type": "application/json", "cookie": cookie},
            data=payload,
        )

    @staticmethod
    def insurance(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/application/insurance?apply=true",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def bind_new(cookie, app_id):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/paymentTools/bindNew?applicationId="
            + str(app_id),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def send_signAgreement(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/sms/send/signAgreement",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def check_signAgreement(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/sms/check/signAgreement?code=1234",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def issue(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/application/issue",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def logout(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/logout",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def moved_to_sign_page(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/agreement/movedToSignPage",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    """ БОНУСНАЯ СИСТЕМА, КОТОРАЯ НИКОГДА НЕ БУДЕТ ЗАПУЩЕНА"""

    @staticmethod
    def bonus_amount(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/bonus/amount",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def bonus_byagreement(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/bonus/byAgreement",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def bonus_history(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/bonus/history",
            # Вохможно нужная пагинация? /history?limit=1&offset=1
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def bonus_maxtopay(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/bonus/maxToPay",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    """  ---------------  """

    @staticmethod
    def pay(loan_money, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/payment/card/pay?amount="
            + str(loan_money),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def create(amount, days, cookie):
        payload = json.dumps({"amount": str(amount), "days": str(days)})
        headers = {"Content-Type": "application/json", "cookie": cookie}
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/application/create",
            headers=headers,
            data=payload,
        )

    """ GET - ЗАПРОСЫ"""

    @staticmethod
    def status(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/application/status",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def for_payment(cookie, bool):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/paymentTools?forPayment="
            + str(bool),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def active(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/agreement/active",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def check(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/login/check",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def info(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/client/info",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def tarif_info_list(cookie):
        return requests.request(
            "GET",
            "https://my-preprod.joy.money/client-interface/client/tarifInfoList",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    """ FORGOT PASSWORD"""

    @staticmethod
    def forgot_password(phone):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/actions/forgotPassword?contact="
            + str(phone)
            + "&recoveryType=phone",
            headers={"Content-Type": "application/json"},
        )

    @staticmethod
    def forgot_password_check_field(phone, field_value):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/actions/forgotPassword/checkField?fieldValue="
            + str(field_value)
            + "&phone="
            + str(phone),
            headers={"Content-Type": "application/json"},
        )

    @staticmethod
    def forgot_password_check_sms(code, phone, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/actions/forgotPassword/checksums?code="
            + str(code)
            + "&phone="
            + str(phone),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def forgot_password_set_new_pass(password, cookie):
        payload = json.dumps({"password": password})
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/client/actions/setNewPassword",
            data=payload,
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    """ PROLONGATION"""

    @staticmethod
    def prolongation(days, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/agreement/prolongate?days="
            + str(days),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def prolongation_send_sms(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/sms/send/prolongation",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def prolongation_check_sms(code, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/sms/check/prolongation?code="
            + str(code),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def prolongation_paytool(id_card, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/payment/paytool/prolongation?paytoolId="
            + str(id_card),
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def send_credit_history(cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/sms/send/applyCreditHistoryRequest",
            headers={"Content-Type": "application/json", "cookie": cookie},
        )

    @staticmethod
    def bulk_application(payload, app_id, cookie):
        return requests.request(
            "POST",
            "https://my-preprod.joy.money/client-interface/application/"
            + str(app_id)
            + "/applyData/bulk",
            headers={"Content-Type": "application/json", "cookie": cookie},
            data=payload,
        )

    """ CUSTOM REQUESTS"""


# def create_application():
# create
# bulk (amount, days)
# bulk(fill_time_pages)??
# pending


# def registration(phone):
# auth = Client_interface.authorize(phone, 5000, 15)
# person_check_id = json.loads(auth.text)["personCheckId"]
# login = Client_interface.login(person_check_id, None)
# cookie = login[0]
# create = Client_interface.create_newClient(person_check_id, cookie)
# app_id = create[1]
# payload = json.dumps(
#     dict(surname="Фамилия", patronymic="Отчество", birthdate="12.12.1987", email="testqa@api.pfq", passportIdentifier="1231 233123",
#          passportIssueDate="12.12.2020", passportIssuerCode="123-123", passportIssuerName="тест0 тест0 тест0",
#          birthPlace="йцуйцу", snils="012-345-678 19", addressFactHouse="12", addressRegHouse="12",
#          addressFactFlat="1212", addressRegFlat="1212", bankruptcyProcessed="false",
#          addressFactId="9decf710-1352-4164-b6e3-88158517d67a",
#          addressRegId="9decf710-1352-4164-b6e3-88158517d67a", jobType="26", jobCompanyName="Организация",
#          jobTitle="Должность", salary="10000", expensesAmount="7000", friendFIO="Фамилия Имя Друга",
#          friendType="22", friendPhone="79344213212"))
# bulk = Other.check_bulk_full_success(cookie)
# Client_interface.documents(cookie)
# Client_interface.bulk_application(json.dumps({"personalPageFillDate": "", "passportPageFillDate": "", "jobPageFillDate": ""}), app_id, cookie)
# Client_interface.send_credit_history(cookie)
# Client_interface.check_credit_history(cookie)
# Client_interface.pending(cookie)
