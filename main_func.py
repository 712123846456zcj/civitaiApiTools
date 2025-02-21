
from func.startGET import injson
from func.textRe import text_clean



import requests
import json
import os,sys
import urllib3

from func.urlTools import urlINFO

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

input_your_modeURL = input("请输入模型的url：")
input_your_modelID = urlINFO(input_your_modeURL)[0]
input_your_modelVersionID = urlINFO(input_your_modeURL)[1]

in_url  = f"https://civitai.com/api/v1/models/{input_your_modelID}"

# 你的cookie和token
cookie='ck'#,不是必须的
headerList = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Content-Type":"application/json",
}

params = {"endpoint_url": in_url,
          "limit": 100, #限制-每页返回的结果数。可以是 0 到 200 之间的数字。默认情况下，每页将返回 100 个结果。
}

response = requests.get(
    in_url,
    headers=headerList,
    verify=False,
    params=params

)

if response.status_code == 200:

    # print(response.content.decode('UTF-8'))  # 打印文本中没有乱码

    data = response.json()
    datas = json.dumps(data,indent=4,ensure_ascii=False)
    datas = json.loads(datas)
    injson(injson_info=datas,idid=input_your_modelVersionID)


