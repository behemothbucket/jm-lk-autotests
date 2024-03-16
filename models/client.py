from pydantic import BaseModel, ConfigDict, Field

from utils.constants.features import Account
from utils.constants.routes import Path
from utils.fakers.client import FakeClient


class Client(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    amount: str = Field()
    days: str = Field()
    phone_number: str = Field()
    sms: str = Field(default=Account.DEFAULT_PASSWORD)
    name: str = Field()
    surname: str = Field()
    patronymic: str = Field()
    birthdate: str = Field(default="01.01.2000")
    email: str = Field()
    passport_issuer_identifier: str = Field(default="0000 100000")
    passport_issue_date: str = Field(default="01.01.2015")
    passport_issuer_code: str = Field(default="123-456")
    passport_issuer_name: str = Field(default="Тест Тест")
    birthplace: str = Field(default="гор Москва")
    snils: str = Field(default="012-345-678 19")
    address_reg_city: str = Field(default="г Москва город Москва")
    address_reg_street: str = Field(default="улица Арбат")
    address_reg_house: str = Field(default="дом 1")
    address_reg_flat: str = Field(default="1")
    passport_photo_path: str = Field(
        default=Path.WORKSPACE_DIR + "/resources/img/passport/cat.jpg"
    )
    job_company_name: str = Field()
    job_title: str = Field()
    salary: str = Field()
    expenses_amount: str = Field()
    friend_phone_number: str = Field(default="*-*-*-*-*-*-")
    friend_fio: str = Field()
    asp: str = Field(default="*-*-*-*-*-*-")
    pan: str = Field(default="*-*-*-*-*-*-")

    # Иногда mimesis генерирует странные фамилии из-за чего валится регистрация.

    @classmethod
    def create(cls, amount: str = "5000", days: str = "15") -> "Client":
        fake_client: FakeClient = FakeClient()

        # amount = (
        #     fake_client.generate_amount(amount) if isinstance(amount, list) else amount
        # )
        # days = fake_client.generate_period(days) if isinstance(days, list) else days
        phone_number = fake_client.generate_random_phone_number()
        name = fake_client.generate_russian_name()
        surname = fake_client.generate_russian_surname()
        patronymic = fake_client.generate_russian_patronymic()
        # birthdate = fake_client.generate_birthdate()
        email = fake_client.generate_random_email()
        # passport_issue_date = fake_client.generate_passport_issue_date(birthdate)
        job_company_name = fake_client.generate_job_company_name()
        job_title = fake_client.generate_job_company_title()
        salary = fake_client.generate_salary()
        expenses_amount = fake_client.generate_expenses_amount()
        friend_fio = fake_client.generate_friend_fio()
        pan = Account.PAN

        return Client(
            amount=amount,
            days=days,
            phone_number=phone_number,
            name=name,
            surname=surname,
            patronymic=patronymic,
            # birthdate=birthdate,
            email=email,
            # passport_issue_date=passport_issue_date,
            job_company_name=job_company_name,
            job_title=job_title,
            salary=salary,
            pan=pan,
            expenses_amount=expenses_amount,
            friend_fio=friend_fio,
        )
