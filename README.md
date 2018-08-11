# Django-Chatroom  
基于Django-1.11.8的新闻论坛+web聊天室  

实现的功能：  
  1.登录/注册  
  2.后台管理  
  3.富文本框发帖（引入前端框架bootstrap）  
  4.评论功能，评论下追加评论（递归+AJAX）  
  5.点赞功能  
  6.阅读量，点赞数，帖子数的统计  
  7.分板块发帖  
  8.首页有分页功能，增加了锚点  
  9.群组聊天+个人聊天  

项目结构:  
一共两个个app：  
  1.bbs：实现新闻论坛  
  2.webchat:实现聊天室  

模型models ： 使用ORM模型映射数据库中五张表  
  1.帖子表  
  2.评论表  
  3.板块表  
  4.用户表  
  5.用户组表  
  
本项目所需模块:  

pymysql  
#可使用sudo pip3 install pymysql安装  
mysqldb目前还不支持3.0python,使用pymysql驱动链接mysql数据库  
  
Pillow  
#可使用$ pip3 install Pillow安装  
要安装Pillow,才能使用ImageField字段  


前期配置：  
  1.同步数据库  
    $ python3 manage.py makemigrations  
    $ python3 manage.py  migrate  
    
  2.创建一个后台管理的supperuser用户  
    $ python3 manage.py createsuperuser  
  
####还有好多想要实现的功能没有实现，以后有机会实现了会持续更新的！！！～～～  
