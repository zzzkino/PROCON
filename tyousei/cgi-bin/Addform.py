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
print u"<p><FONT color='#00cc00' size='6'><B>&nbsp; ~調整さま~</B></FONT></p>"

import sqlite3
db = sqlite3.connect('todo.db')

id = form.getvalue('id', '')
Top_id = form.getvalue('Top_id')

if id == '':
    name = ''
    comment = ''
    date1 = ''
    date2 = ''
    date3 = ''
    date4 = ''
    date5 = ''
    Top_id = '%s'%Top_id

else:
    rows = db.execute('select * from NAME where id = %s ' % id)
    for row in rows:
        name = row[1]
        comment = row[2]
        date1 = row[3]
        date2 = row[4]
        date3 = row[5]
        date4 = row[6]
        date5 = row[7]
        Top_id = row[8]

Tops = db.execute('select * from Top where id = %s ' %Top_id )
for Top in Tops:
    MON1 = Top[3]
    MON2 = Top[5]
    MON3 = Top[7]
    MON4 = Top[9]
    MON5 = Top[11]
    DAY1 = Top[4]
    DAY2 = Top[6]
    DAY3 = Top[8]
    DAY4 = Top[10]
    DAY5 = Top[12]

L= [MON1, DAY1, MON2, DAY2, MON3, DAY3, MON4, DAY4, MON5, DAY5]
L2 = [x if x != 0 else '-' for x in L]

print "<form method='post' action='Addformsubmit.py'>"
print "<p><input type=hidden name=id value='%s'></p>" % id
print "<p><input type=hidden name=Top_id value='%s'></p>" % Top_id
print u"<p><font color='#6699ff'>名前</font> : <input type=text name=name size='16' maxlength='32' value='%s'></p>" % name
print u"<p><font color='#ff9900'>コメント</font> : <input type=text name=comment size='32' maxlength='32' value='%s'></p>" % comment
print u"<p>%s月%s日 : <select name=date1>"%(L2[0],L2[1])
print "<option value='0' %s>×</option>" % ('selected' if date1 == 0 else '')
print "<option value='1' %s>△</option>" % ('selected' if date1 == 1 else '')
print "<option value='3' %s>○</option>" % ('selected' if date1 == 3 else '')
print '</select></p>'
print u"<p>%s月%s日 : <select name=date2>"%(L2[2],L2[3])
print "<option value='0' %s>×</option>" % ('selected' if date2 == 0 else '')
print "<option value='1' %s>△</option>" % ('selected' if date2 == 1 else '')
print "<option value='3' %s>○</option>" % ('selected' if date2 == 3 else '')
print '</select></p>'
print u"<p>%s月%s日 : <select name=date3>"%(L2[4],L2[5])
print "<option value='0' %s>×</option>" % ('selected' if date3 == 0 else '')
print "<option value='1' %s>△</option>" % ('selected' if date3 == 1 else '')
print "<option value='3' %s>○</option>" % ('selected' if date3 == 3 else '')
print '</select></p>'
print u"<p>%s月%s日 : <select name=date4>"%(L2[6],L2[7])
print "<option value='0' %s>×</option>" % ('selected' if date4 == 0 else '')
print "<option value='1' %s>△</option>" % ('selected' if date4 == 1 else '')
print "<option value='3' %s>○</option>" % ('selected' if date4 == 3 else '')
print '</select></p>'
print u"<p>%s月%s日 : <select name=date5>"%(L2[8],L2[9])
print "<option value='0' %s>×</option>" % ('selected' if date5 == 0 else '')
print "<option value='1' %s>△</option>" % ('selected' if date5 == 1 else '')
print "<option value='3' %s>○</option>" % ('selected' if date5 == 3 else '')
print '</select></p>'
print "<br>"
print "<p><input type='submit' value='send'></p>"
print "</form>"

print u"<br><p><a href='titleform.py?id=%s'>戻る</a></p>"%Top_id
print'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>'
print'<script src="../js/bootstrap.min.js"></script>'
print '</body></html>'
