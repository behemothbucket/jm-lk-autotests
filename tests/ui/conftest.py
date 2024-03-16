import pytest

from pages.authorization.authorization_page import AuthorizationPage
from pages.lk.lk_page import LKPage
from pages.recovery.recovery_page import RecoveryPage
from pages.registration.registration_page import RegistrationPage
from utils.webdriver.driver.page import Page


@pytest.fixture(scope="function")
def authorization_page(page: Page) -> AuthorizationPage:
    return AuthorizationPage(page=page)


@pytest.fixture(scope="function")
def lk_page(page: Page) -> LKPage:
    return LKPage(page=page)


@pytest.fixture(scope="function")
def recovery_page(page: Page) -> RecoveryPage:
    return RecoveryPage(page=page)


@pytest.fixture(scope="function")
def pdl_registration(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)
