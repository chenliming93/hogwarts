from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from web.class_a.podemo.page.BasePage import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver
    #     self.driver.implicitly_wait(5)

    def addmenber(self,username,acctid,mobile):
        # 姓名
        time.sleep(2)
        self.driver.find_element(By.ID,"username").send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.XPATH,'.//*[@id="memberAdd_acctid"]').send_keys(acctid)
        self.driver.find_element(By.XPATH,'.//*[@id="memberAdd_phone"]').send_keys(mobile)
        self.driver.find_element(By.XPATH,'//form[@class="js_member_editor_form"]/div[1]/a[2]').click()
        check_box = (By.CSS_SELECTOR,".ww_checkbox")
        element = wait_for_click(check_box)

        time.sleep(3)

    def get_menber(self,value):
        # menberslist =self.finds(By.XPATH,'//*[@id="member_list"]//td[2]')
        # titlelist = []
        # for element in menberslist:
        #     titlelist.append(element.get_attribute("title"))
        total_list = []
        while True:
            menberslist = self.finds(By.XPATH, '//*[@id="member_list"]//td[2]')
            titlelist = []
            for element in menberslist:
                titlelist.append(element.get_attribute("title"))

            if value in titlelist:
                return True
            total_list = total_list + titlelist
            result:str = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            num,total = result.split('/',1)
            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR,'.ww_pageNav_info_arrowWrap js_next_page').click()

        return total_list







