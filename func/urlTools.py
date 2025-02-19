

def urlINFO(uurrll=''):
    """
    简单处理url当中的参数，关键只有两个id

    :param uurrll:
    :return:
    """

    idlist = []
    if r'//' in uurrll:
        uurrll = uurrll.replace(r'//', r'/')

    if 'modelVersionId' not in uurrll:
        s = uurrll.rstrip().split('/')
        idlist.append(s[3])
        idlist.append(-999)
    else:
        s = uurrll.rstrip().split('?')
        org = uurrll.rstrip().split('/')
        s2 = s[1].replace('modelVersionId=','')
        idlist.append(org[3])
        idlist.append(s2)


    return idlist

# print(urlINFO(input("your url:")))


