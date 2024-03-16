import allure


@allure.step("Выбрать тип занятости (первый вариант)")
def choose_job_type(self) -> None:
    self.move_to_bottom_of_page()
    self.locators.job_type_input.should_be_visible()
    self.locators.job_type_ul.show_job_ul()
    self.explicit_wait(1)
    self.locators.job_type_li.should_be_clickable()
    self.locators.job_type_li.click()


@allure.step("Ввод названия компании: {company_name}")
def fill_job_company_name(self, company_name: str) -> None:
    self.locators.job_company_name_input.should_be_visible()
    self.locators.job_company_name_input.fill(company_name)


@allure.step("Ввод должности: {job_title}")
def fill_job_title(self, job_title: str) -> None:
    self.locators.job_title_input.should_be_visible()
    self.locators.job_title_input.fill(job_title)


@allure.step("Ввод суммы дохода: {salary}")
def fill_salary(self, salary: str) -> None:
    self.locators.salary_input.should_be_visible()
    self.locators.salary_input.fill(salary)


@allure.step("Ввод суммы расходов: {expenses_amount}")
def fill_expenses_amount(self, expenses_amount: str) -> None:
    self.locators.expenses_amount_input.should_be_visible()
    self.locators.expenses_amount_input.fill(expenses_amount)


@allure.step("Отметить чекбокс: Банкротство [{state}]")
def click_bankruptcy_checkbox(self, state: bool) -> None:
    if state == True:
        self.locators.bankruptcy_true_checkbox.click()
    else:
        self.locators.bankruptcy_false_checkbox.click(force=True)
    self.explicit_wait(1)


@allure.step("Ввод доп. номер телефона: {additional_phone_number}")
def fill_additional_phone_number(self, additional_phone_number: str) -> None:
    self.locators.additional_phone_input.is_displayed()
    self.locators.additional_phone_input.fill(additional_phone_number)


@allure.step("Отметить все документы к согласию")
def click_all_documents_registration_page_checkbox(self) -> None:
    if not self.locators.registration_page_all_documents_checkbox.documents_state():
        self.locators.registration_page_all_documents_checkbox.should_be_visible()
        self.locators.registration_page_all_documents_checkbox.should_be_clickable()
        self.locators.registration_page_all_documents_checkbox.click(force=True)


@allure.step("Нажать на кнопку 'Отправить заявку' | Шаг 3")
def click_send_application_button(self, force: bool = False) -> None:
    self.move_to_bottom_of_page()
    self.explicit_wait(1)
    self.locators.send_application_button.should_be_visible()
    self.locators.send_application_button.should_be_clickable()
    self.locators.send_application_button.click(force=True)


@allure.step("Ввод ASP: {asp}")
def fill_asp_code(self, asp: str) -> None:
    self.move_to_bottom_of_page()
    self.explicit_wait(2)
    self.locators.asp_input.should_be_visible()
    self.locators.asp_input.enter_asp(asp)
