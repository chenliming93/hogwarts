import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
class TestContact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = 'launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(240)
    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        name = "东方不败04"
        gender = "男"
        moblie = "13555571135"
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        if gender == "男":
            WebDriverWait(self.driver,20).until(lambda x:x.find_element(MobileBy.XPATH,'//*[@text="女"]'))
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]').send_keys(moblie)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        time.sleep(3)
        print(self.driver.page_source)

        result = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.TextView"]').text
        print(result)
        assert result == "添加成功"





