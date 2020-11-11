import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from web.class_a.podemo.page.BasePage import BasePage
from web.class_a.podemo.page.add_member_page import AddMemberPage
from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def __init__(self):
    #     options = Options()
    #     options.debugger_address='localhost:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #     # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     self.driver.implicitly_wait(5)
    def goto_addmember(self):

        self.find(By.CSS_SELECTOR,'#menu_contacts').click()
        time.sleep(2)
        # 添加成功
        loc = (By.CSS_SELECTOR,'.js_has_member>div>a:nth-child(2)').click()
        def wait_for_next(x:WebDriver):
            try:
                x.find_element(*loc).click()
                return x.find_element(By.ID,"username")
            except:
                return False

        WebDriverWait(self.driver,10).until(wait_for_next)
        return AddMemberPage(self.driver)


