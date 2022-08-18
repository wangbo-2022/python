import json

json_str = '''[{"provinceName":"美国","currentConfirmedCount":2119195,"confirmedCount":90367064},
               {"provinceName":"英国","currentConfirmedCount":16624988,"confirmedCount":23298969}]'''

# 把json字符串转为python数据
rs = json.loads(json_str)
# print(rs)
# print(type(rs))
# print(type(rs[0]))


# 把json文件转为python数据
with open('data/test.json') as fp:
    python_list = json.load(fp)
    # print(python_list)
    # print(type(python_list))
    # print(type(python_list[0]))
# python转为json字符串
json_str1 = json.dumps(rs, ensure_ascii=False)
print(json_str1)

# python转为json文件
with open('data/test1.json', 'w') as fp:
    json.dump(rs, fp, ensure_ascii=False)

