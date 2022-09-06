import requests

baseUrl='https://www.pearvideo.com/video_1725262'

contId=baseUrl.split('_')[-1]

url='https://www.pearvideo.com/videoStatus.jsp?contId=1725262&mrd=0.22497807787747015'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    'Referer': 'https://www.pearvideo.com/video_1725262'
}

response=requests.get(url,headers=headers)

text=response.json()

# print(text)

vedioUrl=text['videoInfo']['videos']['srcUrl']
systemTime=text['systemTime']

vedioUrl=vedioUrl.replace(systemTime,f'cont-{contId}')

with open('a.mp4','wb') as f:
    f.write(requests.get(vedioUrl).content)