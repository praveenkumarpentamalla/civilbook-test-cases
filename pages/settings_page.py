from selenium.webdriver.common.by import By
from utilities.BaseClass import Base

class SettingsPage(Base):
    socket_url = (By.NAME, "socket_url")
    save_btn = (By.ID, "saveBtn")

    def update_socket_url(self, url):
        self.type(self.socket_url, url)
        self.click(self.save_btn)

