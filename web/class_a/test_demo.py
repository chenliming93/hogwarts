from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import shelve

class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        # options.debugger_address='127.0.0.1:9222'
        options.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(3)

    def test_cookie(self):
        # get_cookies() 可以获取当前打开的页面的Cookie信息
        # cookies = self.driver.get_cookies()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850078208853'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'otqlFIg5c9xgcTuRlet_HPfL2XJrye4GBCpQBM3n2zOIToS2hv0LF2zlgPxEZn9zxygCris9mq0keKW_wm6Bn1Jx2ks6pjO33jDqPbmJoY8uzmZ24VKwgrwYdkV_6eLEdcN6QjtKj6gaFi888eu3OR90A3GBopUcKN7xXNuH3IR68bY6dHAH_aGnHQRjEkiKMEoP0MYLS6B6y6PdLD7VDriG5du5nPRul7XHnmf1qm0n5J6vF7LMVUV0J5-_vawaYw-af27KXXbhRk1Qjy1k0A'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850078208853'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324979169747'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'CS78Dv775n1b-CG6JupWPs3s3NXJZmX-OVl4cm6mUhpPCedutW998OIndOz8Jolh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6933382'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603541148, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8gff64t'},
            {'domain': '.qq.com', 'expiry': 1603599440, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1532387382.1603509616'},
            {'domain': '.qq.com', 'expiry': 1666585040, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.642223725.1603509616'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635045612, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'a21a3843a441fd5947b1da1ee64cf1d2f7513187b5a6ab256fc686f82b5168a5'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '667099978'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'aaDBP0j5sW'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606105039, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '4217523580930275'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3426669568'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.refresh()
        time.sleep(3)
