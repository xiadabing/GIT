#列表相关操作
#定义列表
a_var = "python自动化测试16班人才辈出"
a_list = ['keyou',18,a_var,True,None,['python','java','php']]
print('列表:\n',a_list)

#1 修改列表
a_list[1] =17
print(a_list)

#2 插入元素
a_list.append("keyou") #将元素整体插入进去
print(a_list)

a_list.extend("keyou") #将元素分开单独插入进去
print(a_list)

a_list.insert(3,"lemon")
print(a_list)

#3 删除元素
del a_list[1]  #根据索引删除值
print(a_list)

a_list.remove(18) #删除第一个出现的元素
print(a_list)

print(a_list.pop(1)) #删除以后会返回删除值

#4 列表排序(Ture和Flase决定是正序还是倒序)
a_list.sort(reverse=True)