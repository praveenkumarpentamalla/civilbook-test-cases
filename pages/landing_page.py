from selenium.webdriver.common.by import By
from utilities.BaseClass import Base


class LandingPage(Base):
    home_button = (By.XPATH, '//a[@href="https://civilbook.in/#home"]')
    departments_button = (By.XPATH, '//a[@href="https://civilbook.in/#departments"]')
    about_button = (By.XPATH, '//a[@href="https://civilbook.in/about"]')
    contact_button = (By.XPATH, '//a[@href="https://civilbook.in/contact"]')

    def landing(self):
        self.driver.get("https://civilbook.in")
        self.click(self.home_button)
        self.click(self.departments_button)
        self.click(self.about_button)
        self.click(self.contact_button)

