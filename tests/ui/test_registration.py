import allure
import pytest

from pages.registration.registration_page import RegistrationPage
from utils.constants.features import Feature
from utils.constants.routes import Routes
from utils.constants.suites import Suite


@pytest.mark.ui
@pytest.mark.registration
@pytest.mark.smoke
@allure.severity(allure.severity_level.CRITICAL)
@allure.parent_suite("UI")
@allure.suite(Suite.SMOKE)
@allure.sub_suite("Регистрация")
@allure.feature(Feature.CLIENTS)
class TestRegistration:
    REGISTRATION_URL = Routes.AUTHORIZATION.value

    @pytest.mark.pdl_registration
    @allure.title("PDL: Успешная регистрация")
    def test_pdl_registration(self, pdl_registration: RegistrationPage):
        pdl_registration.visit(self.REGISTRATION_URL)
        pdl_registration.first_step()
        pdl_registration.second_step()
        pdl_registration.third_step()
        pdl_registration.approve_application()
        pdl_registration.sign_agreement()
        pdl_registration.check_current_loan_page()
