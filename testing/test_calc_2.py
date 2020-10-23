# @time   :22:00
# @Author :明沫
# @File   :test_calc.py
# @Software:PyCharm
import pytest
import yaml


def test_a():
    print("test a")


def get_datas():
    with open(r"F:\HGWARTS\HOGWARTS15\datas\calc.yaml", encoding='GBK') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']  # 0
    add_ids = datas['add']['ids']  # 1
    add_datas_float = datas['add']['data_float']  # 2
    add_ids_float = datas['add']['ids_float']  # 3
    # 减法
    sub_datas = datas['sub']['datas']  # 4
    sub_ids = datas['sub']['ids']  # 5
    # 乘法
    mul_datas = datas['mul']['datas']  # 6
    mul_ids = datas['mul']['ids']  # 7
    # 除法
    div_datas = datas['div']['datas']  # 8
    div_ids = datas['div']['ids']  # 9
    div_data_price_float = datas['div']['data_price_float']  # 10
    div_ids_price_float = datas['div']['ids_price_float']  # 11
    div_data_div_zero = datas['div']['data_div_zero']  # 12
    div_ids__div_zero = datas['div']['ids__div_zero']  # 13
    return [add_datas, add_ids, add_datas_float, add_ids_float, sub_datas, sub_ids, mul_datas, mul_ids,
            div_datas, div_ids, div_data_price_float, div_ids_price_float, div_data_div_zero, div_ids__div_zero]


def steps(addstepfile, calc, a, b, except_):
    with open(addstepfile) as f:
        steps = yaml.safe_load(f)

    # for step in steps:
    #     if 'add' == step:
    #         result = calc.add(a,b)
    #     elif 'add1' == step:
    #         result == calc.add1(a,b)
    #     assert except_ == result


class TestCounter:
    # 加法
    @pytest.mark.parametrize('a,b,except_a', get_datas()[0], ids=get_datas()[1])
    @pytest.mark.first
    def test_add1(self, get_calc, a, b, except_a):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == except_a
        print("第一个执行")

    # 加法
    @pytest.mark.parametrize('a,b,except_a', get_datas()[2], ids=get_datas()[3])
    @pytest.mark.run(order=2)
    def test_add2(self, get_calc, a, b, except_a):
        result = get_calc.add(a, b)
        assert round(result, 2) == except_a
        print("第二个执行")

    @pytest.mark.parametrize('a,b,except_s', get_datas()[4], ids=get_datas()[5])
    @pytest.mark.run(order=6)
    def test_sub(self, get_calc, a, b, except_s):
        result = get_calc.sub(a, b)
        assert result == except_s

    @pytest.mark.parametrize('a,b,except_m', get_datas()[6], ids=get_datas()[7])
    @pytest.mark.run(order=-1)
    def test_mul(self, get_calc, a, b, except_m):
        result = get_calc.mul(a, b)
        assert round(result, 2) == except_m

    @pytest.mark.parametrize('a,b,except_d1', get_datas()[8], ids=get_datas()[9])
    @pytest.mark.run(order=3)
    def test_div1(self, get_calc, a, b, except_d1):
        self.result = get_calc.div(a, b)
        assert self.result == except_d1

    @pytest.mark.parametrize('a,b,except_d2', get_datas()[10], ids=get_datas()[11])
    @pytest.mark.run(order=4)
    def test_price_float(self, get_calc, a, b, except_d2):
        self.result = get_calc.div(a, b)
        assert self.result == except_d2

    @pytest.mark.parametrize('a,b', get_datas()[-2], ids=get_datas()[-1])
    @pytest.mark.run(order=5)
    def test_div_zero(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError) as e:
            self.result = get_calc.div(a, b)
            print("除数为0！")

    # def test_add_step(self):
    #     a = 1
    #     b = 1
    #     except_=2
    #     steps(r'F:\HGWARTS\HOGWARTS15\step\add_steps.yml',self.calc,a,b,except_)


if __name__ == '__main__':
    pytest.main('[ --alluredir ./result]')
    # pytest.main('[allure serve ./result]')
