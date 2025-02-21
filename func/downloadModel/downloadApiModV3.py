import urllib.request
import os
from urllib.parse import urlparse, parse_qs, unquote
import time

# api key ------ example:"kfc50905090kfckfc509050905090kfc"
token = "1d4c8c50906cadee87458516425a3248"
# 官方：创作者可以要求人们登录后才能下载他们的资源。这是我们提供的选项，但不是我们的要求——这完全取决于资源所有者。

def wellDone(outpath, model_any_id, model_name):
    model_id = model_any_id
    in_url = f"https://civitai.com/api/download/models/{model_id}?type=Model&format=SafeTensor&token={token}"

    headers = {
                # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Authorization": f"Bearer {token}",
        # "accept-encoding":"gzip, deflate, br, zstd",
        "referer": "https://civitai.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        # "connection":"keep-alive"
    }

    class NoRedirection(urllib.request.HTTPErrorProcessor):
        def http_response(self, request, response):
            return response

        https_response = http_response

    request = urllib.request.Request(in_url, headers=headers)
    opener = urllib.request.build_opener(NoRedirection)

    response = opener.open(request)

    if response.status in [301, 302, 303, 307, 308]:
        redirect_url = response.getheader('Location')

        parsed_url = urlparse(redirect_url)
        query_params = parse_qs(parsed_url.query)
        content_disposition = query_params.get('response-content-disposition', [None])[0]

        if content_disposition:
            filename = unquote(content_disposition.split('filename=')[1].strip('"'))
        else:
            raise Exception('Unable to determine filename')

        response = urllib.request.urlopen(redirect_url)
    elif response.status == 404:
        raise Exception('File not found')
    else:
        raise Exception('No redirect found, something went wrong')

    total_size = response.getheader('Content-Length')
    if total_size is not None:
        total_size = int(total_size)

    output_file = os.path.join(outpath, filename)
    chunk_size = 8192
    progress = 0

    with open(output_file, 'wb') as f:
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            progress += chunk_size
            if progress % total_size <= chunk_size:
                print(f"\rDownloading... ({progress / total_size * 100:.2f}%)", end='')
            else:
                print(f"\rDownloading... ({(progress / total_size * 100):.2f}%)", end='')

    print(f"\nDownloading finished.")

# wellDone(outpath='.',model_any_id=input('id:'),model_name='test')