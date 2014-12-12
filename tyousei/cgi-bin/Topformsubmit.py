#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()

import sqlite3
db = sqlite3.connect('todo.db')

import os
if os.environ['REQUEST_METHOD'] == "POST":
    id = form.getvalue('id')
    title = form.getvalue('title')
    auther = form.getvalue('auther')
    Mon1 = form.getvalue('Mon1')
    Day1 = form.getvalue('Day1')
    Mon2 = form.getvalue('Mon2')
    Day2 = form.getvalue('Day2')
    Mon3 = form.getvalue('Mon3')
    Day3 = form.getvalue('Day3')
    Mon4 = form.getvalue('Mon4')
    Day4 = form.getvalue('Day4')
    Mon5 = form.getvalue('Mon5')
    Day5 = form.getvalue('Day5')

if id is None:
    sql = "insert into Top(title,auther,Mon1,Day1,Mon2,Day2,Mon3,Day3,Mon4,Day4,Mon5,Day5) values('%s', '%s', %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (title,auther,Mon1,Day1,Mon2,Day2,Mon3,Day3,Mon4,Day4,Mon5,Day5)
    cursor = db.cursor()
    cursor.execute(sql)
else:
    sql = "update Top set title = '%s', auther = '%s', Mon1 = %s,Day1 = %s, Mon2 = %s,Day2 = %s, Mon3 = %s,Day3 = %s, Mon4 = %s,Day4 = %s, Mon5 = %s,Day5 = %s where id = %s" % (title, auther,Mon1,Day1,Mon2,Day2,Mon3,Day3,Mon4,Day4,Mon5,Day5 , id)
    cursor = db.cursor()
    cursor.execute(sql)
db.commit()
db.close()

print "Content-type: text/html\n"
print "<meta http-equiv='refresh' content='0;URL=http://localhost:8000/cgi-bin/list.py'>"