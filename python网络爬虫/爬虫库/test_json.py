import json

person={
    'name':'zhangsan',
    'age':18,
    'gender':True,
    'tel':[123456,'654321']
}

print(type(person))

# 1.python字典转换成json字符串
json_str=json.dumps(person,indent=4)
print(type(json_str))

# 2.python字典转换成json字符串并存储到文件
json.dump(person,open('data.json','w'),indent=4)

# 3.json字符串转为python字典
py_dict=json.loads(json_str)
print(type(py_dict))

# 4.json文件转为python字典
py_dict1=json.load(open('data.json','r'))
print(py_dict1)













