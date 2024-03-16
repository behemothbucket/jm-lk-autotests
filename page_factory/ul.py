import allure
import re
from selenium.webdriver import Keys
from page_factory.component import Component
from selenium.webdriver.common.action_chains import ActionChains


class Ul(Component):
    @property
    def type_of(self) -> str:
        return "ul"

    def fill(self, value: str, **kwargs):
        with allure.step(f'Ввести в поле "{self.name}" значение "{value}"'):
            element = self.get_element(**kwargs)
            element.fill(value)

    def type(self, value: str, **kwargs):
        with allure.step(f'Ввод значения "{value}" в список "{self.name}"'):
            element = self.get_element(**kwargs)
            element.type(value)

    def select_first_address_variant(self, **kwargs):
        with allure.step(f'Выбрать первый вариант из подсказок для адреса: "{self.name}"'):
            element = self.get_element(**kwargs)
            list_name: str | None = self.extract_list_name(self._locator)
            script = (
                f"setTimeout(() => {{const ul = document.querySelector('#{list_name}');"
                'ul.style = "overflow: visible;visibility:visible;";},0);'
            )
            element._page.execute_script(script)
            element.type(Keys.ENTER)

    def extract_list_name(self, list_name: str) -> str | None:
        pattern = r"'(.*?)'"
        result = re.search(pattern, list_name)
        if result:
            value = result.group(1)
            return value
        return None

    def show_job_ul(self, **kwargs):
        with allure.step(f'Выбрать первый вариант из подсказок для Типа занятости'):
            element = self.get_element(**kwargs)
            script = "setTimeout(() => {const ul = document.querySelector('form#JobForm ul');ul.style = 'overflow: visible;visibility:visible;';},0);"
            element._page.execute_script(script)

    def click_add_another_card(self):
        with allure.step("Нажать на кнопку 'Другая карта' в поле привязки карт"):
            actions = ActionChains(self._page._webdriver)
            actions.send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
            actions.perform()
