from web.class_a.podemo01.index_page import IndexPage


class TestWx:
    def setup(self):
        self.index = IndexPage()
    def test_wx(self):
       # assert self.index.goto_register().register()
        assert self.index.got_login().goto_register().register()