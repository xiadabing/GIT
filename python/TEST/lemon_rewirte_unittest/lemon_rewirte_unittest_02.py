#痛点、每个实例方法是一条用例，代码冗余太多
#反复对excel进行操作，可读性差，效率也非常低
#程序不够灵活，代码很难重用
#单元测试中，实例方法执行的时候如果抛出异常，那么这个实例方法将会终止执行，
#有for循环的话，那么代码会一致执行

#ddt，是一种数据驱动思想，是一个辅助加载测试用例的一个库
import unittest
import inspect
from ddt import ddt, data

test_cases = (10,0,True,False,None,2,12.1," ","可优")


@ddt  #ddt是用来装饰类的，需要与ddt装饰器一起使用，装饰器就是给类和函数添加额外的功能
class TestCase01(unittest.TestCase):
    """
    使用ddt来加载测试数据
    """

    @data(*test_cases)  #将元组拆包为多个位置参数（序列类型），推荐使用
    #@data(10,0,True,False,None,2,12.1,"","可优")
    def test_case(self,val):
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        print("值为：{}\n类型为：{}\n".format(val,type(val)))
        self.assertTrue(val)

if __name__ == '__main__':
    unittest.main()
#用例执行的条数，与data装饰器的（位置）参数个数一致
#每执行一条用例，会自动将一个参数传给val，当最后一个参数传给val，
#且用例执行结束之后，程序才执行完毕，这个过程相当于遍历参数
#ddt和data要一起使用