import requests
from tqdm import tqdm

# api key
token = "1d4c8c50906cadee87458516425a3248"
# token = "kfc50905090kfckfc509050905090kfc"

def wellDone(outpath, model_any_id,model_name):
    """
    传入保存路径，模型或者模型版本id，模型名字进行下载
    :param outpath:
    :param model_any_id:
    :param model_name:
    :return:
    """

    # https://civitai.com/api/download/models/634767
    model_id = model_any_id

    in_url = f"https://civitai.com/api/download/models/{model_id}?token={token}"

    headerList = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "referer": "https://civitai.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Content-Type":"application/json",
    }

    def download_with_progress(url, headers=None, **kwargs):
        response = requests.get(url, headers=headers, verify=False, stream=True, **kwargs)
        total_size = int(response.headers.get('content-length', 0))

        with tqdm(total=total_size, unit='iB', unit_scale=True, desc=f'\nDownloading --{model_name}') as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                pbar.update(len(chunk))
                yield chunk

    # Download the model using tqdm
    with open(f'{outpath}/{model_name}.safetensor', 'wb') as f:
        for chunk in download_with_progress(in_url, headers=headerList):
            f.write(chunk)