import os
from concurrent.futures import ThreadPoolExecutor

import requests


def imd(indata, i, out_path):
    """
    下载图片
    :param indata:
    :return:
    """

    urls = []
    allinfo = []

    for image in indata['modelVersions'][i]['images']:
        url = image['url']
        if r'/width=450' in url:
            url = url.replace(r'/width=450', r'/original=true,quality=90')
        urls.append(url)
    # urls = urls[0:21]
    print(f'图片数量：{len(urls)}',urls)

    def download_image(image_url):
        response = requests.get(image_url)

        if response.status_code == 200:
            image_data = response.content
            # md5_hash = hashlib.md5(image_data).hexdigest()
            # file_path = f"{images_download_folder}/{md5_hash[0]}/{md5_hash[1]}/{md5_hash[2]}/{md5_hash[3]}/{md5_hash}.jpeg"
            fnames = image_url.split('/')[-1]
            file_path = f"{out_path}/{fnames}.png"
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 创建多级目录
            if os.path.exists(file_path):
                print(f"图片已存在：{file_path}")
                pass
            else:
                with open(file_path, "wb") as file:
                    file.write(image_data)
                    print(f"图片已成功下载并存储：{file_path}")
        else:
            print("无法下载图片。")

    def process_txt_file(data_in):

        # print(file_path,data_in)
        # with open(file_path, 'r', encoding='utf-8') as file:
            # data = file.read()
            # data = json.loads(data)
            # urls = [result.get('url') for result in data.get('results', [])]
            # image_urls = re.findall(r'image_url:\s(.*?)\n', data)
            # print(image_urls)
            # print(type(data))

            # print(image_urls)
        with ThreadPoolExecutor(max_workers=10) as executor:  # 可以根据需求调整线程数
            executor.map(download_image, data_in)

    process_txt_file(data_in=urls)