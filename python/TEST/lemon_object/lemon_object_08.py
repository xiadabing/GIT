class Animal:
    """
    创建动物
    """

    def __init__(self, name, age, color):
        """

        :param name: 名字
        :param age: 年龄
        :param color: 毛色
        """
        self.name, self.age, self.color = name, age, color

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
    def __init__(self,name,age,color,job):
        #这里是，丢弃父类方法，重写构造方法
        self.name, self.age, self.color, self.job = name, age, color, job
        #不丢弃父类构造方法，而是在父类的基础上修改
        #super()相当于父类的一个对象
        #先调用父类的构造方法设置这三个属性，然后再添加一个job属性
        #相当于对父类的拓展
        super().__init__(name,age,color)
        self.job = job
    def fly(self):
        print('{}会飞'.format(self.name))

    def sleep(self):
        """
        方法的重写：
        当定义了一个跟父类一样的方法时，会覆盖父类的方法，父类的方法不会被执行
        1，首先检查本身有没有这个方法，如果没有去父类中查找，有则直接执行本身这个方法
        :return:
        """
        print('{}不需要睡觉'.format(self.name))

    def eat(self):
        super().eat()
        print('{}想吃蟠桃'.format(self.name))



a_little_dog = XiaoTianQuan('啸天犬', 2, '黄色','守护天庭')
print(a_little_dog.job)
a_little_dog.eat()

#python中没有明确的多态定义，处处皆多态
