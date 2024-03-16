import allure
import re
from page_factory.component import Component


class Span(Component):
    @property
    def type_of(self) -> str:
        return "span"

    def get_app_or_agree_id(self, **kwargs) -> str:
        with allure.step("Получить номер договора или заявки"):
            element = self.get_element(**kwargs)
            element_text = element.text
            return "".join(re.findall(r"\d", element_text))

    def navigate_to_sidebar_menu_item(self, item_name: str) -> None:
        with allure.step(f"В боковом меню нажать на '{item_name}'"):
            menu_item_locator = self._locator.format(item_name)
            element = self._page.get_xpath(menu_item_locator)
            element.click()
