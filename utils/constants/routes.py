import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class Routes(str, Enum):
    AUTHORIZATION = "/login"
    LK = "/user/loans"
    HISTORY_LOANS = "/user/loans/history"
    USER_DATA_PERSONAL = "/user/data/personal"
    USER_CARDS = "/user/cards"
    RECOVERY = "/recovery"
    ANCHOR = "/#"
    API_EMULATOR_BASE_URL = os.getenv("API_EMULATOR_BASE_URL", default="*-*-*-*-*-*-")


class Path(str, Enum):
    WORKSPACE_DIR = os.path.abspath(os.curdir)
