import unittest
import inspect

from TEST.lemon_unittest.lemon_unnitest_02 import MathOper

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
        file_name = 'record_run_result.txt'
        print('打开【{}】文件'.format(file_name))
        file = open(file_name,mode='a') #以追加模式打开文件
        file.write('{}\n'.format('开始执行用例')) #将开始执行用例写入文件中
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
        finally:
            #用例执行结束，关闭文件
            print('关闭【{}】文件'.format(file_name))
            file.write('{}\n'.format('用例执行结束'))
            file.close()

    def test_two_neg_divide(self):
        """
        测试2个正数相除
        :return:
        """
        #定义一个文件路径
        file_name = 'record_run_result.txt'
        print('打开【{}】文件'.format(file_name))
        file = open(file_name,mode='a') #以追加模式打开文件
        file.write('{}\n'.format('开始执行用例')) #将开始执行用例写入文件中
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
        finally:
            #用例执行结束，关闭文件
            print('关闭【{}】文件'.format(file_name))
            file.write('{}\n'.format('用例执行结束'))
            file.close()
if __name__ == '__main__':
    unittest.main()


