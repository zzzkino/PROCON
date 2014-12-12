#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Content-type: text/html\n"
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
print "<html><body style='margin:15px;padding:15px;'>"
print'<head>'

print'<meta http-equiv="X-UA-Compatible" content="IE=edge">'
print'<meta name="viewport" content="width=device-width, initial-scale=1">'

print'<link href="../css/bootstrap.min.css" rel="stylesheet">'
print'<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>'
print'<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>'
print'</head>'


import cgi
form = cgi.FieldStorage()
id = form.getvalue('id', '')
print u"<p><FONT color='#00cc00' size='6'><B>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ~調整さま~</B></FONT></p>"
print u"<p><FONT color='#1e90ff' size='6'><B>スケジュール管理画面</B></FONT></p>"
import sqlite3
db = sqlite3.connect('todo.db')

rows = db.execute('select * from Top ')
for row in rows:
    id = row[0]
    title = row[1]
    auther = row[2]
    Mon1 = row[3]
    Day1 = row[4]
    Mon2 = row[5]
    Day2 = row[6]
    Mon3 = row[7]
    Day3 = row[8]
    Mon4 = row[9]
    Day4 = row[10]
    Mon5 = row[11]
    Day5 = row[12]
    print u"<a href='titleform.py?id= %s'><font color='#ffcc00'>スケジュール</font>: <font color='#ff33cc'>%s</font>&nbsp;&nbsp;(<font color='#ffcc00'>作成者</font>: <font color='#ff33cc'>%s</font>)</a>" % (id,title,auther)

    print "<p>&nbsp; &nbsp; &nbsp; 参加者: "
    names = db.execute('select * from NAME where Top_id = %s' %id)
    for Name in names:
        nameid = Name[0]
        name = Name[1]
        comment = Name[2]
        date1 = Name[3]
        date2 = Name[4]
        date3 = Name[5]
        date4 = Name[6]
        date5 = Name[7]
        Top_id = Name[8]
        print "<font size='4' color='#339999'>%s</font> &nbsp; "%name
    print '</p><hr>'
db.close()
print u"<a href='Topform.py'><font color='#3333cc'>スケジュール追加</font></a>"
print'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>'
print'<script src="../js/bootstrap.min.js"></script>'
print '</body></html>'