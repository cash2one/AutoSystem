todo:
* 调整tinymce的文本框大小 2014.10.18 check
* 确定网站的主题
* 建立网站
* 发布文章同时发布到social media
* 学习kindleear的方法，制作特定网站的模板，获取全文，比如quora，reddit
* 制作自动分析关键字热度，SEO竞争度的程序
* 搜索看有没有让用户提交网址的程序，或者能让wordpress编程这样的程序
* 在social media网站上自动follow相关的用户
* 制作将特定网站文章发布到kindle的多人程序
* 学习推荐系统，研究Hacker News，reddit的推荐算法
* 在rss文章中加入“需要修改”的链接
* 加入使用不同方法获取全文的功能
* 加入队列任务功能

2015.12.24
* 获取youtube认证用户首页视频信息保存到本地 2015-12-26 check

* 在同一页面展示所有的视频信息，能显示视频缩略图，显示视频链接，能够直接输入标题的中文翻译 2015-12-26 check

* 当输入标题的中文翻译后，自动下载youtube视频和字幕，然后合成视频 2015-12-27 check

* 自动下载youtube上订阅的频道最新上传的视频时，过滤掉某些我订阅的频道,但是不需要下载的频道  2016-1-5 check

* 可以根据用户选择视频的分类，上传到优酷上不同的专辑下 2016-1-10 check

* 设置输入优酷tag的功能 check 2016-1-10

* 更新优酷视频信息（描述）的功能 check 2016-1-10

* 将中文和英文的字幕一起合成到视频中 check 2016-1-20

* 将video app 的admin.py分成几个python文件，放在admin目录下 check 2016-1-18

* 制作自动批量合并字幕到视频，然后上传到优酷的功能（修改原来的）。 check 2016-1-25

* 在linode上部署django的运行环境 check

* 设置django自动运行某些命令 用django crontab 或 celery check 2016-2-13

* 编写一个只下载指定youtube视频字幕的功能 check 2016-2-8

* 处理某些视频无法下载字幕，无法合并字幕到视频后上传的问题 check 2016-2-9

* 有些youtube视频不提供自动字幕，无法下载并合并自动字幕，无法正常上传到优酷，每次查找需要上传的视频时都会查到这些视频
check 2016-2-14（不存在这个问题,之前只是由于某视频太大了，未完全下载导致的）

* 在Video Model中设置一个字段，用于控制是否发布视频，选择不发布的视频，之后可以不显示在list diaplay中,
Video的NeedUploadToYouku Manager也不选择该视频 check 2016-2-14

* 解决mkv视频上传到优酷没有声音的问题 check 2016-2-15

* 设置自动获取已下载视频信息，但未下载的youtube视频的时长，格式，文件大小等信息的功能。使用celery后台获取 check 2016-2-15

* 解决youtube认证的问题 check 2016-2-15

* 批量获取youtube视频时长 check 2016-2-15

* 定期获取download文件夹大小，超过一定值时删除早起下载的视频，字幕文件，同时在video model中将对应file字段清空
check 2016-2-18

* 制作调整字幕大小，字体的功能 check 2016-2-21

* 将字幕软写入到视频中，上传到youku后有视频字幕不同步的现象，估计要改为硬写入 check 2016-2-23

* 解决ffmpeg命令在windows上使用绝对路径的问题 (解决方法，使用硬写入)check 2016-2-23

* youtube上的英文vtt字幕包含格式，导致转换成srt字幕再和中文srt字幕合并后有代码，暂时不知道该如何处理。
potplay上也无法正常显示英文vtt字幕
暂时只合并中文字幕到视频
2016-3-10

* 使用官方的youtube-dl (2016.3.6)能监测到自动字幕，但是使用修改版youtube-dl
https://github.com/Don42/youtube-dl/commits/socks_handler_2016-03-03
总是无法监测到字幕
2016-3-14

* youtube 的Credentials的Authorized redirect URIs必须是顶级域名:
Invalid Redirect: http://106.185.37.62/oauth2/oauth2callback must end with a public top-level domain (such as .com or .org)
买个域名还是将本地数据库中auth2_authentication_credectial里的值复制到服务器上的数据库中？
已用后者搞定。
check 2016-3-20

* 远程debug
check 2016-3-20

* 本地和vps上的settings文件不一样，导入settings中变量的代码也不一样，怎么解决？
使用settings目录下__init__.py文件导入各类setting的方法
check 2016-3-20

