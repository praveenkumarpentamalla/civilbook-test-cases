from selenium.webdriver.common.by import By
from utilities.BaseClass import Base


class ProfilePage(Base):
    contact_number = (By.NAME, "contact_number")
    update_btn = (By.XPATH, "//input[@type='submit' and @value='Update']")

    def update_contact_number(self, number):
        self.type(self.contact_number, number)
        self.click(self.update_btn)
