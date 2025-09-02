import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
class Base:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = logger

    def open_url(self, url):
        self.driver.get(url)
        if self.logger:
            self.logger.info(f"Opened URL: {url}")

    def find(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        if self.logger:
            self.logger.info(f"Found element: {locator}")
        return element

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.logger.info(f"Clicking element: {locator}")
        try:
            element.click()
        except ElementClickInterceptedException:
            self.logger.warning(f"Element click intercepted for {locator}, retrying with JS click")
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        if self.logger:
            self.logger.info(f"Typed '{text}' into {locator}")

    def get_title(self):
        title = self.driver.title
        if self.logger:
            self.logger.info(f"Page title: {title}")
        return title

    def get_url(self):
        url = self.driver.current_url
        if self.logger:
            self.logger.info(f"Page URL: {url}")
        return url
