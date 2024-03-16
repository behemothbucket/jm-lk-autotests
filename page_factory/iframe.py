import allure
from page_factory.component import Component


class Iframe(Component):
    @property
    def type_of(self) -> str:
        return "iframe"

    def switch_to_iframe(self, **kwargs) -> None:
        with allure.step("Переключиться на iframe"):
            element = self.get_element(**kwargs)
            self._page.webdriver.switch_to.frame(element._web_element)

    def switch_to_default(self):
        with allure.step("Переключиться в обычное состояние (из iframe)"):
            self._page.webdriver.switch_to.default_content()
