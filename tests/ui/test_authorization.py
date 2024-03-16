import allure
import pytest

from pages.authorization.authorization_page import AuthorizationPage
from utils.constants.features import Account, Feature
from utils.constants.routes import Routes
from utils.constants.suites import Suite


@pytest.mark.ui
@pytest.mark.authorization
@pytest.mark.smoke
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("UI")
@allure.suite(Suite.SMOKE)
@allure.sub_suite("Авторизация")
@allure.feature(Feature.CLIENTS)
class TestAuthorization:
    AUTHORIZATION_URL = Routes.AUTHORIZATION.value

    @allure.title("Успешная авторизация")
    def test_authorization(self, authorization_page: AuthorizationPage):
        authorization_page.visit(self.AUTHORIZATION_URL)
        authorization_page.fill_phone_number(Account.PHONE.value)
        authorization_page.fill_password(Account.DEFAULT_PASSWORD.value)
        authorization_page.click_next_button()
        authorization_page.check_current_loan_page()
