import re

# # search方法
# # 创建模式对象
# pat = re.compile("AA")
# m = pat.search("AABCDAADEGADAA")
#
# # 没有模式对象
#
# m = re.search("AA", "AADGSRGZAAFHSFA")
# print(m)

# # findall 方法
# print(re.findall("[a-z]+", "agejgFGHOIJHUIujYyuKTuHUuty"))
# print(re.findall("[]A-Z]", "AhoHuJFGOhiOHOJIokj"))


# sub方法
print(re.sub("a", "A", "agjoiariuwhgahrt"))

# 字符串前面加r可以处理转义字符 \带来的问题
a = "\adfajf\'"
b = r"\adfajf\'"
print(a)
print(b)











