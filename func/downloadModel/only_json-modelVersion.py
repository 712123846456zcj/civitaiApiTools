from func.textRe import text_clean


import requests
import json
import os,sys

# 655996
# input_your_modelID = 469314 # input("请输入链接的原始模型id：")
input_your_modelVersionID = 634767 #input("请输入链接的版本模型id：")

in_url  = f"https://civitai.com/api/v1/model-versions/{input_your_modelVersionID}"


# 你的cookie和token
#cookie = ""


headerList = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "referer": "https://civitai.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    # "cookie": cookie,
    "Content-Type":"application/json",
}


params = {"endpoint_url": in_url,
}

response = requests.get(
    in_url,
    headers=headerList,
    verify=False,

)


if response.status_code == 200:

    # print(response.content.decode('UTF-8'))  # 打印文本中没有乱码

    data = response.json()
    datas = json.dumps(data,indent=4,ensure_ascii=False)
    datas = json.loads(datas)
    print(datas)
