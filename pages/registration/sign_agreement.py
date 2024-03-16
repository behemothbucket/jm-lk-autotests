import allure
from pages.registration.steps.step_3 import fill_asp_code


@allure.step("Проверка: Открыта страница привязки карты и доп.услуг")
def check_sign_agreement_page(self):
    self.locators.sign_agreement_page_title_span.should_be_visible()


@allure.step("Привязать банковскую карту")
def add_card(self, pan: str) -> None:
    self.locators.add_card_input.should_be_visible()
    self.locators.add_card_ul.click_add_another_card()
    self.locators.payment_iframe.should_be_visible()
    self.locators.payment_iframe.switch_to_iframe()
    self.locators.pan_input.should_be_visible()
    self.locators.pan_input.clear()
    self.locators.pan_input.fill(pan)
    self.locators.submit_input.should_be_visible()
    self.locators.submit_input.click()
    self.locators.payment_iframe.switch_to_default()


@allure.step("Дождаться успешной транзакции...")
def check_payment_transaction_status(self) -> None:
    try:
        self.locators.thank_you_button.should_be_visible()
        self.locators.thank_you_button.should_be_clickable()
        self.locators.thank_you_button.click()
        self.retry_count = 0
    except:
        if self.retry_count == 3:
            raise Exception("Payment transaction failed")
        try:
            self.loader_text_span.should_be_visible()
            self.explicit_wait(2)
            ++self.retry_count
            check_payment_transaction_status(self)
        except:
            self.reload()
            fill_asp_code(self, self.client.asp)
            ++self.retry_count
            self.check_payment_transaction_status(self)
