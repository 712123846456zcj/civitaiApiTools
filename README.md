# C站模型信息和图片下载脚本，一键解放双手v1.1 beta
## 项目介绍

#### C站模型信息和图片下载脚本，一键解放双手
#### 包含模型的简介（简介图尚未实现下载，~~简介保留html代码未处理~~已处理html代码）和面板信息，记录到文件夹当中
#### 作者例图一键下载到文件夹
##### 关于模型下载建议手动下载，该项目仅是搜图的懒人必备工具
![](https://i.postimg.cc/mr3z9p9Z/62c6542b6f3dbeb00589fd53344ad95b.png)

[](https://i.postimg.cc/7hJq3bR1/20250219-201759.png)![](https://i.postimg.cc/7hJq3bR1/20250219-201759.png)

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

注：该脚本采样python3和标准库编写，利用civitai的官方API完成主要工作，下载到本地使用python解释器运行即可，无需第三方库，但cookie需要自行查找并且复制到main_func.py当中（好像也不需要），另外程序可能会因为网络等问题报错，尝试重新运行即可。

3.如果需要批量下载返图区图床的图片，请使用CivitAI_Image_grabber文件夹内的脚本（此项目非本人开发），不过我调整了一些东西，按照文件夹内的教程和需求下载即可。

4.有空闲时间会完善此工具

### 项目参考链接：
#### https://github.com/Confuzu/CivitAI_Image_grabber/tree/main
#### https://developer.civitai.com/docs/api/public-rest
#### https://blog.csdn.net/qq_35977139/article/details/132741398
