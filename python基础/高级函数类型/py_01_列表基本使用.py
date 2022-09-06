name_list = ["zhangsan", "lisi", "wangwu"]

# 查找索引
print(name_list.index("lisi"))

# 修改
name_list[0] = "张三"

# 增加
name_list.append("小二")
name_list.insert(1,"yyy")

temp_list = ["1", "2", "3"]
name_list.extend(temp_list)

# 删除
name_list.remove("lisi")
name_list.pop(0)
name_list.clear()

print(name_list)

name_list = ["zhangsan","zhangsan", "lisi", "wangwu", "zhangsan"]

del name_list[1]

print(name_list)

print(len(name_list))

print(name_list.count("zhangsan"))

name_list.remove("zhangsan")

print(name_list)

