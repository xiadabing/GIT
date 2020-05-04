

class MathOper:

    def __init__(self,one_num,two_num):
        self.one_num,self.two_num = one_num,two_num

    def add(self):
        return self.one_num+self.two_num

    def minus(self):
        return self.one_num-self.two_num

    def multiply(self):
        return self.one_num * self.two_num

    def divide(self):
        try:
            return round(self.one_num / self.two_num,2)
        except ZeroDivisionError:
            return '*'

if __name__ == '__main__':
    nums =(10,0)