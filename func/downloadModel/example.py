

import requests

# https://civitai.com/api/download/models/634767
model_id = "634767"

in_url = f"https://civitai.com/api/download/models/{model_id}?token=1d4c8c50906cadee87458516425a3248"

headerList = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "referer": "https://civitai.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Content-Type":"application/json",
}

params = {"endpoint_url": in_url,
}

response = requests.get(
    in_url,
    headers=headerList,
    verify=False,

)
