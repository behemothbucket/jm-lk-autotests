from datetime import datetime


class UnderAgeError(Exception):
    def __str__(self) -> str:
        return "You must be at least 18 years old. You are underage."


def check_adulthood(date_of_birth: datetime) -> None:
    today: datetime = datetime.today()
    age: int = today.year - date_of_birth.year

    if today.month < date_of_birth.month or (
        today.month == date_of_birth.month and today.day < date_of_birth.day
    ):
        age -= 1

    if age < 18:
        raise UnderAgeError()


def get_legal_years() -> tuple:
    return datetime.now().year - 71, datetime.now().year - 19


def get_passport_issue_date(birthdate: str) -> str:
    date_object = datetime.strptime(birthdate, "%d.%m.%Y")
    new_date = date_object.replace(year=date_object.year + 18).strftime("%d.%m.%Y")
    return new_date
