import os
from enum import Enum
from itertools import chain

from dotenv import load_dotenv

load_dotenv()


class Feature(str, Enum):
    CLIENTS = "Clients"


class Account(str, Enum):
    PHONE = "*-*-*-*-*-*-"
    DEFAULT_PASSWORD = "*-*-*-*-*-*-"
    RECOVERY_PHONE = "*-*-*-*-*-*-"
    RECOVERY_NEW_PASSWORD = "*-*-*-*-*-*-"
    RECOVERY_SMS = "*-*-*-*-*-*-"
    PAN = os.getenv("PAN", default="*-*-*-*-*-*-")


class Payment(str, Enum):
    PROVIDER = os.getenv("PROVIDER", default="QIWI")


class AutoApproveType(Enum):
    AUTO_APPROVE = "auto_approve"
    REJECT = "reject"
    VERIFICATOR = "verificator"


class Tariff(Enum):
    MEGA_START = (
        "MEGA_START",
        "start",
        list(reversed(range(3000, 10500, 500))),
        list(range(10, 31)),
    )
    PRAKTIK = (
        "PRAKTIK",
        "middle",
        list(range(11000, 31000, 1000)),
        list(range(10, 31)),
    )
    PROFI = (
        "PROFI",
        "end",
        list(chain(range(25000, 31000, 1000), range(40000, 101000, 20000))),
        [10, 16, 20, 24],
    )

    def __new__(
        cls, value: str, locator: str, amount_range: list, period_range: list
    ) -> "Tariff":
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(
        self, value: str, locator: str, amount_range: list, period_range: list
    ) -> None:
        self.locator = locator
        self.amount_range = amount_range
        self.period_range = period_range
