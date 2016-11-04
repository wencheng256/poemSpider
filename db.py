# -*- coding: utf-8 -*-
import MySQLdb as m


def insert(title, writer, content, exp, knowledge):
    db = m.connect(db='poem', host='www.mario256.cn', user='root', passwd='abc123', charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO poem(title, writer, content, exp, knowledge) VALUES (%s, %s, %s, %s, %s)",
        (title, writer, content, exp, knowledge))
    db.commit()
    db.close()


def finish(n):
    db = m.connect(db='poem', host='www.mario256.cn', user='root', passwd='abc123', charset="utf8")
    cursor = db.cursor()
    cursor.execute("INSERT INTO page(page) VALUES (%s)", n)
    db.commit()
    db.close()


def error(msg):
    db = m.connect(db='poem', host='www.mario256.cn', user='root', passwd='abc123', charset="utf8")
    cursor = db.cursor()
    cursor.execute("INSERT INTO err(msg) VALUES (%s)", msg)
    db.commit()
    db.close()
