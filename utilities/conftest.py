import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import get_logger
from pages.login_page import LoginPage
import os


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome, firefox, or internetexplorer"
    )


@pytest.fixture
def login(setup, setup_logger):
    driver = setup
    logger = setup_logger

    login_page = LoginPage(driver, logger)
    
    email = "XXXXXXXX"
    password = "XXXXXXX"

    login_page.login(email, password)
    return driver, logger


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser_name == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name == "internetexplorer":
        from selenium.webdriver.ie.service import Service as IEService
        from webdriver_manager.microsoft import IEDriverManager
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://beta.civilbook.in/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def setup_logger():
    return get_logger()


# Attach screenshot on every test (pass or fail)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":  # After test is executed
        driver = getattr(item.instance, "driver", None)
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            # Attach to HTML report if plugin is used
            if "pytest_html" in item.config.pluginmanager.list_plugin_distinfo():
                extra = getattr(item.config, "_html", None).extras
                if extra is not None:
                    from pytest_html import extras
                    item.extra = getattr(item, "extra", [])
                    item.extra.append(extras.image(screenshot_path))
