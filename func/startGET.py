

import json
import os

from func.findVerID import findID, reID
from func.imageDownload import isDownload
from func.textRe import text_clean, extract_text_from_html
from func.writeOver import overINFO
from func.downloadModel.downloadApiMod import wellDone

isDownloadApi = True
all_info = ['暂无或暂未设置']

def injson(injson_info='', idid=''):
    print('-'*50)
    """

    传入api返回的json内容

    [info] ====== injson_info --> type list

    """
    # 按json从上到下顺序添加模型信息，类型str
    # 如果没有信息：all_info.append("模型简介：" + all_info[0])
    # 如果是在modelVersions里面的name，就是版本名，最外层的是原本的模型名
    # 如果是在modelVersions里面的description，那就是单个版本特有的About this version内容，最外层的是此模型主页的详细简介
    # 至于['modelVersions'][0]中的0或者1或者...，对应着模型版本的索引，0就是默认最新的模型id，也对应着一个版本id
    # xx如果输入的是默认id（非版本id）..xx，目前已改善，整合旧版本的id读写方法，进行筛选优化，原始id仅仅用于其他用途或者索取完整的简介信息
    # 优化：只需在模型页面当中找到版本id即可（原始id是唯一的，单个模型当中，每一个版本都对应着一个版本id
    # 原始id仅用于获取完整简介信息，版本id用于获取特定信息和图片，经过多个星期的观察发现两者必不可少）

    all_info.append("模型原始id：" + str(injson_info['id']))
    all_info.append("模型名字：" + str(injson_info['name']))
    all_info.append("模型简介：" + extract_text_from_html(injson_info['description']))
    all_info.append("模型种类：" + str(injson_info['type']))
    all_info.append("模型tags：" + str(injson_info['tags']))

    # 从这里开始就到version内部了，索引开始选取,findverid的索引从0开始

    all_info.append("模型版本id：" + str(findID(inverID=idid,injson=injson_info)[0]))
    all_info.append("模型版本号：" + str(findID(inverID=idid,injson=injson_info)[1]))
    all_info.append("模型算法：" + str(findID(inverID=idid,injson=injson_info)[2]))

    try:
        all_info.append("模型版本简介：" + extract_text_from_html(findID(inverID=idid,injson=injson_info)[3]))
    except:
        all_info.append("模型版本简介：无")

    try:
        all_info.append("模型触发词：" + str(findID(inverID=idid,injson=injson_info)[4]))
    except:
        all_info.append("模型触发词：无")

    s = injson_info['name'] + str(findID(inverID=idid,injson=injson_info)[1])
    out_name_paths = text_clean(cleaned_filename=s)
    os.makedirs(out_name_paths, exist_ok=True)

    try:
        reID(inverID2=idid,injson2=injson_info,inpath=out_name_paths)
    except:
        pass

    for i in all_info[1:]:
        print(i)

    with open(file=out_name_paths+'/'+out_name_paths+'.txt',mode='w',encoding='utf-8') as ff:
        ff.write(overINFO(all_info[1:]))
        print('\n[+]所有信息已写入...工作完成\n')

    if isDownloadApi:
        wellDone(outpath=out_name_paths,model_any_id=int(findID(inverID=idid,injson=injson_info)[0]),model_name=out_name_paths)
    else:
        print('[-]skip models download\n')
