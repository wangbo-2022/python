import requests
import re

headers={
    "cookie": "_uuid=95C854107-A10A8-5693-C25E-D5CAA594649A53927infoc; b_nut=1657287055; buvid3=6DAB06B8-D524-DAA4-C92D-FE476E3BB28949933infoc; buvid4=C0CA2865-2A5D-6501-398A-5503E3B0909D49933-022070821-xgg7j7gVRYFUTla1YbPW8Q%3D%3D; fingerprint=de7a174875494e75683c5918487cf59e; sid=8i7vy346; buvid_fp_plain=undefined; DedeUserID=237024234; DedeUserID__ckMd5=a1b683afc21ee61f; SESSDATA=40bad200%2C1672839083%2C54c6e*71; bili_jct=6bcdddd68092acf223cbab10a14f5223; buvid_fp=cbc0cf3814b8109a60771a2117ba1261; hit-dyn-v2=1; blackside_state=0; CURRENT_BLACKGAP=0; rpdid=|(um~JuklYkm0J'uYl~k)~u)l; nostalgia_conf=-1; i-wanna-go-back=-1; b_ut=5; CURRENT_QUALITY=80; LIVE_BUVID=AUTO2016606507742724; PVID=1; bp_video_offset_237024234=700134829634617300; theme_style=light; bsource=search_bing; is-2022-channel=1; b_lsid=D856FE33_182F47DF8D6; innersign=1; CURRENT_FNVAL=4048",
    'referer': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }

def response(html_url):

    res=requests.get(html_url,headers=headers)
    res.encoding='utf-8'

    text = res.text

    title=re.findall('<h1 title="(.*?)" class="video-title tit">',text)[0]

    cid=re.findall('"cid":(.*?),"',text)[0]

    session=re.findall('"session":"(.*?)"',text)[0]

    return [title,cid,session]


def get_info(html_url):

    vedio_info=response(html_url)

    print(vedio_info)


get_info('https://www.bilibili.com/video/BV14V4y1H7PG')





