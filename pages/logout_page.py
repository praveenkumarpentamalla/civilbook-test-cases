from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import Base

class ProfileLogout(Base):
    profile_icon = (By.XPATH, '//img[@src="https://beta.civilbook.in/images/user/user.png"]')
    logout_option = (By.XPATH, '//a[contains(text(), "Log out")]')

    def logout(self):
        self.driver.get("https://beta.civilbook.in/home")

        wait = WebDriverWait(self.driver, 15)

        profile = wait.until(EC.element_to_be_clickable(self.profile_icon))
        profile.click()

        logout_btn = wait.until(EC.element_to_be_clickable(self.logout_option))
        logout_btn.click()
