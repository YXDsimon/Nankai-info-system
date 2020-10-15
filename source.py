def CountCN(str):
    count = 0
    for ch in str:
        if '\u4e00' <= ch <= '\u9fff':
            count += 1
    return count

def printMenu():
    print("##############################################################################")
    print('                     南开大学软件学院通讯录管理系统v0.01a')
    print('')
    print('                             添加数据请按[a]')
    print('                             查看数据请按[s]')
    print('                             删除数据请按[d]')
    print('                             修改数据请按[m]')
    print('                                                               返回菜单请按[q]')
    print("##############################################################################")

def printL():
    "打印通讯录的内容"
    print("{:<7}{:\u3000<5}{:<17}{:<15}{:<18}".format(
        "序号", "姓名", "QQ", "电话", "邮箱"))
    for s in l:
        if '\u4e00' <= s[1][0] <= '\u9fff':
            print("{:<9}{:\u3000<5}{:<17}{:<17}{:<20}".format(s[0], s[1], s[2], s[3], s[4]))
        else:
            print("{:<9}{:<10}{:<17}{:<17}{:<20}".format(s[0], s[1], s[2], s[3], s[4]
                                                          ))


l = []  # 用来存储信息的list
printMenu()
while(1):
    order = input('请输入相应的命令(返回菜单请按q)：')
    if order == 'a':
        name = input('请输入您的姓名：')
        qq = input('请输入您的qq号码：')
        tel = input('请输入您的电话号码：')
        email = input('请输入您的邮箱：')
        l.append([len(l)+1, name, qq, tel, email])
        print('添加成功！')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~修改/添加数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        printL()

    elif order == 's':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~通讯录数据列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        printL()

    elif order == 'm':
        boolname = 0
        boolqq = 0
        booltel = 0
        boolemail = 0
        mNum = input('请输入您想要修改的学生的序号：')
        Newname = input("请输入修改后的姓名：（不修改可输入空格）")
        if not Newname.isspace():
            boolname = 1
        Newqq = input("请输入修改后的QQ：（不修改可输入空格）")
        if not Newqq.isspace():
            boolqq = 1
        Newtel = input("请输入修改后的电话：（不修改可输入空格）")
        if not Newtel.isspace():
            booltel = 1
        Newemail = input("请输入修改后的邮箱：（不修改可输入空格）")
        if not Newemail.isspace():
            boolemail = 1
        boolexists = 0
        for stu in l:
            if stu[0] == int(mNum):
                boolexists = 1
                if boolname == 1:
                    stu[1] = Newname
                if boolqq == 1:
                    stu[2] = Newqq
                if booltel == 1:
                    stu[3] = Newtel
                if boolemail == 1:
                    stu[4] = Newemail
                break
        if boolexists == 0:
            print("序号不存在!")
        else:
            print('修改成功！')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~修改/添加数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        printL()
    elif order == 'd':
        dNum = input("请输出想要删除的学生序号：")
        boolexists = 0
        for i in range(len(l)):
            if l[i][0] == int(dNum):
                boolexists = 1
                l.pop(i)
                for j in range(i, len(l)):
                    l[j][0] -= 1
                break
        if boolexists == 0:
            print("序号不存在！")
        else:
            print('删除成功！')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~修改/添加数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        printL()
    elif order == 'q':
        printMenu()
    else:
        print("指令输入错误！")
