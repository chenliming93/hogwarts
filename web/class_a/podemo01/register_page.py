from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
class RegisterPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def register(self):
        company_name = 'qq'
        admin_name = "11"
        mobile = '1212'
        self.driver.find_element(By.ID,'corp_name').send_keys(company_name)
        self.driver.find_element(By.ID,'manager_name').send_keys(admin_name)
        self.driver.find_element(By.ID,'manager_name').send_keys(mobile)
        return True