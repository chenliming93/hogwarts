# @time   :22:00
# @Author :明沫
# @File   :test_calc.py
# @Software:PyCharm
import pytest

from testing.calulator_ import Calculator


def test_a():
    print("test a")


class TestCalc:

    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    ids = ['int_case', 'bignum_case', 'float_case', 'minuses_case', 'zero_case']

    @pytest.mark.parametrize('a,b,except_a', [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-2, -3, -5], [0, 1, 1]],
                             ids=ids)
    def test_add(self, a, b, except_a):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == except_a

    @pytest.mark.parametrize('a,b,except_s', [[1, 1, 0], [0.1, 0.1, 0], [-2, -1, -1], [0, 1, -1]],
                             ids=['int_case', 'float_case', 'minuses_case', 'zero_case'])
    def test_sub(self, a, b, except_s):
        result = self.calc.sub(a, b)
        assert result == except_s

    @pytest.mark.parametrize('a,b,except_m', [[1, 1, 1], [0.1, 0.1, 0.01], [-2, 2, -4], [-2, -1, 2], [0, 1, 0]],
                             ids=['int_case', 'float_case', 'minuses_case', 'minuses_case2', 'zero_case'])
    def test_mul(self, a, b, except_m):
        result = self.calc.mul(a, b)
        assert round(result, 2) == except_m

    @pytest.mark.parametrize('a,b,except_d',
                             [[1, 1, 1], [0.1, 0.1, 1.0], [-2, -1, 2.0], [6, -3, -2], [0, 1, 0], [1, 0, 0]],
                             ids=['int_case', 'float_case', 'minuses_case', 'minuses_case2', 'zero_case', 'zero_case2'])
    def test_div(self, a, b, except_d):
        try:
            self.result = self.calc.div(a, b)
            assert self.result == except_d
        except Exception as e:
            print(e)
