from logging import disable
import random
from typing_extensions import deprecated
from mimesis import Person, Address, Datetime, Finance
from mimesis.locales import Locale
from mimesis.builtins import RussiaSpecProvider
from mimesis.random import Random
from mimesis.enums import Gender
from utils.fakers.helpers.dates import get_legal_years, get_passport_issue_date
from utils.constants.features import AutoApproveType


class FakeClient:
    def __init__(self):
        self.person = Person(locale=Locale.RU)
        self.gender = random.choice([Gender.FEMALE, Gender.MALE])
        self.ru = RussiaSpecProvider()
        self.address = Address(locale=Locale.RU)
        self.dt = Datetime()
        self.fin = Finance(locale=Locale.RU)
        self.random = Random()

    def generate_random_phone_number(
        self, type: AutoApproveType = AutoApproveType.AUTO_APPROVE
    ) -> str:
        last_number = {
            AutoApproveType.AUTO_APPROVE: 0,
            AutoApproveType.REJECT: 9,
            AutoApproveType.VERIFICATOR: 5,
        }.get(type)

        if last_number is None:
            raise ValueError(
                "Invalid type value. Must be NumberType.AUTO_APPROVE, NumberType.REJECT or NumberType.VERIFICATOR."
            )

        emulator_mask = "79########{}".format(last_number)

        return self.person.telephone(mask=emulator_mask)

    def generate_random_password(self) -> str:
        password_length = self.random.randint(6, 16)
        return self.person.password(length=password_length)

    def generate_russian_name(self) -> str:
        return self.person.first_name(gender=self.gender)

    def generate_russian_surname(self) -> str:
        return self.person.last_name(gender=self.gender)

    def generate_russian_patronymic(self) -> str:
        return self.ru.patronymic(gender=self.gender)

    def generate_birthdate(self) -> str:
        legal_start_year, legal_end_year = get_legal_years()
        birthdate = self.dt.datetime(start=legal_start_year, end=legal_end_year)
        return birthdate.strftime("%d.%m.%Y")

    def generate_random_email(self) -> str:
        return self.person.email()

    def generate_passport_issuer_identifier(self) -> str:
        return self.ru.series_and_number().replace(" ", "", 1)

    def generate_passport_issue_date(self, birthdate: str) -> str:
        passport_issue_date = get_passport_issue_date(birthdate)
        return passport_issue_date

    def generate_passport_issuer_code(self) -> str:
        return "123-456"

    def generate_passport_issuer_name(self) -> str:
        random_sentence = self.ru.generate_sentence()
        return " ".join(random_sentence.split()[:3])

    def generate_birthplace(self) -> str:
        return self.address.country()

    def generate_snils(self) -> str:
        return self.ru.snils()

    def generate_address_reg_city(self) -> str:
        return "г Москва город Москва"

    def generate_address_reg_street(self) -> str:
        return "ул Арбат"

    def generate_address_reg_house(self) -> str:
        return "дом 1"

    def generate_address_reg_flat(self) -> str:
        return "1"

    def generate_job_company_name(self) -> str:
        return self.fin.company()

    def generate_job_company_title(self) -> str:
        return self.person.occupation()

    def generate_salary(self) -> str:
        return str(self.random.randint(a=1, b=999999))

    def generate_expenses_amount(self) -> str:
        return str(self.random.randint(a=1, b=999999))

    def generate_amount(self, range: list[int]) -> str:
        min, max = range
        return str(self.random.randint(a=min, b=max))

    def generate_period(self, range: list[int], in_weeks: bool = False) -> str:
        min, max = range
        period = self.random.randint(a=min, b=max)
        if in_weeks:
            period /= 7
        return str(period)

    def generate_friend_fio(self) -> str:
        return self.person.full_name(gender=self.gender)
