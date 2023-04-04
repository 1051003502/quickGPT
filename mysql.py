import pymysql


def get_app_data_from_dataset():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="sdu2020", charset="utf8", db="quickgpt")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql1 = "select * from app"
    cursor.execute(sql1)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def insert_app_data_to_dataset(app_name, app_introduction, prompt, example):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="sdu2020", charset="utf8", db="quickgpt")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql1 = "insert into app(app_name, app_introduction, prompt, example) values(%(app_name)s,%(app_introduction)s,%(prompt)s,%(example)s)"
    cursor.execute(sql1, {"app_name": app_name, "app_introduction": app_introduction, "prompt": prompt,"example":example})
    conn.commit()

    # 3关闭连接
    cursor.close()
    conn.close()
    return True

def test_get_app_data_from_dataset():
    app_data = get_app_data_from_dataset()
    pass


if __name__ == '__main__':
    test_get_app_data_from_dataset()
