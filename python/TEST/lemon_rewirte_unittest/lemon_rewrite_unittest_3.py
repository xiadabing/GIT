
#使用@unpack装饰器，来进一步拆包
#痛点、每个实例方法是一条用例，代码冗余太多
#反复对excel进行操作，可读性差，效率也非常低
#程序不够灵活，代码很难重用
#单元测试中，实例方法执行的时候如果抛出异常，那么这个实例方法将会终止执行，
#有for循环的话，那么代码会一致执行

#ddt，是一种数据驱动思想，是一个辅助加载测试用例的一个库
import unittest
import inspect
from ddt import ddt, data,unpack




@ddt
class TestCase01(unittest.TestCase):
    """
    使用ddt来加载测试数据
    """

    @data([True,False,None],("可优","柠檬小姐姐",0))
    @unpack   #使用anpack,那么所有的元素要能支持拆包才行，序列类型才可以拆包（list、tuple）
    def test_case(self,*val): #拆包以后会变成多个位置参数，因为val要改成*val可变参数
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        print("值为：{}\n类型为：{}\n".format(*val,type(*val)))
        self.assertTrue(*val)

if __name__ == '__main__':
    unittest.main()
