import allure
from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page
from utils.constants.routes import Routes


class RecoveryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Ввод номера телефона: '{recovery_phone}'")
    def fill_phone_number(self, recovery_phone: str) -> None:
        self.locators.phone_input.should_be_visible()
        self.locators.phone_input.fill(recovery_phone)

    @allure.step("Нажать на кнопку 'Я не помню пароль'")
    def click_on_forgot_password_button(self):
        self.locators.forgot_password_button.should_be_clickable()
        self.locators.forgot_password_button.click()
        self.page.wait_for_correct_current_url(Routes.RECOVERY.value)

    @allure.step("Ввод номера телефона: '{recovery_phone}' и SMS '{recovery_sms}'")
    def fill_phone_number_and_sms(self, recovery_phone: str, recovery_sms: str):
        self.locators.recovery_phone_input.should_be_visible()
        self.locators.recovery_phone_input.fill(recovery_phone)
        self.locators.next_button.should_be_clickable()
        self.locators.next_button.click()
        self.locators.recovery_sms_input.should_be_visible()
        self.locators.recovery_sms_input.fill(recovery_sms)
        self.locators.next_button.should_be_clickable()
        self.locators.next_button.click()

    @allure.step("Ввод нового пароля: '{recovery_password}' и зайти в ЛК")
    def fill_new_passoword_and_login(self, recovery_password: str):
        self.locators.new_password_input.should_be_visible()
        self.locators.new_password_input.fill(recovery_password)
        self.locators.repeat_new_password_input.should_be_visible()
        self.locators.repeat_new_password_input.fill(recovery_password)
        self.locators.change_password_button.should_be_clickable()
        self.locators.change_password_button.click()
        self.locators.success_password_change_status_span.should_be_visible()
        self.locators.login_button.should_be_clickable()
        self.locators.login_button.click()
