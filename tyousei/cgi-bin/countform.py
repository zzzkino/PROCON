#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()

print "Content-type: text/html\n"
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
print "<html><script>function OnlyNumber(evt)"
print"{var evt = evt || window.event;var c = evt.keyCode;"
print"if((48<=c && c<=57) || (96<=c && c<=105) || c==8 || c == 9 || c==32 "
print"|| c == 37 || c == 39 || c == 46 || c == 18 || (112<=c && c<=123) ){return true;}return false;}</script>"
print"<body style='margin:15px;padding:15px;'>"
print'<head>'
print'<meta http-equiv="X-UA-Compatible" content="IE=edge">'
print'<meta name="viewport" content="width=device-width, initial-scale=1">'
print'<link href="../css/bootstrap.min.css" rel="stylesheet">'
print'<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>'
print'<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>'
print'</head>'
print u"<p><FONT color='#00cc00' size='6'><B>&nbsp; &nbsp; &nbsp; &nbsp; ~調整さま~</B></FONT></p>"

import sqlite3
db = sqlite3.connect('todo.db')

Top_id = form.getvalue('Top_id')
rows = db.execute(' select * from Top where id = %s ' % Top_id)
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

print u"<p>最適な日程を計算するために参加者に重要ポイントを付与してください。</p>"
print u"<p><font size='6' color='#6699ff'>タイトル: %s</font></p>"%title
print u"<p><font size='5' color='#ffdb1e'>作成者: %s</font></p>"%auther
names = db.execute('select * from NAME where Top_id = %s ' % Top_id )

print "<form method='post' action='resultform.py'>"
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
    print u"<p><font color='#ff33cc'>参加者</font>: <font size='4' color='#339999'>%s</font> ( コメント: <font size='4' color='#339999'>%s</font> )</font> &nbsp; &nbsp; ポイント&nbsp;<input name=%s size='5' maxlength='5' value='1' class='OnlyNumber' style='text-align: right; ime-mode: disabled;' onkeydown='return OnlyNumber(event)' oncontextmenu='return false;' type='text' placeholder='半角数値'></p>" % (name,comment,nameid)
print "<p><input type=hidden name=Top_id value='%s'></p>" % Top_id
print u"<br><p><input type='submit' value='結果'></p>"
print "</form>"
print u"<br><p><a href='titleform.py?id=%s'>戻る</a></p>"%Top_id
print'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>'
print'<script src="../js/bootstrap.min.js"></script>'
print '</body></html>'
