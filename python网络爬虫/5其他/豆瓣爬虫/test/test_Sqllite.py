import sqlite3

# # 建立连接
# conn = sqlite3.connect("test.db")
# # 获取游标
# c = conn.cursor()
#
# sql = '''
#     create table company
#     (id int primary key not null,
#     name text not null,
#     age int not null,
#     address char(50),
#     salary real);
#
# '''
# # 执行sql语句
# c.execute(sql)
# # 提交数据库操作
# conn.commit()
# # 关闭数据库连接
# conn.close()

# # 建立连接
# conn = sqlite3.connect("test.db")
# # 获取游标
# c = conn.cursor()
#
# sql1 = '''
#     insert into company(id,name,age,address,salary)
#     values (1, "张三", 31, "成都", 8000)
#
# '''
# sql2 = '''
#     insert into company(id,name,age,address,salary)
#     values (2, "李四", 32, "成都", 10000)
#
# '''
# # 执行sql语句
# c.execute(sql1)
# c.execute(sql2)
# # 提交数据库操作
# conn.commit()
# # 关闭数据库连接
# conn.close()

# 建立连接
conn = sqlite3.connect("test.db")
# 获取游标
c = conn.cursor()

sql = "select id,name,address,salary from company"

# 执行sql语句
cursor = c.execute(sql)

for row in cursor:
    print("id = %d" % row[0])
    print("name = %s" % row[1])
    print("address = %s" % row[2])
    print("salary = %d" % row[3])

# 关闭数据库连接
conn.close()
