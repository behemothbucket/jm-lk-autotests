import allure
from time import sleep
from utils.webdriver.driver.page import Page
from pages.locators import Locators


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.locators = Locators(self.page)

    def visit(self, url: str) -> None:
        with allure.step(f"Перейти на страницу '{url}'"):
            self.page.visit(url)

    def reload(self) -> Page:
        page_url = self.page.url()
        with allure.step(f"Перезагрузить страницу '{page_url}'"):
            return self.page.reload()

    def explicit_wait(self, seconds: int) -> None:
        with allure.step(f"Явное ожидание {seconds} секунд(-а/-ы)"):
            sleep(seconds)

    def move_to_bottom_of_page(self) -> None:
        with allure.step("Перевести фокус в конец страницы"):
            self.page.move_to_bottom_of_page()
