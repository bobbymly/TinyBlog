# encoding:utf-8 -*-
import hashlib
import MySQLdb
import sys
import datetime
reload(sys)
sys.setdefaultencoding("utf-8")


host = "127.0.0.1"
user = "root"
password = ""
database = "Blog"
charset = "utf8"

#连接数据库
def open():
    conn = MySQLdb.connect(host, user, password, database, charset=charset)
    cursor = conn.cursor()
    return conn, cursor

#断开数据库连接
def close(conn, cursor):
    conn.close()
    cursor.close()

#获取所有已发布博文
def allArticle():
    conn, cursor = open()
    cursor.execute("SELECT content,id,title from craft where type = '1' order by id DESC ;")
    result = cursor.fetchall()
    close(conn, cursor)
    return result

#获取指定博文
def getArticle(id):
    conn, cursor = open()
    cursor.execute("SELECT content,pubTime,type,name from craft,user where craft.id = %s and userid = user.id;" % id)
    result = cursor.fetchall()
    close(conn, cursor)
    return result

#获取帐号密码
def APIlogin(result):
    conn, cursor = open()
    result[0] = MySQLdb.escape_string(result[0])
    result[1] = MySQLdb.escape_string(result[1])
    cursor.execute("select name,password from user where name = '%s'" % result[0])
    result = cursor.fetchall()
    close(conn, cursor)
    return result

#添加博文
def addArticle(data, userId, op):
    conn, cursor = open()
    data["title"] = MySQLdb.escape_string(data["title"].decode("utf-8"))
    data["content"] = MySQLdb.escape_string(data["content"].decode("utf-8"))
    cursor = conn.cursor()
    today = datetime.date.today()
    cursor.execute(
        "insert into craft(userid,title,content,pubTime,type) values ('%s','%s','%s','%s','%s')" % (
            userId, data["title"], data["content"], today.strftime("%Y-%m-%d"), op))
    conn.commit()
    #cursor.execute("select id from craft where ")
    #result = cursor.fetchall()
    close(conn, cursor)
    return 

#获取博文信息
def articleManage():
    conn, cursor = open()
    cursor.execute("SELECT id,title,type,pubTime from craft where type != '4' ORDER BY pubTime desc;")
    result = cursor.fetchall()
    close(conn, cursor)
    return result

#更改类型
def change(result):
    conn, cursor = open()
    #用户输入转义，防止SQL注入
    result[0] = MySQLdb.escape_string(str(result[0]))
    result[1] = MySQLdb.escape_string(result[1])
    cursor = conn.cursor()
    if (result[1] == '4'):
        cursor.execute("DELETE FROM craft where id = '%s'; "%(result[0]))
    else:
        cursor.execute("UPDATE craft set type = '%s' where id = '%s';" % (result[1], result[0]))
    conn.commit()
    close(conn, cursor)
    return

def alterArticle(content,id):
    conn, cursor = open()
    # data["title"] = MySQLdb.escape_string(data["title"].decode("utf-8"))
    content= MySQLdb.escape_string(content.decode("utf-8"))
    cursor = conn.cursor()
    cursor.execute(
        "update craft set content='%s' where id='%s' " % (content,id))
    conn.commit()
    #cursor.execute("select id from craft where ")
    #result = cursor.fetchall()
    close(conn, cursor)
    return 


# #删除博文
# def delete(result):
#     conn,cursor = open()
#     result[0] = MySQLdb.escape_string(str(result[0]))
#     result[1] = MySQLdb.escape_string(result[1])
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM craft where id = '%s'; "%(result[0]))
#     conn.commit()
#     close(conn,cursor)
#     return


#获取所有账号密码
def verifyToken():
    conn, cursor = open()
    cursor.execute("select password,id from user ;")
    result = cursor.fetchall()
    close(conn, cursor)
    return result

#添加用户表
def createUser():
    conn, cursor = open()
    cursor.execute("DROP table if EXISTS user")
    cursor.execute('''create table user (
id INT(11) primary key not null unique auto_increment,
name VARCHAR(45),
isAdmin VARCHAR(45),
regTime DATE,
password VARCHAR(45)
)''')
    close(conn, cursor)
    return

#添加博文表
def createCraft():
    conn, cursor = open()
    cursor.execute("DROP table if EXISTS craft")
    cursor.execute('''create table craft (
id INT(11) primary key not null unique auto_increment,
userid INT(11),
title LONGTEXT,
content LONGTEXT,
pubTime date,
type INT(11)
)
''')
    close(conn, cursor)
    return

#添加用户,密码两次 md5 加密
def insertUser(username, password):
    conn, cursor = open()
    today = datetime.date.today()
    Md5 = hashlib.md5()
    Md5.update(password)
    Md5hex = Md5.hexdigest()
    Md52 = hashlib.md5()
    Md52.update(Md5hex)
    password_twice = Md52.hexdigest()
    cursor.execute("insert into user values('1','%s','1','%s','%s')" % (
        username, today.strftime("%Y-%m-%d"), password_twice))
    conn.commit()
    close(conn, cursor)
    return

#添加博文
def insertCraft():
    conn, cursor = open()
    today = datetime.date.today()
    cursor.execute(
        "insert into craft values('1','1','Hello World！','# Hello World!\n\n* 这是一个轻量的博客，支持 markdown； \n* 这是博客的第一篇文章；','%s','1');" % (
            today.strftime(
                "%Y-%m-%d")))
    conn.commit()
    close(conn, cursor)
    return
