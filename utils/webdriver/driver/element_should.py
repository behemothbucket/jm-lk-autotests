import allure
from selenium.common.exceptions import TimeoutException
from utils.types.webdriver.driver.element import ElementInterface
from utils.types.webdriver.driver.element_should import ElementShouldInterface
from utils.types.webdriver.driver.page import PageInterface
from utils.webdriver.driver.element_wait import ElementWait
from utils.webdriver.logger import logger


class ElementShould(ElementShouldInterface):
    """ElementShould API: Commands (aka Expectations) for the current Element"""

    def __init__(
        self,
        page: PageInterface,
        element: ElementInterface,
        timeout: int,
        ignored_exceptions: tuple | None = None,
    ):
        self._page = page
        self._element = element
        self._wait = ElementWait(element.web_element, timeout, ignored_exceptions)

    def be_clickable(self) -> ElementInterface:
        """An expectation that the element is displayed and enabled so you can click it"""
        try:
            value = self._wait.until(lambda e: e.is_displayed() and e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element

        raise AssertionError("Элемент не кликабелен")

    def be_hidden(self) -> ElementInterface:
        """An expectation that the element is not displayed but still in the DOM (aka hidden)"""
        try:
            value = self._wait.until(lambda e: e and not e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        raise AssertionError("Элемент не скрыт")

    def be_visible(self) -> ElementInterface:
        """An expectation that the element is displayed"""
        try:
            value = self._wait.until(lambda e: e and e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element

        raise AssertionError("Элемент не отображается")

    def have_text(self, expected_text: str, case_sensitive=True) -> "ElementInterface":
        """An expectation that the element has the given text"""
        logger.info(
            "Page.have_text() - Проверка что элемент содержит текст:\n`%s`",
            expected_text,
        )

        element_text = self._element.web_element.text

        with allure.step(
            f"Фактический текст:\n{element_text}\nОжидаемый текст:\n{expected_text}\nЧувствительность регистра: {case_sensitive}"
        ):
            logger.info(
                f"Фактический текст:\n{element_text}\nОжидаемый текст:\n{expected_text}\nЧувствительность регистра: {case_sensitive}"
            )
            try:
                if case_sensitive:
                    value = self._wait.until(lambda _: element_text == expected_text)
                else:
                    value = self._wait.until(
                        lambda _: element_text.strip().lower() == expected_text.lower()
                    )
            except TimeoutException:
                value = False

            if value:
                return self._element

            raise AssertionError(
                f"Фактический текст:\n `{element_text}`\nОжидаемый текст:\n `{expected_text}`"
            )

    def have_text_in(
        self, expected_text_list: list[str], case_sensitive=True
    ) -> "ElementInterface":
        """An expectation that the element has the given text in list of strings"""
        logger.info(
            "Page.have_text_in() - Наличие текста элемента в массиве строк:\n`%s`",
            expected_text_list,
        )

        element_text = self._element.web_element.text

        with allure.step(
            f"Фактический текст:\n{element_text}\nОжидаемый текст в массиве:\n{expected_text_list}\nЧувствительность регистра: {case_sensitive}"
        ):
            logger.info(
                f"Фактический текст:\n{element_text}\nОжидаемый текст в массиве:\n{expected_text_list}\nЧувствительность регистра: {case_sensitive}"
            )
            try:
                if case_sensitive:
                    value = self._wait.until(
                        lambda _: element_text in expected_text_list
                    )
                else:
                    _expected_text_list = list(
                        map(lambda text: text.lower(), expected_text_list)
                    )
                    value = self._wait.until(
                        lambda _: element_text.strip().lower() in _expected_text_list
                    )
            except TimeoutException:
                value = False

            if value:
                return self._element

            raise AssertionError(
                f"Фактический текст:\n {element_text}\nОжидаемый текст в массиве строк:\n {expected_text_list}"
            )
