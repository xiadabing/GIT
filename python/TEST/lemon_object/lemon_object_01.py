class Person:
    hair = 3
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height


    def run(self):
        self.weather_forecast()
        print('在类里面:',self.eat())
        print('{}可以跑步'.format(self.name))

    def eat(self):
        print('{}会吃东西'.format(self.name))

    @classmethod
    def anger(cls): #类方法
        cls.weather_forecast() #静态方法内部调用方式
        cls.head = 2

    @staticmethod #定义类中静态方法
    def weather_forecast():  #我们往往会把与类相关的函数，放到类中来，作为静态方法
        """
        播报天气
        :return:
        """
        print('天气：晴朗')
        print('温度：22')
        print("适合出游")

keyou = Person('keyou',17,190)
#可以使用类.静态方法名
# Person.weather_forecast()
#可以使用对象.静态方法名
# keyou.weather_forecast()
#Person.hair = 4
#keyou.hair = 5
print(keyou.hair)
Person.anger()
