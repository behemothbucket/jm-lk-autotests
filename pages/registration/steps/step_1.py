import allure
from selenium.webdriver.common.keys import Keys


@allure.step("Ввод номера телефона: {phone_number}")
def fill_phone_number(self, phone_number: str) -> None:
    self.locators.phone_input.should_be_visible()
    self.locators.phone_input.fill(phone_number)


@allure.step("Ввод смс-кода: {sms}")
def fill_sms(self, sms: str) -> None:
    self.locators.sms_code_input.should_be_visible()
    self.locators.sms_code_input.fill(sms)


@allure.step("Отметить все документы к согласию")
def click_checkbox_all_documents_authorization_page(self) -> None:
    self.locators.authorization_page_all_documents_checkbox.should_be_clickable()
    self.locators.authorization_page_all_documents_checkbox.click()


@allure.step("Нажать кнопку 'Далее'")
def click_next_button(self) -> None:
    self.locators.next_button.should_be_clickable()
    self.locators.next_button.click()
    self.explicit_wait(1)


@allure.step("Ввод имени: {name}")
def fill_name(self, name: str) -> None:
    self.locators.name_input.should_be_visible()
    self.locators.name_input.fill(name)


@allure.step("Ввод фамилии:  {surname}")
def fill_surname(self, surname: str) -> None:
    self.locators.surname_input.should_be_visible()
    self.locators.surname_input.fill(surname)
    self.explicit_wait(1)
    self.locators.patronymic_input.click()


@allure.step("Ввод отчества: {patronymic}")
def fill_patronymic(self, patronymic: str) -> None:
    self.locators.patronymic_input.should_be_visible()
    self.locators.patronymic_input.fill(patronymic)


@allure.step("Ввод даты рождения: {birtdate}")
def fill_birthdate(self, birtdate: str) -> None:
    self.locators.birthdate_input.should_be_visible()
    self.locators.birthdate_input.clear()
    self.locators.birthdate_input.fill(birtdate)


@allure.step("Ввод email: {email}")
def fill_email(self, email: str) -> None:
    self.locators.email_input.should_be_visible()
    self.locators.email_input.fill(email)


@allure.step("Нажать на кнопку 'Далее' | Шаг 1")
def click_next_button_first_step(self) -> None:
    # BUG не знаю почему не работает кнопка "Далее" через JS, обычный или принудительный (force) клик
    self.locators.email_input.type(Keys.ENTER)
    self.locators.email_input.type(Keys.ENTER)
    self.explicit_wait(1)
    # 1.
    # self.click_next_button()
    # 2.
    # self.next_button_first_step.should_be_clickable()
    # self.next_button_first_step.click()
    # 3.
    # self.next_button_first_step.type(Keys.ENTER)
    # 4.
    # self.next_button_first_step._page.get_xpath(
    #     self.next_button_first_step._locator
    # ).click(force=True)
