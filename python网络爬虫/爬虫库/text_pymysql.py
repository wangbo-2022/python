import pymysql

# 建立连接
conn=pymysql.connect(host='localhost',user='root',passwd='123456',database='mydb1')

# 获取游标
cursor=conn.cursor()

# 编写sql语句（修改）
sql='update user1 set name="李四" where id=2;'

sql1='insert into user1 values(%s,%s);'
add_data=[3,'赵六']

# 执行sql语句
row_count=cursor.execute(sql)
row_count=cursor.execute(sql1,add_data)

# 提交修改
conn.commit()

# 编写sql语句（查询）
sql2='select * from user1;'

# 执行sql语句
row_count=cursor.execute(sql2)

# 获取查询结果
result=cursor.fetchall()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

print(result)










