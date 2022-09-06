# str1 = "hello world"
#
# # 查找
# print(str1.index("llo"))
# print(str1.find("llo"))
# print(str1.find("abc"))
#
# # 替换
# # 不会改变原字符串
# print(str1.replace("world", "python"))
# print(str1)
#
# poem = ["\t\n登鹳雀楼",
#         "王之涣",
#         "白日依山尽",
#         "黄河入海流",
#         "欲穷千里目\t\n",
#         "更上一层楼"]
#
# for poem_str in poem:
#     # print("|%s|" % poem_str.center(10, "　"))
#     # print("|%s|" % poem_str.ljust(10, "　"))
#     # print("|%s|" % poem_str.rjust(10, "　"))
#     print("|%s|" % poem_str.strip().center(10, "　"))


poem_str ="登鹳雀楼\t王之涣\t白日依山尽\t\n黄河入海流\t\n欲穷千里目\t更上一层楼"

poem_list = poem_str.split()
print(poem_list)

poem_str1 = "  ".join(poem_list)
print(poem_str1)

