def print_line(char, times):
    """"""
    print(char * times)


def print_lines(num, char, times):
    """打印多行分隔线

    :param num: 分割线行数
    :param char: 分隔字符
    :param times: 重复次数
    """
    i = 0
    while i < num:
        print_line(char, times)
        i += 1


print_lines(5,"+", 50)
