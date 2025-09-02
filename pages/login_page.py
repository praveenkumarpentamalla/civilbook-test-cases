from selenium.webdriver.common.by import By
from utilities.BaseClass import Base


class LoginPage(Base):
    email_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    login_btn = (By.XPATH, '//button[text()="Sign In with Password"]')


    def login(self, email, password):
        self.type(self.email_input, email)
        self.type(self.password_input, password)
        self.click(self.login_btn)