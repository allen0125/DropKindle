# DropKindle

DropKindle 将 Dropbox 、坚果云、OneDrive中的文档推送到 Kindle


## 使用指南:

由于作者很菜，还不上进，不学习，所以DropKindle用起来很难受，如果用着不爽可以提PR但是不能打我(

DropKindle也就3个页面，index login register。

须将 drop2kindle#gmail.com ( #用at符号代替 ) 添加到 Kindle 白名单当中

新用户需要先注册，注册邮箱需要用Kindle的收件箱。
我也没推送个txt来验证是不是你的Kindle邮箱，反正得自己看准了，写对了。
然后login页面登录。登录完成之后点DropBox OAuth2 链接获取Dropbox的授权码，
在获取授权的同时DropKindle会在你的Dropbox 应用文件夹当中新建一个DKindle文件夹。
DropKindle只有DKindle这个文件夹的权限，所以这个文件夹中要避免存放隐私相关的文件。
完成获取权限之后就可以将需要推送的文本文件(兹瓷的文件⬇️️列出来了)放到DKindle这个文件夹当中
然后在dropkindle主页点击Push即可完成推送。每次推送都会有历史记录，所以在DKindle文件夹中
已经推送过的文件是不会再次被推送的。

文件大小限制: 20MB

大概就是这么多了吧。

写完了发现我还是好好学习，做的好一些吧……

本来剧本是Django-Crontab来自动推送的，可是Crontab的环境变量还没搞定，然后我觉得手动推送也挺好
本身也不是高频操作，然后还能节(shao)省(xie)性(ba)能(ge)。

## 依赖工具:

- Django
- Dropbox Python SDK
- SQLite
- ~~Django-Crontab~~

## 支持文件类型:

- mobi
- azw
- txt
- doc
- docx
- pdf

## Todo:

- 坚果云支持
- OneDrive支持
