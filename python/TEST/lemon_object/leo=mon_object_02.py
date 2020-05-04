from TEST.lemon_object.lemon_object_01 import Person

keyou = Person('keyou',17,190)

#可以使用类.静态方法名
Person.weather_forecast()
#可以使用对象.静态方法名
keyou.weather_forecast()