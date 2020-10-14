from prettytable import PrettyTable


# def printL():
#     "打印通讯录的内容"
#     print('{:<3}{:<13}{:<15}{:<13}{:<18}'.format('序号', '姓名', 'QQ', '电话', '邮箱'))
#     for i in range(len(l)):
#         print('{:<5}{:<15}{:<15}{:<15}{:<20}'.format(
#             i+1, l[i][0], l[i][1], l[i][2], l[i][3]))


print("##############################################################################")
print('                     南开大学软件学院通讯录管理系统v0.01a')
print('')
print('                             添加数据请按[a]')
print('                             查看数据请按[s]')
print('                             删除数据请按[d]')
print('                             修改数据请按[m]')
print(
    '                                                               返回菜单请按[q]')
print("##############################################################################")
table = PrettyTable(['姓名', 'QQ', '电话', '邮箱'])  # 存储数据的table
table.align="l"
order = input('请输入相应的命令(返回菜单请按q)：')
if order == 'a':
    name = input('请输入您的姓名：')
    qq = input('请输入您的qq号码：')
    tel = input('请输入您的电话号码：')
    email = input('请输入您的邮箱：')
    table.add_row([name, qq, tel, email])
    print('添加成功！')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~修改/添加数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(table)
print('[{name:<{len}}x'.format(name=name+']',len=22-len(name.encode('GBK'))+len(name)))