import requests
import json

headers={
    'cookie': 'pgv_pvid=5558001456; pac_uid=0_dc52c63cab8ff; iip=0; fqm_pvqid=f5a3aae3-f522-4c0e-aa07-7b5eca39a789; ts_refer=cn.bing.com/; ts_uid=6134148400; RK=/8ltVIegRK; ptcz=2a7f5c8b9eebd238a4ed0bf8b0a901f5a04aeb671a579b6d24cb8ea38fabca89; euin=oK6kNK4FNKCsoc**; tmeLoginType=2; fqm_sessionid=f11c37e1-b7fd-4ebc-8ecc-69fb44a11197; pgv_info=ssid=s2488703400; _qpsvr_localtk=0.5830449071419888; login_type=1; psrf_qqaccess_token=B333112A24F04787CC8C4AE9EE7FFFD2; wxrefresh_token=; psrf_qqopenid=054EC5DA85D1B5D4EE738FE52EE82CA4; psrf_qqunionid=346F29A1532A374644BF48A6D24F9307; wxunionid=; psrf_qqrefresh_token=0F9423E627483211CC571FDDFD80C33B; psrf_musickey_createtime=1662127171; psrf_access_token_expiresAt=1669903171; qm_keyst=Q_H_L_5808aB0M2ihjlkQw_2PUKnzBC0f5mA0_khnlWxq8spNFfVAeZW6ZZtQ; qqmusic_key=Q_H_L_5808aB0M2ihjlkQw_2PUKnzBC0f5mA0_khnlWxq8spNFfVAeZW6ZZtQ; qm_keyst=Q_H_L_5808aB0M2ihjlkQw_2PUKnzBC0f5mA0_khnlWxq8spNFfVAeZW6ZZtQ; wxopenid=; uin=1159589662; ts_last=y.qq.com/n/ryqq/search',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

url='https://y.qq.com/n/ryqq/search?w=%E8%AE%B8%E5%B5%A9'

response=requests.get(url,headers=headers)


text=response.content.decode()

with open('3音频爬虫/qq音乐.html','w',encoding='utf-8') as f:
    f.write(text)