import json

import requests

from utils.constants.features import Account
from utils.constants.routes import Routes


class Emulator:
    @staticmethod
    def delete_person(phone: str):
        try:
            delete = requests.post(
                Routes.API_EMULATOR_BASE_URL
                + "/emulator/qa/person/delete?phone="
                + str(phone)
            )
            return delete
        except BaseException:
            return "Такой person не существует"

    @staticmethod
    def expired_agreement(agree_id, days):
        payload = json.dumps(
            {
                "agreementId": agree_id,
                "paymentProvider": "autotests",
                "factLoanDays": days,
            }
        )
        return requests.request(
            "POST",
            Routes.API_EMULATOR_BASE_URL
            + "/emulator/qa/doExpiredAgreementWithAvailableProlongation",
            headers={"Content-Type": "application/json"},
            data=payload,
        )

    @staticmethod
    def approve_application(app_id):
        return requests.post(
            Routes.API_EMULATOR_BASE_URL
            + "/emulator/qa/approve/default?applicationId="
            + str(app_id)
        )

    @staticmethod
    def submit_payment_qiwi(amount, request_id):
        return requests.post(
            Routes.API_EMULATOR_BASE_URL
            + "/emulator/payment/submitPayment?amount="
            + str(amount)
            + "&requestId="
            + str(request_id)
            + "&pan="
            + Account.PAN
        )

    @staticmethod
    def submit_payment_tkb(amount, request_id):
        return requests.post(
            Routes.API_EMULATOR_BASE_URL
            + "/emulator/payment/submitPayment?amount="
            + str(amount)
            + "&requestId="
            + str(request_id)
            + "&pan="
            + Account.PAN
        )

    @staticmethod
    def refuse_by_client(phone):
        return requests.post(
            Routes.API_EMULATOR_BASE_URL
            + "/emulator/qa/person/phone/"
            + str(phone)
            + "/refuseByClient"
        )
