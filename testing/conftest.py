# @time   :23:12
# @Author :明沫
# @File   :conftest.py
# @Software:PyCharm

import os, sys

sys.path.append(os.getcwd())
from testing.calulator_ import Calculator
import pytest


@pytest.fixture(scope="class")
def get_calc():
    calc = Calculator()
    print("开始计算 ")
    yield calc
    print("结束计算 ")
