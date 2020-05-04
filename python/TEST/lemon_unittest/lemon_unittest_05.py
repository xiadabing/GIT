
import unittest
import inspect
#导入自定义模块
from TEST.lemon_unittest.lemon_unnitest_02 import MathOper

def setUpModule():
    """
    打开文件
    :return:
    """
    global file_name
    global file
    print('\n{:=^40s}\n'.format('开始执行测试用例'))
    file_name = 'homework.txt'
    print('打开【{}】文件'.format(file_name))
    file = open(file_name,mode='a',encoding='utf-8')
    file.write('\n{:=^40s}\n'.format('开始执行测试用例'))

def tearDownModule():
    """
    重写父类的方法
    每一个用例执行以后会被调用
    :return:
    """
    print("\n{:=^40s}\n".format('用例执行结束'))
    print('关闭【{}】文件'.format(file_name))
    file.write('{:=^40s}\n'.format('用例执行结束'))
    file.close()

class TestMulti(unittest.TestCase):  #继承unittest.TeatCase类
    """
    测试2数相乘
    """
    def test_negatives_multi(self):  #测试用例方法名必须以test开头
        """
        测试2个负数相乘
        :return:
        """
        #能够查看当前运行的实例方法名称
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        #获取实际结果
        real_result = MathOper(-2,-4).multiply()
        #验证实际结果与预期结果是否一致
        expect_result = 8
        msg = '测试2个负数相除相乘'
        try:
            self.assertEqual(expect_result,real_result,msg='测试2个负数相乘失败')

        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{},执行结果为：{}\n'.format(msg, 'pass'))



    def test_neg_pos_multi(self):
        """
        2.测试一个正数一个负数相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(2, -5).multiply()
        expect_result = -10
        msg = '测试一个正数和一个负数相乘'
        try:
            self.assertEqual(expect_result, real_result, msg='测试一个正数和一个负数相乘')
        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{},执行结果为：{}\n'.format(msg, 'pass'))


    def test_two_zero(self):
        """
        两个0相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(0, 0).multiply()
        expect_result = 0
        msg = '测试2个0相乘失败'
        try:
            self.assertEqual(expect_result, real_result, msg='测试2个0相乘失败')
        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{},执行结果为：{}\n'.format(msg, 'pass'))

    def test_two_pos_muti(self):
        """
        两个正数相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(3, 5).multiply()
        expect_result = 15
        msg = '测试2个正数相乘失败'
        try:
            self.assertEqual(expect_result, real_result, msg='测试2个正数相乘失败')
        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg, 'fail', e))
            raise e
        else:
            file.write('{},执行结果为：{}\n'.format(msg, 'pass'))



class TestDivide(unittest.TestCase):
    """
    测试除法运算
    """
    def test_two_pos_divide(self):
        """
        测试2个正数相除
        :return:
        """
        #定义一个文件路径
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        actual_result = MathOper(8,4).divide()
        expect_result = 2
        msg = '测试2个正数相乘'
        try:
            self.assertEqual(expect_result,actual_result,msg='测试2个负数相乘失败')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg,'fail',e))
            raise e
        else:
            file.write('{},执行结果为：{}\n'.format(msg,'pass'))
    def test_two_neg_divide(self):
        """
        测试2个正数相除
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        actual_result = MathOper(-8,-4).divide()
        expect_result = 2
        msg = '测试2个负数相乘'
        try:
            self.assertEqual(expect_result,actual_result,msg='测试2个负数相除正例')
        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg,'fail',e))
            raise e
        else:
            file.write('{},执行结果为：{}\n'.format(msg,'pass'))

if __name__ == '__main__':
    unittest.main()