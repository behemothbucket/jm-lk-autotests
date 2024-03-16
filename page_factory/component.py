import allure
from selenium.common.exceptions import StaleElementReferenceException
from utils.webdriver.driver.element import Element
from utils.webdriver.driver.elements import Elements
from utils.webdriver.driver.page import Page


class Component:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self._page = page
        self._locator = locator
        self._name = name

    @property
    def type_of(self) -> str:
        return "component"

    @property
    def name(self) -> str:
        return self._name

    def get_element(self, **kwargs) -> Element:
        locator = self._locator.format(**kwargs)

        with allure.step(f'Найти элемент с именем "{self.name}"'):
            return self._page.get_xpath(locator)

    def get_elements(self, **kwargs) -> Elements:
        locator = self._locator.format(**kwargs)

        with allure.step(f'Найти элементы с именем "{self.name}"'):
            return self._page.find_xpath(locator)

    def click(self, force: bool = False, **kwargs) -> None:
        with allure.step(f'Нажать на "{self.name}"'):
            element = self.get_element(**kwargs)
            element.click(force)

    def is_displayed(self, **kwargs) -> bool:
        """Метод is_displayed() в Selenium проверяет,
        присутствует ли и отображается ли определенный элемент.
        Если элемент отображается, возвращаемое значение истинно
        Если нет, то возвращаемое значение является ложным."""

        with allure.step(f'Проверка: "{self.name}" отображается'):
            element = self.get_element(**kwargs)
            return element.is_displayed()

    def should_be_visible(self, **kwargs) -> None:
        """Метод should_be_visible() проверяет, является ли элемент видимым, но отличие заключается в том (is_displayed()),
        что если элемент не отображается, то вызывается исключение, указывающее на несоответствие ожиданиям.
        """
        with allure.step(f'Ожидание того, что "{self.name}" будет отображаться'):
            try:
                element = self.get_element(**kwargs)
                element.should().be_visible()
            except StaleElementReferenceException:
                self.should_be_visible(**kwargs)

    def should_be_clickable(self, **kwargs) -> None:
        with allure.step(f'Ожидание того, что "{self.name}" можно кликнуть'):
            try:
                element = self.get_element(**kwargs)
                element.should().be_clickable()
            except StaleElementReferenceException:
                self.should_be_clickable(**kwargs)

    def should_have_text(self, text: str, **kwargs) -> None:
        with allure.step(
            f'Проверить что элемент "{self.name}" содержит текст "{text}"'
        ):
            try:
                element = self.get_element(**kwargs)
                element.should().have_text(text)
            except StaleElementReferenceException:
                self.should_have_text(text, **kwargs)
