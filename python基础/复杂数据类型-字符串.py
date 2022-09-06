str1 = "hello python!"
str2 = "hello"
str3 = "12345"
str4 = " "
str5 = "hello123"
str6 = ""
str7 = "Hello Python!"
str8 = "HELLO"

# # 索引
# print(str1[4])
#
# # 长度
# print(len(str1))
#
# # 判断类型
# print(str1.isspace())
# print(str4.isspace())
#
# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())
# print(str4.isalnum())
#
# print(str1.isalpha())
# print(str2.isalpha())
# print(str3.isalpha())
# print(str4.isalpha())
# print(str5.isalpha())
# print(str6.isalpha())
#
# print(str1.istitle())
# print(str7.istitle())
#
# print(str1.islower())
# print(str7.islower())
# print(str8.islower())
#
# print(str1.isupper())
# print(str7.isupper())
# print(str8.isupper())
#
# print("\u00b2".isnumeric())
# print("\u00b2".isdigit())
# print("\u00b2".isdecimal())
# print("一".isnumeric())
# print("一".isdigit())
# print("一".isdecimal())
#
# # 大小写转换
# print(str1.capitalize())
# print(str8.capitalize())
#
# print(str1.title())
# print(str8.title())
#
# print(str1.upper())
# print(str5.upper())
# print(str7.upper())
#
# print(str7.lower())
# print(str8.lower())
#
# print(str5.swapcase())
# print(str7.swapcase())
#
# # 文本对齐
# print(str1.ljust(8))
# print(str1.rjust(20))
# print(str1.center(20))
#
# # 去除空白符
# print(" hello python ".lstrip())
# print(" hello python ".rstrip())
# print(" hello python ".strip())

# # 拆分和连接
# print("abcdecdefg".partition("cde"))
# print("abcdecdefg".rpartition("cde"))
# print("abcdecdefg".split("cde"))
# print("abcdecdefg".split("cde",1))
# print("ab cde\ncde\rfg".split())
# print("ab\r\ncde\ncde\rfg".splitlines())
# print("a".join(["hello","python","2"]))


# # 查找和替换
# print("abced".startswith("a"))
# print("abced".endswith("d"))
# print("abcde".count("b"))

# print("abcde".index("b"))
# print("abcde".rindex("b"))
#
# print("abcde".find("d"))
# print("abcde".rfind("d"))
#
# print("abcde".replace("c","f"))

# # 切片
# print("abcdefg"[1:5:2])
# print("abcdefg"[1:5])
# print("abcdefg"[:5:2])
# print("abcdefg"[1::2])
# print("abcdefg"[1:-1:2])
# print("abcdefg"[1:5:])
# print("abcdefg"[::-1])

# 遍历
for item in "abcdefg":
    print(item)