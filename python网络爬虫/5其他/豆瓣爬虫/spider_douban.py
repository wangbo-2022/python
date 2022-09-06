# -*- coding = "utf-8" -*-
import re
import urllib.request
from bs4 import BeautifulSoup
import xlwt
import sqlite3

# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImage = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片片名
findName = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 相关内容
findBd = re.compile(r'<p class="">(.*?) </p>', re.S)



def askURL(url):

    headers = {
        "user-agent": "Mozilla/5.0( Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    return html


def getData(baseurl):

    data_list = []
    for i in range(0, 10):

        html = askURL(baseurl + str(i * 25))
        soup = BeautifulSoup(html, "html.parser")

        for item in soup.find_all("div", class_ = "item"):
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            image = re.findall(findImage, item)[0]
            data.append(image)

            name = re.findall(findName, item)
            if len(name) == 2:
                cname = name[0]
                data.append(cname)

                oname = name[1].replace("/", "")
                data.append(oname)
            else:
                data.append(name)

                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", "", bd)
            bd = re.sub("/", "", bd)
            data.append(bd.strip())

            data_list.append(data)

    return data_list


def save_data_to_excel(data, savePath):

    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet("电影Top250", cell_overwrite_ok=True)

    col = ("电影详情链接","电影图片链接","影片中文名","影片外文名","评分","评价数","概况","想关信息")
    for i in range(0, 8):
        worksheet.write(0, i, col[i])

    for i in range(0, 250):
        for j in range(0, 8):
            worksheet.write(i+1, j, data[i][j])
    workbook.save(savePath)


def save_data_to_sql(data, dbpath):

    db_init(dbpath)

    db_insert(data, dbpath)


def db_init(dbpath):

    conn = sqlite3.connect(dbpath)

    c = conn.cursor()

    sql = '''
        create table top250
        (id integer primary key autoincrement,
        link_info text,
        link_pic text,
        cname varchar,
        oname varchar,
        score numeric,
        rated numeric,
        inq text,
        info text)
    '''

    c.execute(sql)

    conn.commit()

    conn.close()


def db_insert(data_list, dbpath):

    conn = sqlite3.connect(dbpath)

    cursor = conn.cursor()

    for data in data_list:
        print(data)
        # for index in range(len(data)):
            # if index == 4 and index == 5:
            #     continue
            # data[index] = '"'+data[index]+'"'
        sql = '''
                insert into top250(
                link_info,link_pic,cname,oname,score,rated,inq,info)
                values (%s)''' % data
        print(sql)
        cursor.execute(sql)

        conn.commit()

    conn.close()


def main():

    baseurl = "https://movie.douban.com/top250?start="

    savepath = "豆瓣电影Top250.xls"

    dbpath = "movie.db"

    data = getData(baseurl)

    # save_data_to_excel(data, savepath)

    save_data_to_sql(data, dbpath)


if __name__ == '__main__':

    main()