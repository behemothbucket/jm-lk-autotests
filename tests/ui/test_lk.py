import allure
import pytest

from pages.lk.lk_page import LKPage
from utils.constants.features import Account, Feature
from utils.constants.routes import Routes
from utils.constants.suites import Suite


@pytest.mark.ui
@pytest.mark.lk
@pytest.mark.smoke
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("UI")
@allure.suite(Suite.SMOKE)
@allure.sub_suite("Личный кабинет")
@allure.feature(Feature.CLIENTS)
class TestLK:
    AUTHORIZATION_URL = Routes.AUTHORIZATION.value

    @allure.title("Отображение корректной инфорации в ЛК")
    def test_lk(self, lk_page: LKPage):
        lk_page.visit(self.AUTHORIZATION_URL)
        lk_page.fill_phone_number(Account.PHONE.value)
        lk_page.fill_password(Account.DEFAULT_PASSWORD.value)
        lk_page.click_next_button()
        lk_page.check_current_loan_page()
        lk_page.check_loan_buttons()
        # lk_page.check_detailed_information_and_documents() # BUG JMRU-7955
        lk_page.check_sidebar_navigation()
        lk_page.logout()
