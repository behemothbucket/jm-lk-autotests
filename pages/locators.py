from utils.webdriver.driver.page import Page
from page_factory.button import Button
from page_factory.checkbox import Checkbox
from page_factory.div import Div
from page_factory.input import Input
from page_factory.ul import Ul
from page_factory.li import Li
from page_factory.span import Span
from page_factory.iframe import Iframe


class Locators:
    def __init__(self, page: Page) -> None:
        self.phone_input = Input(
            page, locator='//input[@name="userPhone"]', name="Поле ввода телефона"
        )

        self.password_input = Input(
            page, locator='//input[@name="userPassword"]', name="Поле ввода пароля"
        )

        self.sms_code_input = Input(
            page, locator='//input[@name="userCode"]', name="Поле ввода смс"
        )

        self.authorization_page_all_documents_checkbox = Checkbox(
            page,
            locator='//span[text()="Ознакомлен с документами"]/parent::span/preceding-sibling::label',
            name="Чекбокс Ознакомлен со всеми документами",
        )

        self.next_button = Button(
            page, locator='//button[text()="Далее"]', name="Кнопка Далее"
        )

        self.name_input = Input(
            page, locator='//input[@name="userName"]', name="Поле ввода Имя"
        )

        self.surname_input = Input(
            page, locator='//input[@name="surname"]', name="Поле ввода Фамилия"
        )

        self.patronymic_input = Input(
            page, locator='//input[@name="patronymic"]', name="Поле ввода отчество"
        )

        self.birthdate_input = Input(
            page, locator='//input[@name="birthdate"]', name="Поле ввода дата рождения"
        )

        self.email_input = Input(
            page, locator='//input[@name="email"]', name="Поле ввода email"
        )

        self.next_button_first_step = Button(
            page,
            locator='//button[@id="sendPersonalFormBtn"]',
            name="Кнопка Далее | Первый Шаг",
        )

        self.passport_identifier_input = Input(
            page,
            locator='//input[@name="passportIdentifier"]',
            name="Поле серия и номер паспорта",
        )

        self.passport_issue_date_input = Input(
            page,
            locator='//input[@name="passportIssueDate"]',
            name="Поле Дата выдачи паспорта",
        )

        self.passport_issuer_code_input = Input(
            page,
            locator='//input[@name="passportIssuerCode"]',
            name="Поле Код подразделения",
        )

        self.passport_issuer_name_info_input = Input(
            page,
            locator='//input[@name="passportIssuerName_info"]',
            name="Поле Кем выдан",
        )

        self.birthplace_input = Input(
            page, locator='//input[@name="birthPlace"]', name="Поле место рождения"
        )

        self.snils_input = Input(page, locator='//input[@name="snils"]', name="Snils")

        self.address_reg_city_input = Input(
            page,
            locator='//input[@name="addressRegCity"]',
            name="Поле Город",
        )

        self.address_reg_street_input = Input(
            page,
            locator='//input[@name="addressRegStreet"]',
            name="Поле Улица",
        )

        self.address_reg_house_input = Input(
            page,
            locator='//input[@name="addressRegHouse"]',
            name="Поле Дом",
        )

        self.address_reg_flat_input = Input(
            page,
            locator='//input[@name="addressRegFlat"]',
            name="Поле Квартира",
        )

        self.address_reg_city_ul = Ul(
            page,
            locator="//ul[@id='addressRegCity_list']",
            name="Список подсказок DaData город",
        )

        self.address_reg_street_ul = Ul(
            page,
            locator="//ul[@id='addressRegStreet_list']",
            name="Список подсказок DaData Улица",
        )

        self.address_reg_house_ul = Ul(
            page,
            locator="//ul[@id='addressRegHouse_list']",
            name="Список подсказок DaData дом",
        )

        self.registered_address_true_checkbox = Checkbox(
            page,
            locator="//input[@name='radioAddressFact' and @value='true']/following-sibling::span[contains(@class,'radioIcon')]",
            name="Чекбокс (true) Проживаете по адресу регистрации?",
        )

        self.registered_address_false_checkbox = Checkbox(
            page,
            locator="//input[@name='radioAddressFact' and @value='false']/following-sibling::span[contains(@class,'radioIcon')]",
            name="Чекбокс (false) Проживаете по адресу регистрации?",
        )

        self.next_button_second_step = Button(
            page,
            locator="//button[@id='sendPassportFormBtn']",
            name="Кнопка Далее на втором шаге",
        )

        self.passport_photos_popup_modal = Div(
            page,
            locator="//div[@class='popup-modal']",
            name="Модальное окно для загрузки фотографий",
        )

        self.upload_passport_photos_input = Input(
            page,
            locator="//input[@name='uploadPassport']",
            name="Поле для загрузки фото паспорта",
        )

        self.upload_photos_next_button = Button(
            page,
            locator="//span[text()='Далее']",
            name="Кнопка Далее в окне загрузки фото",
        )

        self.job_type_input = Input(
            page,
            locator="//input[@name='jobType']",
            name="Поле ввода Тип занятости",
        )

        self.job_type_ul = Ul(
            page,
            locator="//label[text()='Тип занятости*']/following-sibling::ul",
            name="Список Тип занятости",
        )

        self.job_type_li = Li(
            page,
            locator="(//label[text()='Тип занятости*']/following-sibling::ul/li)[1]",
            name="Элемент списка Тип работы",
        )

        self.job_company_name_input = Input(
            page,
            locator="//input[@name='jobCompanyName']",
            name="Поле Название компании",
        )

        self.job_title_input = Input(
            page,
            locator="//input[@name='jobTitle']",
            name="Поле Название организаци",
        )

        self.salary_input = Input(
            page, locator="//input[@name='salary']", name="Поле Доходы"
        )

        self.expenses_amount_input = Input(
            page, locator="//input[@name='expensesAmount']", name="Поле Расходы"
        )

        self.bankruptcy_true_checkbox = Checkbox(
            page,
            locator="//input[@name='bankruptcyProcessed' and @value='true']/following-sibling::span[contains(@class,'radioIcon')]",
            name="Чекбокс (true) Банкротство",
        )

        self.bankruptcy_false_checkbox = Checkbox(
            page,
            locator="//input[@name='bankruptcyProcessed' and @value='false']/following-sibling::span[contains(@class,'radioIcon')]",
            name="Чекбокс (false) Банкротство",
        )

        self.additional_phone_input = Input(
            page,
            locator="//input[@name='friendPhone']",
            name="Поле ввода Дополнительный номер телефона",
        )

        self.registration_page_all_documents_input = Input(
            page,
            locator="//input[@name='jobPolicy']",
            name="Поле ввода Согласен с подписанием документов",
        )

        self.registration_page_all_documents_checkbox = Checkbox(
            page,
            locator="//span[text()='Согласен с подписанием документов']/preceding-sibling::label",
            name="Чекбокс всех документов на 3 шаге регистрации",
        )

        self.send_application_button = Button(
            page,
            locator="//button[@id='test_make_request']",
            name="Кнопка Отправить заявку",
        )

        self.asp_input = Input(
            page,
            locator="//input[@inputmode='tel' and @type='text']",
            name="Поля ввода ASP",
        )

        self.new_or_current_loan_button = Button(
            page,
            locator="//a[text()='Действующий займ' or text()='Новый займ']",
            name="Кнопка Действующий займ или Новый займ",
        )

        self.current_loan_button = Button(
            page,
            locator="//a[text()='Действующий займ']",
            name="Кнопка Действующий займ",
        )

        self.new_loan_button = Button(
            page,
            locator="//a[text()='Новый займ']",
            name="Кнопка Новый займ",
        )

        self.history_loans_button = Button(
            page,
            locator="//a[text()='История займов']",
            name="Кнопка История займов",
        )

        self.application_number_span = Span(
            page,
            locator="//div[@id='pending_pdl' or @id='approved_pdl']/span",
            name="Текст Займ №...'",
        )

        self.add_card_button = Button(
            page, locator="//button[@id='add_card']", name="Кнопка Указать карту"
        )

        self.sign_agreement_page_title_span = Span(
            page,
            locator="//span[text()='Деньги готовы к зачислению на вашу карту']",
            name="Заголовок страницы подписания договора(привязка карты, услуг)",
        )

        self.add_card_input = Input(
            page, locator="//input[@name='paymentTools']", name="Поле ввода карты"
        )

        self.add_card_ul = Ul(
            page,
            locator="//input[@name]/following-sibling::ul",
            name="Список вариантов добавления карты",
        )

        self.add_card_li = Li(
            page,
            locator="//li[@data-value='modal' and text()='Добавить карту']",
            name="Элемент меню Добавить карту",
        )

        self.payment_iframe = Iframe(
            page,
            locator="//iframe[@name='payment']",
            name="Фрейм для заполенния карты",
        )

        self.pan_input = Input(
            page, locator="//input[@name='pan']", name="Поле ввода *pan*"
        )

        self.submit_input = Input(
            page, locator="//input[@type='submit']", name="Поле ввода Отправить"
        )

        self.get_money_button = Button(
            page, locator="//button[@id='get_money']", name="Кнопка Получить деньги"
        )

        self.loader_text_span = Span(
            page,
            locator="//span[text()='Операция обрабатывается платежной системой']",
            name="Текст обработки платежной системы",
        )

        self.thank_you_button = Button(
            page,
            locator="//a[text()='Хорошо, спасибо!']",
            name="Кнопка Хорошо спасибо",
        )

        self.agreement_number_span = Span(
            page,
            locator="//span[contains(text(),'Займ №')]",
            name="Текст с номером договора",
        )

        self.pay_loan_button = Button(
            page,
            locator="//button[@id='repayBtnForTest']",
            name="Кнопка Погасить займ",
        )

        self.detailed_information_span = Span(
            page,
            locator="//span[text()='Подробная информация']",
            name="Кнопка Подробная информация",
        )

        self.logout_button = Button(
            page,
            locator="//img//following-sibling::span[text()='Выход']",
            name="Кнопка Выход из ЛК",
        )

        self.close_notice_text_button = Button(
            page,
            locator="//div[@class='notice__close']",
            name="Кнопка Закрыть уведомление",
        )

        self.sidebar_menu_item = Span(
            page,
            locator="//span[text()='{}']",
            name="Вкладка в боковом меню (Мои займы, Мои карты, Мои данные)",
        )

        self.forgot_password_button = Button(
            page,
            locator="//a[text()='Я не помню пароль']",
            name="Кнопка Я не помню пароль",
        )

        self.recovery_phone_input = Input(
            page,
            locator="//input[@name='phone']",
            name="Поле ввода номаера телефона на странице восстановаления пароля",
        )

        self.recovery_sms_input = Input(
            page,
            locator="//input[@name='recoveryCheckSMS']",
            name="Поле ввода смс для восстановления пароля",
        )

        self.new_password_input = Input(
            page, locator="//input[@name='newPassword']", name="Поле Новый пароль"
        )

        self.repeat_new_password_input = Input(
            page,
            locator="//input[@name='repeatNewPassword']",
            name="Поле Повторите новый пароль",
        )

        self.change_password_button = Button(
            page,
            locator="//button[contains(text(), 'Сменить пароль')]",
            name="Кнопка Сменить пароль",
        )

        self.success_password_change_status_span = Span(
            page,
            locator="//span[contains(text(), 'Пароль успешно изменен')]",
            name="Информационный текст Пароль успешно изменен",
        )

        self.login_button = Button(
            page, locator="//a[text()='Войти']", name="Кнопка Войти"
        )
