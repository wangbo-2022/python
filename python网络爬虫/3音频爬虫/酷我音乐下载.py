import requests
import prettytable as pt

tb=pt.PrettyTable()
tb.fieldnames=['序号','歌名','歌手','专辑']
count=0

url='https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%E6%9D%8E%E8%8D%A3%E6%B5%A9&pn=1&rn=30&httpsStatus=1&reqId=884b4130-279f-11ed-bcd3-957d1de18afc'

headers={
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1661780107; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1661780107; _ga=GA1.2.2092754803.1661780107; _gid=GA1.2.558845926.1661780107; _gat=1; kw_token=57D975Q5G4A',
    'csrf': '57D975Q5G4A',
    'Host': 'www.kuwo.cn',
    'Referer': 'https://www.kuwo.cn/search/list?key=%E6%9D%8E%E8%8D%A3%E6%B5%A9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
response=requests.get(url,headers=headers)
json_data=response.json()

data_list=json_data['data']['list']
down_list=[]
for data in data_list:
    artist=data['artist']
    name=data['name']
    album=data['album']
    rid=data['rid']
    tb.add_row([count,name,artist,album])
    down_list.append([rid,name,artist])
    count +=1

print(tb)

while True:
    input_index=eval(input('请输入下载的歌曲序列号(-1退出)'))
    if input_index==-1:
        break
    down_info=down_list[input_index]
    rid=down_info[0]
    music_url=f'https://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music&httpsStatus=1&reqId=196f23e1-27a3-11ed-9a3a-1f092d1464a4'
    music_json=requests.get(music_url).json()['data']['url']
    music_data=requests.get(music_json).content
    
    with open(f'C:\\Users\\wangbo\\Desktop\\study\\python\\python网络爬虫\\2音频爬虫\\music\\{down_info[1]}-{down_info[2]}.mp3',mode='wb') as f:
        f.write(music_data)
    print(f'爬取成功：{down_info[1]}-{down_info[2]}')