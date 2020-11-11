from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    driver: WebDriver
    base_url=""

    def __init__(self,driver:WebDriver):
        if driver == None:
            options = Options()
            options.debugger_address='localhost:9222'
            self.driver = webdriver.Chrome(options=options)
        else:
            self.driver=driver
        if self.base_url!="":
            self.driver.get(self.base_url)

    def find(self,by,loc):
        self.driver.find_element(by,loc)

    def finds(self,by,loc):
        self.driver.find_element(by,loc)

    def wait_for_click(self,loc):
        element = WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(loc))
        return element
