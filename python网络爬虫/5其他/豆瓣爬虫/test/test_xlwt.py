import xlwt

# 创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
# 创建工作表
worksheet = workbook.add_sheet("sheet1")
# 写入数据
for i in range(1, 10):
    for j in range(1, i + 1):
        worksheet.write(i-1, j-1, ("%d X %d = %d" % (i, j, (i * j))))
# 保存数据表
workbook.save("student.xls")
