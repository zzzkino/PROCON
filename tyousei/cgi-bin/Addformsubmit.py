#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
form = cgi.FieldStorage()

import sqlite3
db = sqlite3.connect('todo.db')

import os
if os.environ['REQUEST_METHOD'] == "POST":
    id = form.getvalue('id')
    name = form.getvalue('name')
    comment = form.getvalue('comment')
    date1 = form.getvalue('date1')
    date2 = form.getvalue('date2')
    date3 = form.getvalue('date3')
    date4 = form.getvalue('date4')
    date5 = form.getvalue('date5')
    Top_id = form.getvalue('Top_id')
    if id is None :
        sql = "insert into NAME(name , comment, date1, date2, date3, date4, date5, Top_id ) values('%s', '%s', %s, %s, %s, %s, %s, %s )" % (name, comment, date1, date2, date3, date4, date5, Top_id )
        cursor = db.cursor()
        cursor.execute(sql)
    else:
        sql = "update NAME set name = '%s', comment = '%s', date1 = %s,date2 = %s, date3 = %s,date4 = %s, date5 = %s,Top_id = %s where id = %s " % (name,comment,date1,date2,date3,date4,date5, Top_id, id )
        cursor = db.cursor()
        cursor.execute(sql)
    db.commit()
    db.close()

print "Content-type: text/html\n"
print "<meta http-equiv='refresh' content='0;URL=http://localhost:8000/cgi-bin/titleform.py?id=%s'>"%Top_id
