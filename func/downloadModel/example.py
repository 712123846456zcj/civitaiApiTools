import requests

# https://civitai.com/api/download/models/634767
model_id = "256157"

in_url = f"https://civitai.com/api/download/models/{model_id}?type=Model&format=SafeTensor&token=1d4c8c50906cadee87458516425a3248"

headerList = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "referer": f"https://civitai.com/models/{model_id}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",

}

session = requests.Session()
session.headers.update(headerList)

response = session.get(in_url, verify=False)

# 检查重定向的 URL
if response.status_code == 307:
    print(f"Received 307 Temporary Redirect. Redirecting to: {response.headers['Location']}")
else:
    # 下载模型
    response.raise_for_status()
    with open("downloaded_model.safetensor", "wb") as f:
        f.write(response.content)
    print("模型下载完成。")