* 开始部署到VPS上
check 2016-3-20

* 将youtube playlist是否下载的设置导入production环境
check 2016-3-20 使用Django自带的功能dump出数据，再导入

* 编写test

* 研究Fabic部署，获取服务器ssh密钥
http://tutos.readthedocs.org/en/latest/source/ndg.html
check 直接使用ssh 密码登陆

* VPS是否能渲染1080p的视频
check 2016-3-28 可以，但是速度十分慢

* 在本机上测试celery+redis运行对应函数
check 2016-3-28

* 解决ffmpeg合并ass字幕时的字体目录问题
check 2016-3-31 CentOS上安装对应的ttf字体就可以了

* 提高日本linode 上下载youtube视频的速度，目前只有150KiB/s
但2016-3-27 14:49测试，下载速度60m/s
2016-3-27 15:45 下载速度155.56KiB/s
上传到优酷倒是相当快


* Linode上压字幕到视频十分慢，一个150m的视频要45min，虽然subprocess可以后天运行不因为页面timeout而停止，但是无法把压了字幕后的信息录入数据库
用celery异步执行不知道是否可行，或者直接上传原视频，不压字幕
check 2016-3-31 暂时先不压字幕

* 在celery中设置定时获取youtube视频，下载上传youtube视频
check 2016-4-12

* 新加坡Linode上，获取youku的access token后无法保存到django-setting的表中
暂时使用直接在数据库中修改要保持的值的方法代替
check 2016-4-10 更新到pull request版本的django-settings，支持django1.9

* 如何将setting信息正确保存到数据库中
解决：django-setting插件有一个push
https://github.com/jqb/django-settings/pull/30/commits
check 2016-4-10

* 在changelist的界面直接输入video对应的youku model的中文title
check 2016-4


* 在youku model中增加一个set playlist列，这样设置youku model时就能直接设置playlist
上传视频到优酷后，使用celery延时设置playlist即可
check 2016-4

---

* youtube视频不提供自动字幕时，字幕处理。比如video id UQ0w6nO-8sY

* 为celery的subtask加入retry的设置

* 多次上传到优酷不成功后，设置该video的 allow_upload_youku 值为false

* 上传到youku时显示进度

* 设置断点时无法正确映射到remote server（大小写问题）

* 将subtitle分出来到另一个独立的app中，独立的model，用外键与video相连

* 将youku分出来到另一个独立的app中

* 增加对上传到youku多账号支持

* 制定youtube channel与youku playlist的关联，设置自动下载youtube channel下的新视频，自动上传到不同账号的优酷，并设置到指定的youku playlist
2016-6-30

* 获取ImGoTop playlist的视频，提示失败

---

http://127.0.0.1:8000/admin/video/video/QTCJJiZrNYo/?_changelist_filters=p%3D1
等部分视频下载视频信息时，未关联到对应的yt_channel

---

* 可以把youtube视频加入不同的playlist，根据playlist将视频上传到优酷上不同的专辑下

* 在youtube上建立一些playlist，浏览youtube是可以把需要下载的视频加入这些list，
AutoSystem自动下载这些playlist下的视频，并根据playlist设置分类

* 获取视频标题的google翻译

* 根据英文单词等级分类，自动获取较难单词的翻译

* 根据关键字获取amazon affiliate的链接
自动生成优酷的视频介绍，加入各种affiliate链接，京东，亚马逊等

* 将合成字幕的视频上传到百度云中作为备份

* 自动删除一定时期前下载的视频，否则VPS容量不足

* 使用ajax技术，优美简洁的django admin节目，适合在mobile上显示操作

* 制作网站的宣传视频，要求用户点赞，评论，订阅，关注微信微博等，自动合成到视频的前面或后面

* 在威客网站上找人制作视频的片头和片尾，宣传网站、微博、微信账号，或者要求用户订阅
自动将片头、片尾合并合并到视频中

* 在威客网站上翻译文章的信息管理

* 制作网站，翻译国外评测文章

经营微博、微信

---
Celery异步调用，要求将费时的批量操作写成一个函数

将字幕软压到视频中再上传到优酷，会导致字幕显示不正常。只能硬压，但是这样耗时比较久。
---
有的视频没有youtube上无法生成字幕，此时下载字幕函数会提示错误



