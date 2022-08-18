# 字典
num = {}
print(type(num))

# 集合
num = {1,2,3,4,5,4,3,2,1,0}
num1 = set([1,2,3,4,5,4,3,2,1])
print(type(num))
print(type(num1))
# 集合中的数是唯一的 且会自动排序
print(num)
print(num1)

# 集合不支持索引
# print(num[1])

# 利用集合去除列表中重复的数据
num1 = [1,2,3,4,5,4,3,2,1]
num1 = list(set(num1))
print(num1)

for each in num:
    print(each)

# 不可变集合
num2 = frozenset([1,2,3,4,5])
# num2.add(1)