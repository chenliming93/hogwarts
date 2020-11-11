
from frame.market import Market
from frame.base_page import BasePage
import os, sys

sys.path.append(os.getcwd())


class Main(BasePage):
    def goto_marKet(self):
        # 制造假的弹框
        # self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.parse_yaml("main.yaml", "goto_marKet")
        return Market(self.driver)
