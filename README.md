# C站模型信息和图片下载脚本，一键解放双手v1.5 beta
# Civitai model information and image download script, free your hands with one click


## 项目介绍

#### 是否厌倦了手动复制提示词，一张一张图片下载的烦恼，或者模型收集太慢，资源获取太慢，难以整理？
#### C站模型信息和图片下载脚本，一键解放双手（一步到位获取模型，模型信息，图片），非爬虫工具，仅为api调用，方便本地管理资源

### Civitai模型图片，信息，一键模型API交互脚本，一键获取内容到本地。

##### 关于模型下载建议手动下载，该项目仅是搜图的懒人必备工具
![](https://i.postimg.cc/mr3z9p9Z/62c6542b6f3dbeb00589fd53344ad95b.png)
![](https://i.postimg.cc/pTy0R3vk/20250221-093559.png)
![](https://i.postimg.cc/7hJq3bR1/20250219-201759.png)

#### 2025.2.21重要更新：修复模型下载策略，调整了一些代码
#### 2025.2.21更新：全面调整参数，新增模型一键下载功能（但要自己准备api key），修复了其他bug
#### 2025.2.21更新：修复了一些bug，新增模型和返图区下载功能（此项目未实现，但可通过附属工具一键获取图床图片）
#### 2025.2.20待更新：添加返图区图床的图片下载，更为方便
#### 2025.2.20更新：调整了一些代码，并且优化了对简介的处理，提高简介可读性，重要！：修复了对链接标签的提取
#### 2025.2.19更新，修复了json提取功能，调整了部分类的调用

## 使用方法
1.下载构建的发行版开箱即用，输入你需要的任意civitai模型链接（公开的），复制到程序一键运行即可
（你复制的链接样式应该如下：
https://civitai.com/models/469314
https://civitai.com/models/469314?modelVersionId=522182
https://civitai.com/models/6424/chilloutmix
https://civitai.com/models/291275/xianyun-genshin-impact-or-goofy-ai?modelVersionId=393719

）

下载构建版本，双击一键运行：https://github.com/712123846456zcj/civitaiApiTools/releases/tag/1.3
注：构建版本会从链接读取后依次进行作者图片下载，简介信息获取，模型下载步骤，目前没有额外设置。
如果不需要下载模型，建议使用源码版本，因为其可以进行更多修改和配置

2.源码部署

注：该程序采用python3编写，程序可能会因为网络等问题报错，尝试重新运行即可。


对于下载模型，请使用任意文本编辑器打开func\downloadModel\downloadApiMod.py，编辑第五行代码token = "" ，在括号里面添加你的key，否则请不要填写任何内容。
（构建版本中我以及打包好了，程序内部拥有我分享的key，可以一键运行，如果你使用源码运行那么建议使用自己的key）

如何获取你个人的key：https://education.civitai.com/civitais-guide-to-downloading-via-api/

注意，如果没有key将无法下载模型[原因--官方：创作者可以要求人们登录后才能下载他们的资源。这是我们提供的选项，但不是我们的要求——这完全取决于资源所有者。]

3.如果需要批量下载返图区图床的图片，请使用CivitAI_Image_grabber文件夹内的脚本（此项目非本人开发），不过我调整了一些东西，按照文件夹内的教程和需求下载即可。

4.有空闲时间会完善此工具

### 项目参考链接：
#### https://developer.civitai.com/docs/api/public-rest
#### https://github.com/Confuzu/CivitAI_Image_grabber/tree/main
#### https://github.com/Confuzu/CivitAI-Model-grabber
#### https://blog.csdn.net/qq_35977139/article/details/132741398
