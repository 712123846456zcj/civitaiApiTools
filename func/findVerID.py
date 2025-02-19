import json

from func.imageDownload import imd

# import ast


md_list = []

def findID(inverID, injson):
    """
    输入版本id
    :param inverID:
    :return:
    """

    if inverID != -999:
        for i in range(0, len(injson['modelVersions'])):

            if int(inverID) == int(injson['modelVersions'][i]['id']):

                # print('yes', i)
                md_list.append(injson['modelVersions'][i]['id'])
                md_list.append(injson['modelVersions'][i]['name'])
                md_list.append(injson['modelVersions'][i]['baseModel'])
                try:
                    md_list.append(injson['modelVersions'][i]['description'])
                except:
                    md_list.append('无')
                try:
                    md_list.append(injson['modelVersions'][i]['trainedWords'])
                except:
                    md_list.append('无')
    else:
        md_list.append(injson['modelVersions'][0]['id'])
        md_list.append(injson['modelVersions'][0]['name'])
        md_list.append(injson['modelVersions'][0]['baseModel'])
        try:
            md_list.append(injson['modelVersions'][0]['description'])
        except:
            md_list.append('无')
        try:
            md_list.append(injson['modelVersions'][0]['trainedWords'])
        except:
            md_list.append('无')


    return md_list


def reID(inverID2, injson2, inpath):
    """
    输入版本id
    :param inverID2:
    :return:
    """
    if inverID2 != -999:

        i0 = 0
        for i in range(0, len(injson2['modelVersions'])):

            if int(inverID2) == int(injson2['modelVersions'][i]['id']):
                # print('yes', i)
                i0 = i

        imd(indata=injson2,i=i0,out_path=inpath)
    else:
        imd(indata=injson2, i=0, out_path=inpath)
    return

