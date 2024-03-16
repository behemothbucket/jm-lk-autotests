import allure

from pages.base.base_page import BasePage
from utils.constants.routes import Routes
from utils.webdriver.driver.page import Page


class AuthorizationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Ввод номера телефона: '{phone_number}'")
    def fill_phone_number(self, phone_number: str) -> None:
        self.locators.phone_input.should_be_visible()
        self.locators.phone_input.fill(phone_number)

    @allure.step("Ввод пароля: '{password}'")
    def fill_password(self, password: str) -> None:
        self.locators.password_input.should_be_visible()
        self.locators.password_input.fill(password)

    @allure.step("Нажать на кнопку 'Далее'")
    def click_next_button(self) -> None:
        self.locators.next_button.should_be_clickable()
        self.locators.next_button.click()

    @allure.step("Проверка: Открыта страница ЛК")
    def check_current_loan_page(self) -> None:
        self.page.wait_for_correct_current_url(Routes.LK.value)
        self.locators.current_loan_button.should_be_visible()
        self.locators.pay_loan_button.should_be_visible()
