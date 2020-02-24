'''
11-2 人口数量：修改前面的函数，使其包含第三个必不可少的形参 population ，并
返回一个格式为 City, Country – population xxx 的字符串，如 Santiago, Chile –
population 5000000 。运行 test_cities.py ，确认测试 test_city_country() 未通过。
修改上述函数，将形参 population 设置为可选的。再次运行 test_cities.py，确认测
试 test_city_country() 又通过了。
再编写一个名为 test_city_country_population() 的测试，核实可以使用类似于
'santiago' 、 'chile' 和 'population=5000000' 这样的值来调用这个函数。再次运行
test_cities.py ，确认测试 test_city_country_population() 通过了。
'''

import unittest
from city_functions import get_formatted_name


class NameFormatterTest(unittest.TestCase):
    '''测试city _functions.py'''

    def test_city_country(self):
        formatted_name = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = get_formatted_name(
            'santiago', 'chile', population=5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


unittest.main()
