import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage, UpdateProfile
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from conftest import setup, setup_logger, pytest_runtest_makereport
from utilities.logger import get_logger
from pages.logout_page import ProfileLogout
from conftest import login

@pytest.mark.usefixtures("setup")
class TestAdminLogout:

    def test_logout(self, login):
        driver, logger = login
        logger.info("Test started: admin Logout")

        # Logout Page
        logout_page = ProfileLogout(driver, logger)
        logout_page.logout()
        logger.info("admin Logout successfully")

