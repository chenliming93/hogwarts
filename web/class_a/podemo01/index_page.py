from selenium import webdriver
from selenium.webdriver.common.by import By

from web.class_a.podemo01.register_page import RegisterPage
from web.class_a.podemo01.login_page import LoginPage

class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
    # 进入登录页
    def got_login(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)

    # 进入到注册页
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)