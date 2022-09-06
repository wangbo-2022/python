xiaoming_dict = {"name": "小明",
                "age": 18,
                "gender": True,
                "weight": 75,
                "hight": 175}

# 取值
print(xiaoming_dict["name"])

# 增加
xiaoming_dict["工作"] = "学生"
# 修改
xiaoming_dict["工作"] = "白领"
# 删除
xiaoming_dict.pop("工作")

# 统计键值对数量
print(len(xiaoming_dict))

# 合并
temp_dict = {"work": "student",
             "age": 20}
xiaoming_dict.update(temp_dict)
# 清空
xiaoming_dict.clear()

print(xiaoming_dict)

info_dict = {"name": "xiaoming",
             "qq": "12345",
             "phone": 123}
# 循环遍历
for k in info_dict:
    print("%s - %s" % (k,info_dict[k]))
