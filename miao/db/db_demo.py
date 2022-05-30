import sqlite3
from datetime import datetime, timedelta


def connect_db(db_file):
    conn = None
    try:
        # 链接数据库
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    if conn is not None:
        return conn


def close_db(cur, conn):
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


def create_table(db_file):
    sql = """CREATE TABLE person (
                id       BIGINT (18)  PRIMARY KEY,
                name     VARCHAR (50) NOT NULL,
                age      INT (10)     NOT NULL,
                birthday DATETIME     NOT NULL
        );"""
    conn = connect_db(db_file)
    # 获取操作游标 游标就是当前操作的行
    cur = conn.cursor()
    print(sql)
    # 执行sql语句
    cur.execute(sql)
    # 提交SQL操作 提交后才会生效
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()


def insert_data(db_file):
    """
        sql语句推荐使用占位符的形式
    """
    # 获取当前时间
    datetime_now = datetime.now()
    # 在当前时间基础上加1天
    # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    birthday = datetime_now - timedelta(days=1)
    sql = 'insert into person(id,name,age,birthday) values (?,?,?,?)'
    data = (1, '张三', 23, birthday)
    conn = connect_db(db_file)
    # 获取操作游标 游标就是当前操作的行
    cur = conn.cursor()
    print(sql)
    # 执行sql语句
    cur.execute(sql, data)
    # 提交SQL操作 提交后才会生效
    conn.commit()
    
    """
        使用拼接字符串,容易导致sql注入,以及数据格式 ' " 等转义问题
    """
    # name = '李四'
    # birthday = datetime.now() - timedelta(weeks=1)
    # sql = f'insert into person(id,name,age,birthday) values ({2},\'{name}\',{30},\'{birthday}\')'
    # conn = connect_db(db_file)
    # # 获取操作游标 游标就是当前操作的行
    # cur = conn.cursor()
    # print(sql)
    # cur.execute(sql)
    # # 提交SQL操作 提交后才会生效
    # conn.commit()

    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()


def select_data(db_file, id=None):
    sql = 'select * from person'
    if id is not None:
        sql = sql + f" where id = {id}"
    conn = connect_db(db_file)
    # 获取操作游标 游标就是当前操作的行
    cur = conn.cursor()
    print(sql)
    # 执行sql语句
    rows = cur.execute(sql)
    list = []
    for row in rows:
        bean = []
        for r in row:
            bean.append(r)
        list.append(bean)
    # 提交SQL操作 提交后才会生效
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()
    return list


def update_data(db_file, id, age):
    sql = f'update person set age={age} where id = {id}'
    conn = connect_db(db_file)
    # 获取操作游标 游标就是当前操作的行
    cur = conn.cursor()
    print(sql)
    # 执行sql语句
    cur.execute(sql)
    # 提交SQL操作 提交后才会生效
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()


def delete_data(db_file, id):
    sql = f'delete from person where id = {id}'
    conn = connect_db(db_file)
    # 获取操作游标 游标就是当前操作的行
    cur = conn.cursor()
    print(sql)
    # 执行sql语句
    cur.execute(sql)
    # 提交SQL操作 提交后才会生效
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()


if __name__ == '__main__':
    # db_file='data.db'
    # 数据库路径 如果路径里面没有这个数据库，会自动创建
    db_file = r'E:\SQLite_DB\test.db'
    # create_table(db_file)
    insert_data(db_file)
    # update_data(db_file, 1, 18)
    # delete_data(db_file, 1)
    list = select_data(db_file)
    s = 0
    for person in list:
        s += 1
        print(f"打印第{s}个数据")
        print(person)
