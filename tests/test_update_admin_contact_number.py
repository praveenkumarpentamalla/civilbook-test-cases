import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage, UpdateProfile
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from conftest import setup, setup_logger, pytest_runtest_makereport
from utilities.logger import get_logger
from conftest import login

@pytest.mark.usefixtures("setup")
class TestSettings:

    def test_update_number(self, login):
        driver, logger = login
        logger.info("Test started: Update admin contact number")

        # Home Page
        home_page = UpdateProfile(driver, logger)
        home_page.go_to_profile()

        # Settings Page
        profile_page = ProfilePage(driver, logger)
        profile_page.update_contact_number("121212121")
        logger.info("admin contact number updated successfully")

        
