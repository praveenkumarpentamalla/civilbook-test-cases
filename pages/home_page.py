from selenium.webdriver.common.by import By
from utilities.BaseClass import Base

class HomePage(Base):
    profile_icon = (By.XPATH, '//img[@src="https://beta.civilbook.in/images/user/user.png"]')
    setting_option = (By.XPATH, '//a[@href="https://beta.civilbook.in/setting"]')

    def go_to_settings(self):
        self.click(self.profile_icon)
        self.click(self.setting_option)


class UpdateProfile(Base):
    profile_icon = (By.XPATH, '//img[@src="https://beta.civilbook.in/images/user/user.png"]')
    profle_option = (By.XPATH, '//a[@href="https://beta.civilbook.in/setting/profile_form"]')

    def go_to_profile(self):
        self.click(self.profile_icon)
        self.click(self.profle_option)