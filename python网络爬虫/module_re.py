import re

# 字符匹配
rs = re.findall("abc", "abc")
rs = re.findall("a.c", "a\nc")
rs = re.findall("a.c", "abc")
rs = re.findall("a\.c", "a.c")
rs = re.findall("a[bcd]e", "abcde")
rs = re.findall("a[bcd]e", "abe")

# 预定义字符集
rs = re.findall("\d", "123")
rs = re.findall("\w", "Aa_123%#")

# 数量词
rs = re.findall("a\d*", "a123")
rs = re.findall("a\d+", "a123")
rs = re.findall("a\d?", "a123")
rs = re.findall("a\d{2}", "a123")

rs = re.findall("\d{2}", "chuan13zhi24")

# flag作用
rs = re.findall("a.bc","a\nbc",re.DOTALL)
rs = re.findall("a.bc","a\nbc",re.S)

# 分组的使用
rs = re.findall("a.+bc","a\nbc",re.DOTALL)
rs = re.findall("a(.+)bc","a\nbc",re.DOTALL)

# r原串的使用
# 消除转义符带来的影响
rs = re.findall("a\\nbc", "a\\nbc")
rs = re.findall(r"a\\nbc", "a\\nbc")
# 解决不符合PEP8规范的问题
rs = re.findall("\d", "a123")
rs = re.findall(r"\d", "a123")

print(rs)