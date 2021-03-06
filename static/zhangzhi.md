# 个人简历

## 基本信息

姓名：张智&emsp;&emsp;&emsp; 性别：男&emsp;&emsp;&emsp; 求职岗位: Python后端开发工程师

生日：1995-03-05 &emsp;&emsp;&emsp; 电话：17601010822&emsp;&emsp;&emsp;邮箱：zhangzhi_dev@qq.com

Github：https://github.com/ZhangzhiS &emsp;&emsp;&emsp;个人博客：https://zz.zzs7.top

## 个人技能

- 两年的Python开发经验；
- 熟练使用Python进行业务开发，了解Python的网络和Web编程，熟悉Python的并发；
- 熟练使用Python常用的标准库以及第三方库；
- 熟练使用Django框架，了解Flask、Tornado的使用；
- 熟悉Mysql、Redis缓存、Mongodb数据库的使用；
- 熟练使用Scrapy爬虫框架，了解常见的反爬虫机制和应对手段；
- 熟练使用正则表达式，CSS，selector选择器等提取网页信息;
- 熟悉RESTful API接口规范；
- 熟练使用Linux环境进行开发部署；
- 熟悉微信系列的开发，包括公众号和小程序；
- 掌握常用的数据结构和算法；
- 熟练使用团队协作开发工具Git；
- 了解LXC以及Docker。
- 了解敏捷开发；
- 代码风格优秀，有良好的写注释的习惯。

## 工作经历
**2017年8月至2019年2月任职于元智合一，担任Python开发工程师**

## 项目经验

### 图片社交小程序“粉我”

**可在微信小程序中搜索“粉我FansMe”体验**，“粉我”目标是做一个面向大学生的图片社交平台，运营范围定位在程度地区。项目使用Django框架开发，采用敏捷开发的方式快速迭代，我在项目中参与了服务端的开发以及负责项目部署。

- admin管理：定位是一个强运营的产品，所以Django自带的admin无法满足需求，替换第三方的xadmin，并对一些模板，方法进行了重写，实现了包括且不止以下功能：
  - 添加新事件，对小程序首页展示的事件顺序可以进行手动排序。
  - 添加运营学校的同时，根据向该学校开放的事件配置生成校内前三名的奖金数目（可手动更改）。
  - 对违规用户进行封号处理。
- 用户提现模块：使用微信商户平台的接口进行开发，采用商户向用户付款的方式完成用户的提现操作，限制了每日平台提现的总额度以及用户提现次数（可在admin中配置）。
- 其他业务逻辑：部分接口的开发，请求第三方服务模块的开发（包括阿里的内容安全，腾讯的人脸检测，对象存储等），限制某些区域用户的开发等等。
- 接口文档编写：离职之前交接项目的时候，使用sphinx-doc对代码中的注释进行提取，生成了接口文档。
- 部署：公司为创业公司，没有运维人员，刚好自己喜欢计算机，也稍微懂一点这方面的知识，所以负责了我参与的所有项目的部署，迁移以及维护。项目采用nginx+uwsgi+Django的方式，部署了两台服务器，使用腾讯的负载均衡进行请求任务的分发。

### 世界杯聊天机器人“小真”

一个有关足球知识的问答的公众号，以聊天的方式获取简介、赛程、球队、球员、教练、场地、比分等信息。项目使用了Google的dialogflow做语义分析来回答用户的问题，我负责抓取需要的数据。

-  实时新闻的抓取：选择抓取推特，FIFA官网，国内足球社区等新闻源。由于抓取到的新闻格式不统一，针对性的做了处理，用来在固定的新闻模板上展示。爬取推特的时候伪装用户来针对反爬。使用Python的sched+os完成每5分钟抓取一次的启动脚本。
- 足球相关数据的抓取：来源于国内的足球社区，使用Charles对他们的app分析，找到了对应的接口以及数据的规律，采用了动态IP代理池的方式应对相应的反爬机制，进行了长时间的爬取，采集了近年来所有的球员、教练、比赛记录等信息。
- 实时比分的抓取：分析国外FlashScore的接口，通过对比分析，找到了比赛过程中发生的事件对应的信号，进行赛况，比分的实时推送。实时推送的速度比直播画面会早很多。
- 其他数据的抓取：赔率，其他联赛的赛程、比赛结果。

### 答题小程序“球迷馆”

以足球知识为主的答题小程序，已停止服务，可以搜索“**猜猜女孩**”来体验答题，匹配用户都是机器人。项目中负责后端业务逻辑、接口的开发。

- 匹配模块：匹配模块包括排位赛的随机匹配以及好友对战玩法中的匹配，使用Redis的hash结构来完成的分级匹配池。上线期间稳定运行，未出现bug，性能良好。
- 用户数据模块：在更新用户数据的时候，使用同时写Mysql和Redis，读Redis的方案，减少Mysql的操作来优化接口性能。

上线运营一段时间后，与著名足球解说合作，作为一个子玩法合并到了对方的**“猜猜女孩**""小程序中。

### 在线教育平台

实现一个在线教育平台，包括教师端以及学生端，实现学生管理以及作业管理等功能。项目中负责部分功能开发。

- 熟练使用Django的模板语法渲染前端页面。
- 使用ajax的方式一部加载页面中的部分数据，提升页面加载速度。
- 了解腾讯TAPD敏捷开发平台的使用。
- 熟练使用Git进行代码管理。

## 教育信息

- 学历：大专
- 毕业院校：江西应用科技学院
- 专业：计算机应用与技术
