from func.textRe import text_clean


import requests
import json
import os,sys

# 655996
input_your_modelID = 469314 # input("请输入链接的原始模型id：")
# input_your_modelVersionID = input("请输入链接的版本模型id：")

in_url  = f"https://civitai.com/api/v1/models/{input_your_modelID}"
def outuid(qs):
    return qs

# 你的cookie和token
cookie = "_sharedID=631d1dda-c949-4f9c-bde0-5cbed7845b0c; _sharedID_cst=TyylLI8srA%3D%3D; _lr_env_src_ats=false; cto_bundle=BMqXfF92TUI3RFFmYkJ1VWRGJTJGY3dyV2xPamhYMjk4a0FpQ0cyZVJ2VDJlOWRvVzdkJTJCczRqdmVvZ0FTUGYzVUxxZVlmSVZqUlIxZ2UlMkI1MVczS0xsaXl0Yk0zMGpBMzJJOHRVcTV2YmhpbjVkVVJnRTFtOXpPOUh1a2taMTBoV2hTQkFOTTdvcHRSTW5PQlI2ajlYYVYlMkJSVCUyRmlnJTNEJTNE; mantine-color-scheme=light; __Secure-next-auth.callback-url=https%3A%2F%2Fcivitai.com; __Host-next-auth.csrf-token=e3df8c20175824afc0f7c0112673316114b4a046647e6bfa4495a2479c808ba0%7Cdb5f2271c6cb7cbfb74809af3787c6ae0567fa4f6b7f40521343c3345f3cc6ed; _sharedID_last=Wed%2C%2019%20Feb%202025%2003%3A11%3A51%20GMT; __Secure-civitai-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..CWJJIkewWnx3ZIUA.Wnll1fCCFBhogl_FqowA6WFtNzyOppA0Lg5cCE8JBPDjUS9y3JFbkUKUo4RbApnlfEfW5yoZaKPsRYCb5FTHsFuQ_O925yEid2o3fc0rW6FGq49yyDbT_syRtbQ-4uahWVAiX4XdKgmSI_vX4k9Wqv-qWro12o9ZWVTXq9CWcACaL27Ngu-fbFjDLWy0SRt77M_U1BVGd4W5Oi10eRHbOjGXI3Sksl42qPvLnlyy07i17K5mZ70NzPcRxxOG8yMvZ71FmBsohoecZBv2wXxNXABNk3U2VDC3NgApY5RsnCac9Jnn5NshOUA5fWn_uTo1DFb74bTXHoWVeeciGscNMlHgHeMhN26ibKJQ2K1XXDwN16IB0XbKr7xNmoZb9eB_-ImkISYxoeNn6XzOAphNiqOvnb5lokwYY7UmtUxCuHJNHRq4jdxRDJHlwuaeEikCoOSuTbfUSZDXRbOLUKYL1CXpFx7iyy8rWPH2PabbDeDCEL-8yXv2dawrKx2CfYMETIWO8djN3lAAoeRUjp0hdjAYbU-dkD99LLVXgJW05ut0ueQPAOHfI9dveRSdx3ViMZYag_Q8OUecRq8JKpjzJDmQBMFZIqcBmsUPGqb0LkqZGpYcEdZGsblSmt4pmVDGXZCs-hxLVus68b4H_a_1ofQPgn5EqcgIoZhCK3a2EZCJYV-0lHPZLHHX4tDpqwrr1idGNGeWE19RgfE1e4v1BY7DbiZSNJRmDeduixjjOSv14r4-IC9TDlsoODWnC0fJfYJqMyoth-IpCtHbIftc99DDGBHHF22YG3YD8jRET3s0x9sYJoXBBpPa2MWJdf985Pgo3prVSMZzDWER1exGW2uBsTiwbNMs8rCrWTavJ1ddJos2s9n1eQMg1peiJksIqiW2M6kBjfilvc92Js7LzrS3APX3yEXAldU5Rak6E34shi6RdjsDDKkJGFNAjCSA8iu4T-0giX3l8cxAUYY26vSCl5dD2We0yXZkZeVRB7w9AMrEAmsomiky9qxv2HaUNMu4pi0ULxfraa_PLOyienWxxkKi_pdVZ3vnTGgC445SHwd_y4C3ooNm6Gg0J2KjoG_DTSO-0rCR-1X4QedTSGyIk9Zp4WnaYXZspOJhlj-KKbJXdeGBIAez0teI4k2o0V43IJpFvbRdpcaLmItnqc7pH0Dlgo1RpZN21OWj3-jWbTeMNimDKBndnu8QJwTVwW3XwNXTVoq-5F3TfXPQOYui_BR8w03B1giX8TxUquhR.ePrK7PC8e0kHYcG3fmoq-w"
headerList = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "referer": "https://civitai.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "cookie": cookie,
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
    print(datas)
