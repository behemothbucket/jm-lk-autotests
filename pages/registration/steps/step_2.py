import allure


@allure.step('Ввод серии и номера паспорта: "{passport_series_number}"')
def fill_passport_series_and_number(self, passport_series_number: str) -> None:
    self.locators.passport_identifier_input.should_be_visible()
    self.locators.passport_identifier_input.fill(passport_series_number)


@allure.step('Ввод даты выдачи паспорта: "{passport_issue_date}"')
def fill_passport_issue_date(self, passport_issue_date: str) -> None:
    self.locators.passport_issue_date_input.should_be_visible()
    self.locators.passport_issue_date_input.fill(passport_issue_date)
    self.explicit_wait(1)
    self.locators.passport_identifier_input.click()
    self.locators.passport_issue_date_input.click()


@allure.step('Ввод код подразделения: "{passport_issuer_code}"')
def fill_passport_issuer_code(self, passport_issuer_code: str) -> None:
    self.locators.passport_issuer_code_input.should_be_visible()
    self.locators.passport_issuer_code_input.fill(passport_issuer_code)


@allure.step('Ввод кем выдан паспорт: "{passport_issuer_name}"')
def fill_passport_issuer_name(self, passport_issuer_name: str) -> None:
    self.move_to_bottom_of_page()
    self.locators.passport_issuer_name_info_input.should_be_visible()
    self.locators.passport_issuer_name_info_input.fill(passport_issuer_name)


@allure.step('Ввод место рождения: "{birthplace}"')
def fill_birthplace(self, birthplace: str) -> None:
    self.locators.birthplace_input.should_be_visible()
    self.locators.birthplace_input.fill(birthplace)


@allure.step('Ввод СНИЛС: "{snils}"')
def fill_snils(self, snils: str) -> None:
    self.locators.snils_input.should_be_visible()
    self.locators.snils_input.clear()
    self.locators.snils_input.fill(snils)


@allure.step('Ввод города(адрес регистрации): "{city}"')
def fill_address_reg_city(self, city: str) -> None:
    self.locators.address_reg_city_input.should_be_visible()
    self.locators.address_reg_city_input.fill(city)
    self.locators.address_reg_city_ul.select_first_address_variant()
    self.explicit_wait(1)


@allure.step('Ввод улицы(адрес регистрации): "{street}"')
def fill_address_reg_street(self, street: str) -> None:
    self.locators.address_reg_street_input.should_be_visible()
    self.locators.address_reg_street_input.fill(street)
    self.locators.address_reg_street_ul.select_first_address_variant()
    self.explicit_wait(1)


@allure.step('Ввод дома(адрес регистрации): "{house}"')
def fill_address_reg_house(self, house: str) -> None:
    self.locators.address_reg_house_input.should_be_visible()
    self.locators.address_reg_house_input.fill(house)
    self.locators.address_reg_house_ul.select_first_address_variant()
    self.explicit_wait(1)


@allure.step('Ввод квартиры(адрес регистрации): "{flat}"')
def fill_address_reg_flat(self, flat: str) -> None:
    self.locators.address_reg_flat_input.should_be_visible()
    self.locators.address_reg_flat_input.fill(flat)
    self.explicit_wait(1)


@allure.step("Отметить чекбокс: 'Проживаете по адресу регистрации?' [{state}]")
def click_registered_address_checkbox(self, state: bool) -> None:
    if state:
        self.locators.registered_address_true_checkbox.click()
    else:
        self.locators.registered_address_false_checkbox.click()
    self.explicit_wait(1)


@allure.step("Нажать на кнопку 'Далее' | Шаг 2")
def click_next_button_second_step(self) -> None:
    self.move_to_bottom_of_page()
    self.explicit_wait(1)
    self.locators.next_button_second_step.should_be_clickable()
    self.locators.next_button_second_step.click()


@allure.step("Загрузить фото паспорта")
def upload_passport_photos(self, path: str) -> None:
    self.locators.passport_photos_popup_modal.should_be_visible()
    self.locators.upload_passport_photos_input.is_displayed()
    self.locators.upload_passport_photos_input.upload_passport_photos(path)
    self.locators.upload_photos_next_button.should_be_visible()
    self.locators.upload_photos_next_button.click(force=True)
    self.explicit_wait(1)
