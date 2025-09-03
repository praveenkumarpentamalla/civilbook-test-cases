from selenium.webdriver.common.by import By
from utilities.BaseClass import Base


class LandingPage(Base):
    home_button = (By.XPATH, '//a[@href="https://civilbook.in/#home"]')
    departments_button = (By.XPATH, '//a[@href="https://civilbook.in/#departments"]')
    about_button = (By.XPATH, '//a[@href="https://civilbook.in/about"]')
    contact_button = (By.XPATH, '//a[@href="https://civilbook.in/contact"]')

    def landing(self):
        self.driver.get("https://civilbook.in")
        print("Home URL:", self.driver.current_url)
        print("Home Title:", self.driver.title)

        self.click(self.home_button)
        print("Home URL:", self.driver.current_url)
        print("Home Title:", self.driver.title)

        self.click(self.departments_button)
        print("Home URL:", self.driver.current_url)
        print("Home Title:", self.driver.title)

        self.click(self.about_button)
        print("Home URL:", self.driver.current_url)
        print("Home Title:", self.driver.title)
        
        self.click(self.contact_button)
        print("Home URL:", self.driver.current_url)
        print("Home Title:", self.driver.title)

