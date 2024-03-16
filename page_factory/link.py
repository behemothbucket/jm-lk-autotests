import allure
from page_factory.component import Component
from utils.webdriver.driver.element import Element
from utils.constants.routes import Routes
from utils.webdriver.logger import logger
from selenium.common import ElementNotInteractableException
from utils.webdriver.logger import logger


class Link(Component):
    @property
    def type_of(self) -> str:
        return "link"

    def check_link(
        self,
        callback=None,
        **kwargs,
    ) -> None:
        """Открыть ссылку в новой вкладке и проверить что url соответствует ожидаемому.

        Аргументы:

        callback -- ссылка на функцию
        **kwargs -- передача параметра в качестве аргумента (для callback)


        """
        logger.info("Link.check_link() - Проверка ссылки в элементе")

        elements: list[Element] = self.get_elements()._list

        with allure.step(
            "Нажать на каждую ссылку и проверить ожидаемый и фактический URL"
        ):
            problem_element: Element | None = elements[0]
            try:
                for element in elements:
                    problem_element = element

                    url = element.get_attribute("href")

                    if Routes.ANCHOR.value in url:
                        logger.info(f"Ссылка-якорь: {url}")
                        continue

                    with allure.step(
                        f'Проверка: открыть URL элемента "{element.text}" и проверить фактический URL'
                    ):
                        logger.info(
                            f'Проверка: открыть URL элемента "{element.text}" и проверить фактический URL'
                        )

                    self._page.open_new_tab_via_js(url)

                    self._page.switch_to_tab_action_close_tab(url, callback, **kwargs)

            except ElementNotInteractableException:
                raise Exception(
                    f'Элемент "{problem_element.text}" не кликабелен или не явлется ссылкой'
                )
