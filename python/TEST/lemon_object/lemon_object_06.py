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

class Dog(Animal):
    """
    Animal 父类，基类
    dog 子类
    """
    def bark(self):
        print('{}会汪汪叫'.format(self.name))

class Cat(Animal):
    """
    定义猫类
    """
    def catch(self):
        print('{}会汪汪叫'.format(self.name))

class XiaoTianQuan(Dog):
    """
    定义啸天犬类
    """
    def fly(self):
        print('{}会飞'.format(self.name))

wangcai = Dog('旺财',1,'灰色')
wangcai.eat()
print("*" * 50)

#集成父类会将父亲的所有的实例方法和类方法，类属性都继承（私有方法除外）

a_little_dog = XiaoTianQuan('啸天犬',2,'黄色')
a_little_dog.sleep()
a_little_dog.fly()
