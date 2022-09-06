def input_password():

    # 1.请用户输入密码
    pwd = input("请输入密码：")

    # 2.如果密码长度>=8，输出密码
    if len(pwd) >= 8:
        return pwd

    # 3.如果密码长度<8，抛出异常

    # 1> 创建一个异常类
    ex = Exception("密码长度不够")

    # 2> 抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
