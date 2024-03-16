from page_factory.component import Component


class Checkbox(Component):
    @property
    def type_of(self) -> str:
        return "checkbox"

    def documents_state(self) -> bool:
        input_state_value_locator = "//input[@name='jobPolicy' and (@value='true' or @value='false' or @value='')]"
        state_element = self._page.get_xpath(input_state_value_locator)
        state = state_element.get_attribute("value")
        return state == "true"
