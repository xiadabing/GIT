#格式化操作format
name='keyou'
print('我叫{}!'.format(name))
print(f'{name}')

#序列类型支持的操作（列表/字典/元组）
zodiac_animal = "猴鸡狗猪鼠牛虎龙蛇马羊"
#1 支持索引取值
print(zodiac_animal[3])

#2 切片操作
print(zodiac_animal[1:-3])

#3 成员关系操作（in 或者 not in）
print("猴" in zodiac_animal)

#4 连接操作(+)
new_zodiac = zodiac_animal+"猫"
print(new_zodiac)

#5 重复操作符(*)
print(zodiac_animal*3)

#6 支持遍历
for item in zodiac_animal:
     print(item)

#7 支持求长度（ len()）

#8 支持内置函数






