from typing import Union
import allure
from services.emulator import Emulator
from utils.sql import SQL
from utils.webdriver.logger import logger


@allure.step("Проверка: Открыта страница верификации")
def is_lk_page(self) -> bool:
    try:
        self.locators.application_number_span.should_be_visible()
        self.locators.logout_button.should_be_visible()
        return True
    except:
        return False


@allure.step("Получить номер заявки")
def get_application_number(self) -> str:
    return self.locators.application_number_span.get_app_or_agree_id()


@allure.step("Получить номер договора")
def get_agreement_number(self) -> str:
    self.locators.agreement_number_span.should_be_visible()
    return self.locators.agreement_number_span.get_app_or_agree_id()


@allure.step("Проверка: Заявка уже одобрена")
def is_already_approved(self) -> bool:
    try:
        self.locators.current_loan_button.should_be_visible()
        return True
    except:
        self.locators.new_loan_button.should_be_visible()
        return False


@allure.step("Одобрить заявку с id = {app_id}")
def approve_application(app_id: str) -> None:
    Emulator.approve_application(app_id)


@allure.step("Проверка: Статус заявки")
def is_application_approved(self) -> None:
    try:
        status_id: Union[str, None, tuple] = SQL.get_application_status(
            app_id=self.app_id
        )
        if not status_id:
            status_id = "Invalid"
        with allure.step(f"Статус заявки - {status_id[0]}"):
            SQL.log(status_id, "[Статус заявки: {}]")
        assert 7 == status_id[0]
    except AssertionError as e:
        logger.error(e)
