import json,ast

# with open(file='2.json',mode='r',encoding='utf-8') as f:
#     ff = f.read()
#     print(type(ff))
#
#     sss = json.dumps(ff,indent=4,ensure_ascii=False)
#     sss = json.loads(sss)
#     print(sss)
#     print(type(sss))

# 522182
md = input('your id:')
with open(file='2.json',mode='r',encoding='utf-8') as f:
    ff = f.read()
    print(type(ast.literal_eval(ff)))
    s = ast.literal_eval(ff) #json_info
    # print(s['modelVersions'])
    # print(len(s['modelVersions']))

    for i in range(0,len(s['modelVersions'])):

        # print(s['modelVersions'][i]['id'])
        if int(md) == int(s['modelVersions'][i]['id']):
            print('yes',i) #578932/
            print(s['modelVersions'][i]['images'])




