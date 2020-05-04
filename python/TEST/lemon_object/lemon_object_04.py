class Animal:
    """
    创建动物
    """
    def __init__(self,name,age,color):
        """

        :param name: 名字
        :param age: 年龄
        :param color: 毛色
        """
        self.name,self.age ,self.color = name, age, color

    def eat(self):
        print('{}需要吃东西'.format(self.name))

    def dirnk(self):
        print('{}需要喝水'.format(self.name))

    def run(self):
        print('{}会跑步'.format(self.name))

    def sleep(self):
        print('{}会睡觉'.format(self.name))

class Dog:
    """
    定义狗类
    """
    def __init__(self,name,age,color):
        """

        :param name: 名字
        :param age: 年龄
        :param color: 毛色
        """
        self.name,self.age ,self.color = name, age, color

    def eat(self):
        print('{}需要吃东西'.format(self.name))

    def dirnk(self):
        print('{}需要喝水'.format(self.name))

    def run(self):
        print('{}会跑步'.format(self.name))

    def sleep(self):
        print('{}会睡觉'.format(self.name))

    def bark(self):
        print('{}会汪汪叫'.format(self.name))


class Cat:
    """
    定义猫类
    :return:
    """
    def __init__(self,name,age,color):
        """

        :param name: 名字
        :param age: 年龄
        :param color: 毛色
        """
        self.name,self.age ,self.color = name, age, color

    def eat(self):
        print('{}需要吃东西'.format(self.name))

    def dirnk(self):
        print('{}需要喝水'.format(self.name))

    def run(self):
        print('{}会跑步'.format(self.name))

    def catch(self):
        print('{}会汪汪叫'.format(self.name))

class XiaoTianQuan:

    def __init__(self,name,age,color):
        """

        :param name: 名字
        :param age: 年龄
        :param color: 毛色
        """
        self.name,self.age ,self.color = name, age, color

    def eat(self):
        print('{}需要吃东西'.format(self.name))

    def dirnk(self):
        print('{}需要喝水'.format(self.name))

    def run(self):
        print('{}会跑步'.format(self.name))

    def sleep(self):
        print('{}会睡觉'.format(self.name))

    def bark(self):
        print('{}会汪汪叫'.format(self.name))




    def fly(self):
        print('{}会飞'.format(self.name))


a_little_dog = XiaoTianQuan('啸天犬',10000,'金色')
a_little_dog.fly()