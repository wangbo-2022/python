import jieba                                # 分词
from matplotlib import pyplot as plt        # 绘图，数据可视化
from wordcloud import WordCloud             # 词云
from PIL import Image                       # 图片处理
import numpy as np                          # 矩阵运算
import xlrd                                 # excel

wb = xlrd.open_workbook("./豆瓣电影Top250.xls")
wbsheet = wb.sheet_by_index(0)
col_data = wbsheet.col_values(6)

text = ""
for item in col_data[1:]:
    text = text + item


cut = jieba.cut(text)
string = " ".join(cut)

img = Image.open(r".\static\assets\img\tree.jpg")
img_arry = np.array(img)

wc = WordCloud(
    background_color='white',
    mask=img_arry,
    font_path="msyh.ttc"
)

wc.generate_from_text(string)

fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

# plt.show()
plt.savefig(r".\static\assets\img\word.jpg")







