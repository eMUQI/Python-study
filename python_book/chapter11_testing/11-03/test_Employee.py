'''
11-3 雇员：编写一个名为 Employee 的类，其方法 __init__() 接受名、姓和年薪，并
将它们都存储在属性中。编写一个名为 give_raise() 的方法，它默认将年薪增加 5000
美元，但也能够接受其他的年薪增加量。
为 Employee 编写一个测试用例，其中包含两个测试方法： test_give_default_
raise() 和 test_give_custom_raise() 。使用方法 setUp() ，以免在每个测试方法中都创
建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
'''
import unittest
from Employee import Employee


class SalaryIncrementTest(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Elon", "Musk", 100000)

    def test_give_default_(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 105000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(100)
        self.assertEqual(self.my_employee.salary, 100100)


unittest.main()
