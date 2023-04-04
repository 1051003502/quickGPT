import pymysql

#基本连接测试
def test1():
    #1连接
    conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="sdu2020",charset="utf8",db="unicom")

    #基于cursor发指令
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

    #2发指令
    cursor.execute("insert into admin(username,password,mobile) values('zhaoxin','123456','18734608179')")
    conn.commit()

    #3关闭连接
    cursor.close()
    conn.close()

#防止sql注入的写法
def test2():
    # 1连接
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="sdu2020", charset="utf8", db="unicom")

    # 基于cursor发指令
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2发指令
    # sql1="insert into admin(username,password,mobile) values(%s,%s,%s)"
    # cursor.execute(sql1,["pig","654854","18734608888"])

    sql2="insert into admin(username,password,mobile) values(%(username)s,%(password)s,%(mobile)s)"
    cursor.execute(sql2,{"username":"root","password":"98465","mobile":"13334608888"})
    conn.commit()

    # 3关闭连接
    cursor.close()
    conn.close()

#查询
def test3():
    # 1连接
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="sdu2020", charset="utf8", db="unicom")

    # 基于cursor发指令
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2发指令
    # sql1="insert into admin(username,password,mobile) values(%s,%s,%s)"
    # cursor.execute(sql1,["pig","654854","18734608888"])

    sql1 = "select * from admin"
    cursor.execute(sql1)
    #fetchall把查询的所有数据都获得
    res=cursor.fetchall()
    for i,row in enumerate(res):
        if i==0:
            for key in row:
                print(key,end=" ")
            print()
        for key in row:
            print(row[key],end=" ")
        print()
    print(res)
    #查询不需要commit
    #conn.commit()

    # 3关闭连接
    cursor.close()
    conn.close()
def insert_user(user_name,user_pwd,user_mobile):
    # 1连接
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="sdu2020", charset="utf8", db="unicom")

    # 基于cursor发指令
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2发指令
    # sql1="insert into admin(username,password,mobile) values(%s,%s,%s)"
    # cursor.execute(sql1,["pig","654854","18734608888"])

    sql2 = "insert into admin(username,password,mobile) values(%(username)s,%(password)s,%(mobile)s)"
    cursor.execute(sql2, {"username": user_name, "password": user_pwd, "mobile": user_mobile})
    conn.commit()

    # 3关闭连接
    cursor.close()
    conn.close()

from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)
@app.route("/add/user",methods=["GET","POST"])
def add_user():
    if request.method=="GET":
        return render_template("add_user.html")
    elif request.method=="POST":
        print(request.form)

        insert_user(request.form.get("user"),request.form.get("pwd"),request.form.get("mobile"))
        return "添加成功"

@app.route("/show/user")
def show_user():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="sdu2020", charset="utf8", db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql1 = "select * from admin"
    cursor.execute(sql1)
    res = cursor.fetchall()
    for i, row in enumerate(res):
        if i == 0:
            for key in row:
                print(key, end=" ")
            print()
        for key in row:
            print(row[key], end=" ")
        print()
    cursor.close()
    conn.close()
    return render_template("show_user.html",data_list=res)
if __name__ == '__main__':
    app.run()



