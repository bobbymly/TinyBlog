# TinyBlog
-------------
一个简易的博客，旨在学习 python 的过程中用与练习

访问地址：http://111.230.98.25/  

* 后端：python（使用 flask 作为 web 框架）
* 数据库：MySQL
* 前端：只有四个非常简单的页面（虽然不好看，能用就行）

*为了减少工作量，博客不具备很复杂的编辑能力，只支持 markdown 语法的博文，再由前端解析渲染（前端 markdown 解析是网上找的模块）*

-------------------
## 后端

* 从数据拉取博文数据并返回给前端
* 验证用户信息（账号密码 MD5 加密），并为前端返回带有时限的token作为cookie（时限为一天），验证方式为 MD5（MD5（密码）+当天日期）
* 向数据库中添加/修改博文

## 数据库
数据库只有两张表

* 用户信息表

![](https://github.com/bobbymly/TinyBlog/blob/master/static/user.png?raw=true)

* 博文信息表

![](https://github.com/bobbymly/TinyBlog/blob/master/static/craft.png?raw=true)

## 前端
前端只有四个简陋的页面，通过ajax获取数据更新各页面内容
* index.html 主页
* article.html 博文内容页
* login.html 用户登陆页
* manage.html 博客管理页
