import allure
from pages.base.base_page import BasePage
from utils.webdriver.driver.page import Page
from utils.constants.routes import Routes


class LKPage(BasePage):
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

    @allure.step("Проверка: Текущая страница ЛК")
    def check_current_loan_page(self) -> None:
        self.page.wait_for_correct_current_url(Routes.LK.value)
        self.locators.current_loan_button.should_be_visible()
        self.locators.pay_loan_button.should_be_visible()
        self.locators.close_notice_text_button.should_be_clickable()
        self.locators.close_notice_text_button.click()

    @allure.step("Проверка: Кнопки 'Текущий займ' и 'История займов'")
    def check_loan_buttons(self) -> None:
        self.locators.history_loans_button.should_be_visible()
        self.locators.history_loans_button.click()
        self.page.wait_for_correct_current_url(Routes.HISTORY_LOANS.value)
        self.locators.current_loan_button.should_be_visible()
        self.locators.current_loan_button.click()
        self.page.wait_for_correct_current_url(Routes.LK.value)
        # TODO: доделать после решения бага /description 500

    @allure.step("Проверка: доп. информация по займу и документы")
    def check_detailed_information_and_documents(self) -> None:
        self.locators.detailed_information_span.should_be_visible()
        # ... blocked by BUG

    @allure.step("Проверка: Навигация в боковом меню")
    def check_sidebar_navigation(self) -> None:
        self.locators.sidebar_menu_item.navigate_to_sidebar_menu_item("Мои данные")
        self.page.wait_for_correct_current_url(Routes.USER_DATA_PERSONAL.value)
        self.locators.sidebar_menu_item.navigate_to_sidebar_menu_item("Мои карты")
        self.page.wait_for_correct_current_url(Routes.USER_CARDS.value)
        self.locators.sidebar_menu_item.navigate_to_sidebar_menu_item("Мои займы")
        self.page.wait_for_correct_current_url(Routes.LK.value)

    @allure.step("Выйти из ЛК")
    def logout(self) -> None:
        self.locators.logout_button.should_be_visible()
        self.locators.logout_button.click()
        self.page.wait_for_correct_current_url(Routes.AUTHORIZATION.value)
        self.locators.phone_input.should_be_visible()
