str1 = "hello python"

# for char in str1:
#     print(char)

print(str1[5])


str2 = "hello hello"

# 字符串长度
print(len(str2))
# 子字符串出现次数
print(str2.count("llo"))
print(str2.count("abc"))
# 子字符串索引
print(str2.index("llo"))
# print(str2.index("abc"))

# 判断空白
str_3 = "    \t\n\r"
print(str_3.isspace())

# 判断数字
# 1>不能判断小数
str_num = "1.1"
# 2>unicode 字符串
str_num = "\u00b2"
# 3>中文数字
str_num = "二零二二"

print(str_num)
print(str_num.isdecimal())
print(str_num.isdigit())
print(str_num.isnumeric())
