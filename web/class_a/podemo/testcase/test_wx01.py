from web.class_a.podemo.page.main_page import MainPage


class TestWx:
    def setup(self):
        self.main = MainPage()
    def test_wx(self):
        username = "b125771"
        acctid = "b6638771"
        mobile = "13505536000"
        men = self.main.goto_addmember()
        men.addmenber(username,acctid,mobile)

        assert username in men.get_menber(username)
