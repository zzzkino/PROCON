#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()

print "Content-type: text/html\n"
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
print "<html><body style='margin:15px; padding:15px;'>"
print'<head>'
print'<meta http-equiv="X-UA-Compatible" content="IE=edge">'
print'<meta name="viewport" content="width=device-width, initial-scale=1">'
print'<link href="../css/bootstrap.min.css" rel="stylesheet">'
print'<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>'
print'<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>'
print'</head>'
print u"<p><FONT color='#00cc00' size='6'><B>&nbsp; ~調整さま~</B></FONT></p>"

import sqlite3
db = sqlite3.connect('todo.db')
D1 =0
D2 =0
D3 =0
D4 =0
D5 =0
import os
if os.environ['REQUEST_METHOD'] == "POST":
    Top_id = form.getvalue('Top_id')
    names = db.execute('select * from NAME where Top_id = %s ' % Top_id )
    rows = db.execute('select * from Top where id = %s'%Top_id )
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
    for Name in names:
        nameid = Name[0]
        name = Name[1]
        comment = Name[2]
        date1 = Name[3]
        date2 = Name[4]
        date3 = Name[5]
        date4 = Name[6]
        date5 = Name[7]

        point = form.getvalue('%s'%nameid)
        if point == None:
            point = 1
        point =int(point)
        date1 =int(date1)
        date2 =int(date2)
        date3 =int(date3)
        date4 =int(date4)
        date5 =int(date5)
        D1 = D1 + ( date1 * point )
        D2 = D2 + ( date2 * point )
        D3 = D3 + ( date3 * point )
        D4 = D4 + ( date4 * point )
        D5 = D5 + ( date5 * point )

if Mon1==0 or Day1==0:
    D1=0
if Mon2==0 or Day2==0:
    D2=0
if Mon3==0 or Day3==0:
    D3=0
if Mon4==0 or Day4==0:
    D4=0
if Mon5==0 or Day5==0:
    D5=0

list=[D1,D2,D3,D4,D5]
if max(list)==0:
    print u"<p><font size='6' color='red'>最適な日程がありません！エラーです。</font></p>"
else:
    print u"最適な日程が出力されました。<br><br>"

MAX=[I for I,J in enumerate(list) if J == max(list)]
DATE = [[Mon1, Day1],[ Mon2 , Day2], [Mon3 , Day3], [Mon4 , Day4], [Mon5 , Day5] ]

print u"<p><font size='6' color='#6699ff'>タイトル: %s</font></p>"%title
print u"<p><font size='5' color='#ffdb1e'>作成者: %s</font></p>"%auther
print "<p>"
for I in MAX:
    MON = DATE[I][0]
    DAY = DATE[I][1]
    print u"<font color='#ff33cc' size='5'><B>%s月%s日</font>&nbsp;&nbsp; "%(MON,DAY)
    k = I + 3
    names = db.execute('select * from NAME where Top_id = %s ' % Top_id )
    print u"<font color='#0066ff' size='5'>○</font>: &nbsp;"
    for Name in names:
        if Name[k] == 3:
            print "<font color='#339999'>%s</font>"%Name[1]
            print "&nbsp;"
    names = db.execute('select * from NAME where Top_id = %s ' % Top_id )
    print u"<font color='#ccff33' size='4'>△</font>: &nbsp;"
    for Name in names:
        if Name[k] == 1:
            print "<font color='#339999'>%s</font>"%Name[1]
            print "&nbsp;"
    names = db.execute('select * from NAME where Top_id = %s ' % Top_id )
    print u"<font color='#ff0066' size='5'>×</font>: &nbsp;"
    for Name in names:
        if Name[k] == 0:
            print "<font color='#339999'>%s</font>"%Name[1]
            print "&nbsp;"
    print"</p>"

print u"<p>となりました！</p>"
print u"<br><p><a href='titleform.py?id=%s'>戻る</a></p>"%Top_id
print'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>'
print'<script src="../js/bootstrap.min.js"></script>'
print '</body></html>'