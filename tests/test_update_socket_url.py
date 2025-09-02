import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from utilities.conftest import setup, setup_logger, pytest_runtest_makereport
from utilities.logger import get_logger


@pytest.mark.usefixtures("setup")
class TestSettings:

    def test_update_socket_url(self, setup_logger):
        logger = setup_logger
        driver = self.driver

        logger.info("Test started: Update Socket URL")

        # Login Page
        login_page = LoginPage(driver, logger)
        login_page.login("admin@fugenwebtech.com", "jsrjsr80")

        # Home Page
        home_page = HomePage(driver, logger)
        home_page.go_to_settings()

        # Settings Page
        settings_page = SettingsPage(driver, logger)
        settings_page.update_socket_url("https://beta.civilbook.in")

        # Assert
        assert "setting" in driver.current_url, "Settings page not opened"
        logger.info("Socket URL updated successfully")
