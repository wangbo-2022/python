# 记录所有名片的列表
card_list = []


def show_menu():
    """
    显示菜单
    """
    print("*" * 50)
    print("欢迎使用名片管理系统 v1.0\n")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片\n")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """
    新增名片
    :return:
    """
    card_dict = {"姓名": "",
                 "电话": "",
                 "QQ": "",
                 "邮箱": ""}

    print("-" * 50)

    print("功能：新建名片")

    card_dict["姓名"] = input("请输入姓名：")
    card_dict["电话"] = input("请输入电话号码：")
    card_dict["QQ"] = input("请输入QQ号码：")
    card_dict["邮箱"] = input("请输入邮箱：")

    card_list.append(card_dict)

    print("%s的名片添加成功" % card_dict["姓名"])
    print("-" * 50)


def show_all():
    """
    显示全部名片信息
    """
    print("*" * 50)
    print("功能：查询全部")

    # 判断是否有名片记录
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新建名片功能添加名片")
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)

    # 打印信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["姓名"],
                                            card_dict["电话"],
                                            card_dict["QQ"],
                                            card_dict["邮箱"]))

    print("*" * 50)


def search_card():
    """
    查询名片，并做出相应操作
    """

    print("-" * 50)
    print("功能：搜索名片")
    # 提示用户输入要搜索的姓名
    name_str = input("请输入要搜索的姓名：")
    # 遍历名片列表
    for card_dict in card_list:
        if card_dict["姓名"] == name_str:
            # 打印表头
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            # 打印信息
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["姓名"],
                                                card_dict["电话"],
                                                card_dict["QQ"],
                                                card_dict["邮箱"]))
            # 处理名片
            deal_card(card_dict)
            break
    else:
        print("没有找到%s的名片，请使用新建名片功能添加名片" % name_str)

    print("-" * 50)


def deal_card(find_dict):
    # 请用户输入想要进行的操作
    opera_str = input("请输入对名片的操作："
                      "【1】:修改 【2】:删除 【其他】:返回上级菜单")
    # 根据用户输入进行相应的操作
    if opera_str == "1":
        # 修改名片
        find_dict["姓名"] = input_card_info(find_dict["姓名"], "请输入姓名：")
        find_dict["电话"] = input_card_info(find_dict["电话"],"请输入电话号码：")
        find_dict["QQ"] = input_card_info(find_dict["QQ"],"请输入QQ号码：")
        find_dict["邮箱"] = input_card_info(find_dict["邮箱"], "请输入邮箱：")
        print("修改名片成功！")
    elif opera_str == "2":
        # 删除名片
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    # 提示用户输入内容
    result_str = input(tip_message)
    # 如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value


