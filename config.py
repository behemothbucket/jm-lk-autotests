import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from utils.webdriver.factory.browser import Browser

load_dotenv()

# WARNING: перелючить в True перед пушем
HEADLESS = True


class DriverConfig(BaseSettings):
    browser: Browser = Field(
        default=Browser.CHROME, json_schema_extra={"BROWSER": os.getenv("BROWSER")}
    )
    remote_url: str | None = None
    headless: bool = HEADLESS
    wait_time: int = 10
    page_load_wait_time: int = 30
    options: list[str] = [
        "ignore-certificate-errors",
        "--no-sandbox",
        "disable-infobars",
        "--disable-extensions",
        "--disable-gpu",
    ]

    if headless:
        options.append("--window-size=1920,1080")
        options.append("--headless")

    capabilities: dict[str, str] = {}
    experimental_options: list[dict] | None = None
    seleniumwire_options: dict = {}
    extension_paths: list[str] | None = None
    webdriver_kwargs: dict | None = None
    version: str | None = None
    local_path: str | None = "//usr//bin//chromedriver"


class LoggingConfig(BaseSettings):
    log_level: str = "INFO"
    screenshots_on: bool = Field(
        default=True, json_schema_extra={"SCREENSHOTS_ON": os.getenv("SCREENSHOTS_ON")}
    )
    screenshots_dir: str = Field(
        default="./screenshots",
        json_schema_extra={"SCREENSHOTS_DIR": os.getenv("SCREENSHOTS_DIR")},
    )


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int = 1920
    height: int = 1080
    orientation: str = "portrait"


class UIConfig(BaseSettings):
    base_url: str = Field(default=os.getenv("BASE_URL"))
    driver: DriverConfig = DriverConfig()
    logging: LoggingConfig = LoggingConfig()
    viewport: ViewportConfig = ViewportConfig()
    custom: dict = {}


@lru_cache()
def get_ui_config() -> UIConfig:
    return UIConfig()
