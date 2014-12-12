#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()

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
print u"<p><FONT color='#00cc00' size='6'><B>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ~調整さま~</B></FONT></p>"

import sqlite3
db = sqlite3.connect('todo.db')
id = form.getvalue('id', '')
if id == '':
    title = ''
    auther = ''
    Mon1 = ''
    Day1 = ''
    Mon2 = ''
    Day2 = ''
    Mon3 = ''
    Day3 = ''
    Mon4 = ''
    Day4 = ''
    Mon5 = ''
    Day5 = ''
else:
    rows = db.execute(' select * from Top where id = %s ' % id)
    for row in rows:
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

        L= [Mon1, Day1, Mon2, Day2, Mon3, Day3, Mon4, Day4, Mon5, Day5]
        L2 = [x if x != 0 else '-' for x in L]

        print u"<p><font size='6' color='#6699ff'>タイトル: %s</font> &nbsp; &nbsp; "%title
        print "<a href=' Topdeletesubmit.py?id=%s' ><img src='../img/trash.png' width='25px'></a></p>" % id
        print u"<p><font size='5' color='#ffdb1e'>作成者: %s</font></p>"%auther
        print u"<p>日程1: %s月%s日</p><p>日程2: %s月%s日</p><p>日程3: %s月%s日</p><p>日程4: %s月%s日</p><p>日程5: %s月%s日</p>"%(L2[0],L2[1],L2[2],L2[3],L2[4],L2[5],L2[6],L2[7],L2[8],L2[9])

print u"<hr><font size='4' color='#ff33cc'>参加者一覧</font><br><br>"

names = db.execute('select * from NAME where Top_id = %s ' % id )
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
    print u"<p>参加者: <font size='4' color='#339999'>%s</font> (コメント: <font size='4' color='#339999'>%s</font>)</font>"%(name,comment)
    print u"&nbsp; <a href='Addform.py?id=%s'><img src='../img/edit.png' width='25px'></a>" % nameid
    print "<a href='Adddeletesubmit.py?id=%s&Top_id=%s'><img src='../img/trash.png' width='25px'></a></p>" % (nameid,Top_id)
    if date1 ==0:
        date1 =u"<font color='#ff0066' size='4'>×</font>"
    if date1==1:
        date1=u"<font color='#ccff33'>△</font>"
    if date1==3:
        date1=u"<font color='#0066ff' size='4'>○</font>"
    if date2 ==0:
        date2 =u"<font color='#ff0066' size='4'>×</font>"
    if date2==1:
        date2=u"<font color='#ccff33'>△</font>"
    if date2==3:
        date2=u"<font color='#0066ff' size='4'>○</font>"
    if date3 ==0:
        date3 =u"<font color='#ff0066' size='4'>×</font>"
    if date3==1:
        date3=u"<font color='#ccff33'>△</font>"
    if date3==3:
        date3=u"<font color='#0066ff' size='4'>○</font>"
    if date4 ==0:
        date4 =u"<font color='#ff0066' size='4'>×</font>"
    if date4==1:
        date4=u"<font color='#ccff33'>△</font>"
    if date4==3:
        date4=u"<font color='#0066ff' size='4'>○</font>"
    if date5 ==0:
        date5 =u"<font color='#ff0066' size='4'>×</font>"
    if date5==1:
        date5=u"<font color='#ccff33'>△</font>"
    if date5==3:
        date5=u"<font color='#0066ff' size='4'>○</font>"
    print u" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 日程1: %s 日程2: %s 日程3: %s 日程4: %s 日程5: %s "%(date1,date2,date3,date4,date5)
    print "<br><br>"
print u"<p>%s<a href='Addform.py?Top_id=%s '><button type='button' class='btn btn-sm btn-info'>参加</button></a></p>" % ('&nbsp;' * 8, id)
print u"<hr><p>最適な日程を計算します。</p>"
print u"<p>%s<a href='countform.py?Top_id=%s '><button type='button' class='btn btn-lg btn-danger'>計算</button></a></p>" % ('&nbsp;' * 7,id)
print u"<p><a href='list.py'>戻る</a></p>"
print'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>'
print'<script src="../js/bootstrap.min.js"></script>'
print '</body></html>'

