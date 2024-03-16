from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from selenium.webdriver.remote.webelement import WebElement

if TYPE_CHECKING:
    from utils.types.webdriver.driver.element_should import \
        ElementShouldInterface


class ElementInterface(ABC):
    @property
    @abstractmethod
    def web_element(self) -> WebElement: ...

    @abstractmethod
    def should(
        self, timeout: int = 0, ignored_exceptions: tuple | None = None
    ) -> "ElementShouldInterface": ...

    @abstractmethod
    def click(self, force: bool = False) -> "ElementInterface": ...

    @abstractmethod
    def type(self, *args) -> "ElementInterface": ...

    @abstractmethod
    def fill(self, *args) -> "ElementInterface": ...

    @abstractmethod
    def clear(self) -> "ElementInterface": ...

    @abstractmethod
    def is_displayed(self) -> bool: ...
