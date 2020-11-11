from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from web.class_a.podemo01.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def saomo(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self.driver)
