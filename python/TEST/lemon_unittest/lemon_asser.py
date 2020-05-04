import unittest
import inspect

class Foo(object):
    pass

class TestCase01(unittest.TestCase):

    def test_case01(self):
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        self.assertTrue('python'.isupper(),msg='测试是否为大写失败')

    def test_case02(self):
        obj = Foo()
        new_obj = obj
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        self.assertIs(obj,new_obj,msg='测试两个对象是否为同一个对象')

    def test_case03(self):
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        obj = Foo()
        self.assertIsInstance(obj,Foo,msg='测试一个对象是否为某个类的实例')

if __name__ == '__main__':
    unittest.main()
