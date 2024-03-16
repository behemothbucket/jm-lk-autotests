from enum import Enum


class Suite(str, Enum):
    SANITY = "Sanity"
    SMOKE = "Smoke"
    REGRESSION = "Regression"
