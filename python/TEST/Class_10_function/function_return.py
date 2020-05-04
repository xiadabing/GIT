# one_list = [13,21,3,76,54,12,44,80,92]
# i = 0
# sum=0
# while i<=len(one_list)-1:
#     sum += one_list[i]
#     i = i+1
# print(sum)


#用while循环实现2-3+4-5+6……+100的和？
# i = 2
# sum = 0
# while i<=100:
#     if i%2 == 0:
#         sum = sum+i
#     else:
#         sum = sum -i
#
#     i += 1
# print(f'{sum}')


# score = float(input("请输入你的分数:"))
# if score>=90:
#     print('A')
# elif score>= 80:
#     print('B')
# elif score>= 70:
#     print('c')
# elif score>= 60:
#     print('D')
# else:
#     print('E')

# money = float(input('请输入你的金额：'))
# total_money = 2 * money
# year = 1
# while year<=10000:
#     money = money + money * 0.0352
#     if money>=total_money:
#         break
#     year = year+1
#     print(money)
# print(year)

# money = float(input('请输入你的金额：'))
# total_money = 2 * money
# year = 1
# while money<=total_money:
#     money =  money * 1.0352
#     year = year+1
# print(year)

# value = int(input("请输入你的数字："))
# reslut = 1
# i = 1
# while i<=value:
#     reslut = reslut * i
#     i = i+1
# print(reslut)

# value = int(input('请输入你的数字：'))
# i = 1
# result = 1
# for i in range(1,value+1):
#     result = result * i
# print(result)

# data = int(input('输入日期:'))
# data_list = ["周一" ,'周二','周三',' 周四','周五' ,'周末']
# if 0<data<=7:
#     if data in range(1,6):
#         print(f'当前日期为：{data_list[data-1]}')
#     else:
#         print(f'当前日期为{data_list[5]}')
# else:
#     print('输入有误，请重新输入')


def login(username,password):
    """name"""
    if username == 'lemon' and password == 'best':
        print('登陆成功')
    else:
        print('输入失败')

login('lemon','best')


































