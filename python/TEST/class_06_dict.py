#字典相关操作
user_info = {'name':'小明','age':18,
             'gender':True,'height':1.75}

#1 求字典长度
print(len(user_info))

#2 获取某个值
print(user_info['name'])  #键不存在会报错
print(user_info.get('motto','lemon')) #键不存在可以返回制定的值

#3 获取所有的keys
print(user_info.keys())

#4 获取所有的values
print(user_info.values())

#5  修改值
user_info['name']='keyou'
print(user_info)

#6 拼接字典
anthor_info = {'motto':'never stop!',('haha,'):'jhkhk' }
user_info.update(anthor_info)
print('user_info=,',user_info)
print('anthor_info=',anthor_info)

# 删除指定键值队
user_info.pop('name')
print('user_info',user_info)
print(user_info.popitem()) #删除最后一组数据 返回值为键值队

#7 清空
user_info.clear()
