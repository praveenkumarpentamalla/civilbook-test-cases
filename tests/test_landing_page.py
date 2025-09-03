import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage, UpdateProfile
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage
from conftest import setup, setup_logger, pytest_runtest_makereport
from utilities.logger import get_logger
from pages.logout_page import ProfileLogout
from conftest import login
from pages.landing_page import LandingPage


@pytest.mark.usefixtures("setup")
class TestLandingPage:

    def test_landing_page(self, setup_logger):
        setup_logger.info("Test started: Landing Page Navigation")

        # Landing Page

        landing_page = LandingPage(self.driver, setup_logger)
        landing_page.landing()

        setup_logger.info("Test started: Landing Page Navigation completed successfully")