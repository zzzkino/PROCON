#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

import sqlite3
db = sqlite3.connect('todo.db')

id = form.getvalue('id')
Top_id = form.getvalue('Top_id')

sql = "delete from NAME where id = %s" % id
cursor = db.cursor()
cursor.execute(sql)

db.commit()
db.close()

print "Content-type: text/html\n"
print "<meta http-equiv='refresh' content='0;URL=http://localhost:8000/cgi-bin/titleform.py?id=%s'>"%Top_id
# print "HTTP/1.1 301 Moved Permanently"
# print 'Location: http://localhost:8000/cgi-bin/titleform.py?id=%s'%Top_id