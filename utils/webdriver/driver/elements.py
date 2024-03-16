from selenium.webdriver.remote.webelement import WebElement

from utils.types.webdriver.driver.elements import ElementsInterface
from utils.types.webdriver.driver.page import PageInterface
from utils.webdriver.driver.elements_should import ElementsShould


class Elements(ElementsInterface):
    def __init__(
        self,
        page: PageInterface,
        web_elements: list[WebElement],
        locator: tuple[str, str] | None,
    ):
        from utils.webdriver.driver.element import Element

        self._list: list[Element] = [
            Element(page, element, None) for element in web_elements
        ]
        self._page = page
        self.locator = locator

    def length(self) -> int:
        return len(self._list)

    def is_empty(self) -> bool:
        """Checks if there are zero elements in the list."""
        return self.length() == 0

    def should(
        self, timeout: int = 0, ignored_exceptions: list = None
    ) -> ElementsShould:
        if timeout:
            wait_time = timeout
        else:
            wait_time = self._page.config.driver.wait_time
        return ElementsShould(self._page, self, wait_time, ignored_exceptions)
