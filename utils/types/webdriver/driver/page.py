from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from config import UIConfig

if TYPE_CHECKING:
    from utils.types.webdriver.driver.element import ElementInterface
    from utils.types.webdriver.driver.elements import ElementsInterface
    from utils.types.webdriver.driver.page_wait import PageWaitInterface


class PageInterface(ABC):
    config: UIConfig

    @abstractmethod
    def __init__(self) -> None:
        ...

    @property
    @abstractmethod
    def webdriver(self) -> WebDriver:
        ...

    @abstractmethod
    def wait(
        self,
        timeout: int,
        use_self: bool = False,
        ignored_exceptions: tuple | None = None,
    ) -> Union[WebDriverWait, "PageWaitInterface"]:
        ...

    @abstractmethod
    def url(self) -> str:
        ...

    @abstractmethod
    def visit(self, url: str) -> "PageInterface":
        ...

    @abstractmethod
    def reload(self) -> "PageInterface":
        ...

    @abstractmethod
    def get_xpath(self, xpath: str, timeout: int) -> "ElementInterface":
        ...

    @abstractmethod
    def find_xpath(self, xpath: str, timeout: int) -> "ElementsInterface":
        ...

    @abstractmethod
    def quit(self):
        ...

    @abstractmethod
    def screenshot(self, filename: str) -> str:
        ...

    @abstractmethod
    def maximize_window(self) -> "PageInterface":
        ...

    @abstractmethod
    def execute_script(self, script: str, *args) -> "PageInterface":
        ...
