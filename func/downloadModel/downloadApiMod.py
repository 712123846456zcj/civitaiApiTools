import time

import requests
from tqdm import tqdm

# api key ------ example:"kfc50905090kfckfc509050905090kfc"
token = ""
# 官方：创作者可以要求人们登录后才能下载他们的资源。这是我们提供的选项，但不是我们的要求——这完全取决于资源所有者。
# 此脚本我不了解下载的数据有问题，所以改用v2版本

def wellDone(outpath, model_any_id,model_name):
    """
    Download a model from Civitai.
    :param outpath:
    :param model_any_id:
    :param model_name:
    :return:
    """

    # https://civitai.com/api/download/models/634767
    model_id = model_any_id

    in_url = f"https://civitai.com/api/download/models/{model_id}?type=Model&format=SafeTensor&token={token}"

    headerList = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Authorization": f"Bearer {token}",
        # "accept-encoding":"gzip, deflate, br, zstd",
        "referer": "https://civitai.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        # "connection":"keep-alive"
    }

    if token:
        max_retries = 3
        for retry in range(max_retries):
            try:
                response = requests.get(in_url, headers=headerList, verify=False, stream=True)
                total_size = int(response.headers.get('content-length', 0))

                with tqdm(total=total_size, unit='iB', unit_scale=True, desc=f'\nDownloading --{model_name}') as pbar:
                    with open(f'{outpath}/{model_name}.safetensor', 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            pbar.update(len(chunk))
                            f.write(chunk)
                break  # Exit the loop if download is successful
            except requests.exceptions.RequestException as e:
                print(f"[-] Download error, retrying... ({retry+1}/{max_retries})")
                time.sleep(2) # Wait for a couple of seconds before retrying

        else:
            print(f"[-] Failed to download after {max_retries} attempts.")
    else:
        print('[-]empty token....over')


# wellDone(outpath='.',model_any_id=input('id:'),model_name='test')