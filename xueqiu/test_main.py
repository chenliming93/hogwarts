from frame.main import Main

import os, sys

sys.path.append(os.getcwd())
class TestMain:
    def test_main(self):
        main = Main().goto_marKet().goto_search().search()

