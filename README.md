# C站模型信息和图片下载脚本，一键解放双手v1.4 beta
# Civitai model information and image download script, free your hands with one click

## 项目介绍
#### C站模型信息和图片下载脚本，一键解放双手（一步到位获取模型，模型信息，图片），非爬虫工具，仅为api调用，方便本地管理资源
#### 包含模型的简介（简介图尚未实现下载，~~简介保留html代码未处理~~已处理html代码）和面板信息，记录到文件夹当中
#### 作者例图一键下载到当前文件夹
##### 关于模型下载建议手动下载，该项目仅是搜图的懒人必备工具
![](https://i.postimg.cc/mr3z9p9Z/62c6542b6f3dbeb00589fd53344ad95b.png)
[20250221-093559.png](https://postimg.cc/PpsbM3P8)
[](https://i.postimg.cc/7hJq3bR1/20250219-201759.png)![](https://i.postimg.cc/7hJq3bR1/20250219-201759.png)

#### 2025.2.21更新：全面调整参数，新增模型一键下载功能（但要自己准备api key），修复了其他bug
#### 2025.2.21更新：修复了一些bug，新增模型和返图区下载功能（计划，未实现）
#### 2025.2.20待更新：添加返图区图床的图片下载，更为方便
#### 2025.2.20更新：调整了一些代码，并且优化了对简介的处理，提高简介可读性，重要！：修复了对链接标签的提取

## 使用方法
1.打开浏览器。进入c站，找到你想要的模型，选择模型版本，在地址栏中复制该链接。
（你复制的链接样式应该如下：
https://civitai.com/models/469314

https://civitai.com/models/469314?modelVersionId=522182

https://civitai.com/models/6424/chilloutmix

https://civitai.com/models/291275/xianyun-genshin-impact-or-goofy-ai?modelVersionId=393719

）

2.粘贴到程序中，回车即可

下载构建版本，双击一键运行：https://github.com/712123846456zcj/civitaiApiTools/releases/tag/1.3

注：该程序采用python3编写，程序可能会因为网络等问题报错，尝试重新运行即可。

对于下载模型，请使用任意文本编辑器打开func\downloadModel\downloadApiMod.py，编辑第五行代码token = "" ，在括号里面添加你的key，否则请不要填写任何内容。

如何获取你个人的key：https://education.civitai.com/civitais-guide-to-downloading-via-api/

注意，如果没有key将无法下载模型[原因--官方：创作者可以要求人们登录后才能下载他们的资源。这是我们提供的选项，但不是我们的要求——这完全取决于资源所有者。]

3.如果需要批量下载返图区图床的图片，请使用CivitAI_Image_grabber文件夹内的脚本（此项目非本人开发），不过我调整了一些东西，按照文件夹内的教程和需求下载即可。

4.有空闲时间会完善此工具

### 项目参考链接：
#### https://developer.civitai.com/docs/api/public-rest
#### https://github.com/Confuzu/CivitAI_Image_grabber/tree/main
#### https://github.com/Confuzu/CivitAI-Model-grabber
#### https://blog.csdn.net/qq_35977139/article/details/132741398
