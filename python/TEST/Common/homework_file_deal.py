#
# def read_file_line(file_name,mode= 'r',encoding='utf-8'):
#     """
#
#     :param file_name:
#     :param mode:
#     :param encoding:
#     :return:
#     """
#     src_file = open(file_name,mode=mode,encoding=encoding)
#     data_list = src_file.readlines()
#     file_len = len(data_list)-1
#     for key,value in enumerate(data_list):
#         if key != (file_len-1):
#             data_list[key] = value[:-1]
#     src_file.close()
#     return data_list
#
#
# def handle_data(one_list):
#     """
#     将字符串转换成列表的过程
#     :param one_list:
#     :return:
#     """
#     full_result_list = []
#     tmp_result_list = []  #用于存放临时结果
#     for item in one_list:
#         one_tmp = item.split('@')
#         for new_item in one_tmp:
#             tmp_result_list.append(new_item.split(':',1))
#         full_result_list.append(dict(tmp_result_list))
#     #print(full_result_list)
#     return full_result_list
#
# def main():
#     """
#     启动函数
#     :return:
#     """
#     completetd_data = handle_data(read_file_line('text.txt'))
#     print('数据的最终处理结果为:\n{}'.format(completetd_data))
#
# if __name__ == '__main__':
#     main()


src_file = open('text.txt',mode='r')
key_list = []
value_list = []
tmp_list = []
actual_list = []
data_list = src_file.readlines() #读取所有行的值，返回列表
print(data_list)
for tmp_data_1 in data_list:                  #将返回的列表值遍历给a
    new_list = tmp_data_1.split('@')      #通过@分隔符取出3组对应的数据列表
    #print(new_list)
    for tmp_data_2 in new_list:            #遍历3组数据列表赋值给b
        item_list = tmp_data_2.split(':',1)     #用冒号分割关键字和值，1指分割字符串中遇到的第一个冒号
        key_list.append(item_list[0])
        value_list.append(item_list[1].rstrip())
    one_dict = zip(key_list,value_list)
    print(one_dict)



src_file.close()






