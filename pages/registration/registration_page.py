import allure
from pages.base.base_page import BasePage
from models.client import Client
from utils.webdriver.driver.page import Page
from pages.registration.steps.all_steps import *
from pages.registration.approve import *
from pages.registration.sign_agreement import *
from devtools import pprint


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.client: Client = Client.create()
        self.phone_number: str = self.client.phone_number
        self.app_id: str | None = None
        self.agree_id: str | None = None
        self.retry_count: int = 0

    # TODO: Убрать качычки в allure steps
    @allure.step("Шаг 1")
    def first_step(self) -> None:
        fill_phone_number(self, self.phone_number)
        fill_sms(self, self.client.sms)
        click_checkbox_all_documents_authorization_page(self)
        click_next_button(self)
        fill_name(self, self.client.name)
        click_next_button(self)
        fill_surname(self, self.client.surname)
        fill_patronymic(self, self.client.patronymic)
        fill_birthdate(self, self.client.birthdate)
        fill_email(self, self.client.email)
        click_next_button_first_step(self)

    @allure.step("Шаг 2")
    def second_step(self) -> None:
        fill_passport_series_and_number(self, self.client.passport_issuer_identifier)
        fill_passport_issue_date(self, self.client.passport_issue_date)
        fill_passport_issuer_code(self, self.client.passport_issuer_code)
        fill_passport_issuer_name(self, self.client.passport_issuer_name)
        fill_birthplace(self, self.client.birthplace)
        fill_snils(self, self.client.snils)
        fill_address_reg_city(self, self.client.address_reg_city)
        fill_address_reg_street(self, self.client.address_reg_street)
        fill_address_reg_house(self, self.client.address_reg_house)
        fill_address_reg_flat(self, self.client.address_reg_flat)
        click_registered_address_checkbox(self, state=True)
        click_next_button_second_step(self)
        upload_passport_photos(self, self.client.passport_photo_path)

    @allure.step("Шаг 3")
    def third_step(self) -> None:
        choose_job_type(self)
        fill_job_company_name(self, self.client.job_company_name)
        fill_job_title(self, self.client.job_title)
        fill_salary(self, self.client.salary)
        fill_expenses_amount(self, self.client.expenses_amount)
        click_bankruptcy_checkbox(self, state=False)
        fill_additional_phone_number(self, self.client.friend_phone_number)
        click_send_application_button(self)
        click_all_documents_registration_page_checkbox(self)
        click_send_application_button(self)
        fill_asp_code(self, self.client.asp)

    @allure.step("Перезаполнение заявки")
    def refill_person_data(self) -> None:
        """Refill problem fields"""
        self.reload()
        self.explicit_wait(1)
        self.move_to_bottom_of_page()
        self.explicit_wait(1)
        click_send_application_button(self, force=True)
        self.explicit_wait(2)
        fill_passport_series_and_number(self, self.client.passport_issuer_identifier)
        fill_passport_issue_date(self, self.client.passport_issue_date)
        fill_passport_issuer_code(self, self.client.passport_issuer_code)
        fill_passport_issuer_name(self, self.client.passport_issuer_name)
        fill_birthplace(self, self.client.birthplace)
        fill_address_reg_house(self, self.client.address_reg_house)
        fill_address_reg_flat(self, self.client.address_reg_flat)
        click_registered_address_checkbox(self, state=True)
        click_next_button_second_step(self)
        click_bankruptcy_checkbox(self, state=False)
        fill_salary(self, self.client.salary)
        click_all_documents_registration_page_checkbox(self)
        click_send_application_button(self, force=True)

    # TODO: Перенести всю логику в approve
    @allure.step("Одобрить заявку")
    def approve_application(self) -> None:
        self.explicit_wait(3)

        if is_lk_page:
            if is_already_approved(self):
                self.app_id = get_application_number(self)
                with allure.step(f"Номер заявки - {self.app_id}"):
                    pass
                self.locators.add_card_button.should_be_clickable()
                self.locators.add_card_button.click()
            else:
                self.explicit_wait(3)
                self.app_id = get_application_number(self)
                approve_application(self.app_id)
                self.explicit_wait(1)
                self.reload()
                is_application_approved(self)
                self.explicit_wait(1)
                self.locators.add_card_button.should_be_clickable()
                self.locators.add_card_button.click()
        else:
            self.refill_person_data()
            self.approve_application()

    # TODO: Перенести всю логику в approve
    @allure.step("Подписать договор")
    def sign_agreement(self) -> None:
        check_sign_agreement_page(self)
        add_card(self, self.client.pan)
        self.explicit_wait(1)
        self.locators.get_money_button.should_be_clickable()
        self.locators.get_money_button.click()
        fill_asp_code(self, self.client.asp)
        check_payment_transaction_status(self)
        self.agree_id = get_agreement_number(self)

    # TODO: Перенести всю логику в approve
    @allure.step("Проверка: Открыта страница ЛК")
    def check_current_loan_page(self) -> None:
        self.locators.current_loan_button.should_be_visible()
        self.locators.pay_loan_button.should_be_visible()
        with allure.step(f"Номер договора - {self.agree_id}"):
            self.log_registration_results()

    # TODO: Перенести всю логику в approve
    def log_registration_results(self) -> None:
        loan_info = f"----------\n[application_id = {self.app_id}]\n[agreement_id = {self.agree_id}]\n[phone_number = {self.phone_number}]"
        logger.info(loan_info)
        pprint(self.client)
