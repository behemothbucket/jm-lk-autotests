import allure
import pytest

from pages.recovery.recovery_page import RecoveryPage
from utils.constants.features import Account, Feature
from utils.constants.routes import Routes
from utils.constants.suites import Suite


@pytest.mark.ui
@pytest.mark.recovery
@pytest.mark.smoke
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("UI")
@allure.suite(Suite.SMOKE)
@allure.sub_suite("Восстановление пароля")
@allure.feature(Feature.CLIENTS)
class TestRecovery:
    AUTHORIZATION_URL = Routes.AUTHORIZATION.value

    @allure.title("Успешное восстановление пароля")
    def test_successful_recovery(
        self,
        recovery_page: RecoveryPage,
    ):
        recovery_page.visit(self.AUTHORIZATION_URL)
        recovery_page.fill_phone_number(Account.RECOVERY_PHONE.value)
        recovery_page.click_on_forgot_password_button()
        recovery_page.fill_phone_number_and_sms(
            Account.RECOVERY_PHONE.value, Account.RECOVERY_SMS.value
        )
        recovery_page.fill_new_passoword_and_login(Account.RECOVERY_NEW_PASSWORD.value)
