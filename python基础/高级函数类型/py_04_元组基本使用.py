info_tuple = ("zhangsan", 18, 1.75)

# 取值
print(info_tuple[1])
# 取索引
print(info_tuple.index("zhangsan"))
# 计数
print(info_tuple.count("zhangsan"))
print(info_tuple)

# 循环遍历
for info in info_tuple:
    print(info)

print("%s 年龄是%d 身高是%.2f" % info_tuple)

info_str = "%s 年龄是%d 身高是%.2f" % info_tuple

print(info_str)
