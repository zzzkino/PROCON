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

id = form.getvalue('id','')
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

print "<form method='post' action='Topformsubmit.py'>"
print "<p><input type=hidden name=id value='%s'></p>" % id
print u"<p><font color='#ff33cc'>スケジュール名</font> : <input type=text name=title size='32' maxlength='32' value='%s'></p>" % title
print u"<p><font color='#ff33cc'>作成者</font> : <input type=text name=auther size='16' maxlength='32' value='%s'></p>" % auther
print u"<p>日程1: <select name=Mon1>"
print "<option value='0' %s>-</option>" % ('selected' if Mon1 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Mon1 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Mon1 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Mon1 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Mon1 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Mon1 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Mon1 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Mon1 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Mon1 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Mon1 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Mon1 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Mon1 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Mon1 == 12 else '')
print u'</select>月'
print "<select name=Day1>"
print "<option value='0' %s>-</option>" % ('selected' if Day1 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Day1 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Day1 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Day1 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Day1 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Day1 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Day1 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Day1 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Day1 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Day1 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Day1 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Day1 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Day1 == 12 else '')
print "<option value='13' %s>13</option>" % ('selected' if Day1 == 13 else '')
print "<option value='14' %s>14</option>" % ('selected' if Day1 == 14 else '')
print "<option value='15' %s>15</option>" % ('selected' if Day1 == 15 else '')
print "<option value='16' %s>16</option>" % ('selected' if Day1 == 16 else '')
print "<option value='17' %s>17</option>" % ('selected' if Day1 == 17 else '')
print "<option value='18' %s>18</option>" % ('selected' if Day1 == 18 else '')
print "<option value='19' %s>19</option>" % ('selected' if Day1 == 19 else '')
print "<option value='20' %s>20</option>" % ('selected' if Day1 == 20 else '')
print "<option value='21' %s>21</option>" % ('selected' if Day1 == 21 else '')
print "<option value='22' %s>22</option>" % ('selected' if Day1 == 22 else '')
print "<option value='23' %s>23</option>" % ('selected' if Day1 == 23 else '')
print "<option value='24' %s>24</option>" % ('selected' if Day1 == 24 else '')
print "<option value='25' %s>25</option>" % ('selected' if Day1 == 25 else '')
print "<option value='26' %s>26</option>" % ('selected' if Day1 == 26 else '')
print "<option value='27' %s>27</option>" % ('selected' if Day1 == 27 else '')
print "<option value='28' %s>28</option>" % ('selected' if Day1 == 28 else '')
print "<option value='29' %s>29</option>" % ('selected' if Day1 == 29 else '')
print "<option value='30' %s>30</option>" % ('selected' if Day1 == 30 else '')
print "<option value='31' %s>31</option>" % ('selected' if Day1 == 31 else '')
print u'</select>日</p>'

print u"<p>日程2: <select name=Mon2>"
print "<option value='0' %s>-</option>" % ('selected' if Mon2 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Mon2 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Mon2 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Mon2 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Mon2 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Mon2 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Mon2 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Mon2 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Mon2 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Mon2 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Mon2 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Mon2 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Mon2 == 12 else '')
print u'</select>月'
print "<select name=Day2>"
print "<option value='0' %s>-</option>" % ('selected' if Day1 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Day2 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Day2 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Day2 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Day2 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Day2 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Day2 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Day2 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Day2 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Day2 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Day2 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Day2 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Day2 == 12 else '')
print "<option value='13' %s>13</option>" % ('selected' if Day2 == 13 else '')
print "<option value='14' %s>14</option>" % ('selected' if Day2 == 14 else '')
print "<option value='15' %s>15</option>" % ('selected' if Day2 == 15 else '')
print "<option value='16' %s>16</option>" % ('selected' if Day2 == 16 else '')
print "<option value='17' %s>17</option>" % ('selected' if Day2 == 17 else '')
print "<option value='18' %s>18</option>" % ('selected' if Day2 == 18 else '')
print "<option value='19' %s>19</option>" % ('selected' if Day2 == 19 else '')
print "<option value='20' %s>20</option>" % ('selected' if Day2 == 20 else '')
print "<option value='21' %s>21</option>" % ('selected' if Day2 == 21 else '')
print "<option value='22' %s>22</option>" % ('selected' if Day2 == 22 else '')
print "<option value='23' %s>23</option>" % ('selected' if Day2 == 23 else '')
print "<option value='24' %s>24</option>" % ('selected' if Day2 == 24 else '')
print "<option value='25' %s>25</option>" % ('selected' if Day2 == 25 else '')
print "<option value='26' %s>26</option>" % ('selected' if Day2 == 26 else '')
print "<option value='27' %s>27</option>" % ('selected' if Day2 == 27 else '')
print "<option value='28' %s>28</option>" % ('selected' if Day2 == 28 else '')
print "<option value='29' %s>29</option>" % ('selected' if Day2 == 29 else '')
print "<option value='30' %s>30</option>" % ('selected' if Day2 == 30 else '')
print "<option value='31' %s>31</option>" % ('selected' if Day2 == 31 else '')
print u'</select>日</p>'
print u"<p>日程3: <select name=Mon3>"
print "<option value='0' %s>-</option>" % ('selected' if Mon3 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Mon3 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Mon3 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Mon3 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Mon3 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Mon3 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Mon3 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Mon3 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Mon3 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Mon3 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Mon3 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Mon3 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Mon3 == 12 else '')
print u'</select>月'
print "<select name=Day3>"
print "<option value='0' %s>-</option>" % ('selected' if Day3 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Day3 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Day3 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Day3 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Day3 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Day3 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Day3 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Day3 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Day3 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Day3 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Day3 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Day3 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Day3 == 12 else '')
print "<option value='13' %s>13</option>" % ('selected' if Day3 == 13 else '')
print "<option value='14' %s>14</option>" % ('selected' if Day3 == 14 else '')
print "<option value='15' %s>15</option>" % ('selected' if Day3 == 15 else '')
print "<option value='16' %s>16</option>" % ('selected' if Day3 == 16 else '')
print "<option value='17' %s>17</option>" % ('selected' if Day3 == 17 else '')
print "<option value='18' %s>18</option>" % ('selected' if Day3 == 18 else '')
print "<option value='19' %s>19</option>" % ('selected' if Day3 == 19 else '')
print "<option value='20' %s>20</option>" % ('selected' if Day3 == 20 else '')
print "<option value='21' %s>21</option>" % ('selected' if Day3 == 21 else '')
print "<option value='22' %s>22</option>" % ('selected' if Day3 == 22 else '')
print "<option value='23' %s>23</option>" % ('selected' if Day3 == 23 else '')
print "<option value='24' %s>24</option>" % ('selected' if Day3 == 24 else '')
print "<option value='25' %s>25</option>" % ('selected' if Day3 == 25 else '')
print "<option value='26' %s>26</option>" % ('selected' if Day3 == 26 else '')
print "<option value='27' %s>27</option>" % ('selected' if Day3 == 27 else '')
print "<option value='28' %s>28</option>" % ('selected' if Day3 == 28 else '')
print "<option value='29' %s>29</option>" % ('selected' if Day3 == 29 else '')
print "<option value='30' %s>30</option>" % ('selected' if Day3 == 30 else '')
print "<option value='31' %s>31</option>" % ('selected' if Day3 == 31 else '')
print u'</select>日</p>'
print u"<p>日程4: <select name=Mon4>"
print "<option value='0' %s>-</option>" % ('selected' if Mon4 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Mon4 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Mon4 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Mon4 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Mon4 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Mon4 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Mon4 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Mon4 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Mon4 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Mon4 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Mon4 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Mon4 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Mon4 == 12 else '')
print u'</select>月'
print "<select name=Day4>"
print "<option value='0' %s>-</option>" % ('selected' if Day4 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Day4 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Day4 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Day4 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Day4 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Day4 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Day4 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Day4 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Day4 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Day4 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Day4 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Day4 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Day4 == 12 else '')
print "<option value='13' %s>13</option>" % ('selected' if Day4 == 13 else '')
print "<option value='14' %s>14</option>" % ('selected' if Day4 == 14 else '')
print "<option value='15' %s>15</option>" % ('selected' if Day4 == 15 else '')
print "<option value='16' %s>16</option>" % ('selected' if Day4 == 16 else '')
print "<option value='17' %s>17</option>" % ('selected' if Day4 == 17 else '')
print "<option value='18' %s>18</option>" % ('selected' if Day4 == 18 else '')
print "<option value='19' %s>19</option>" % ('selected' if Day4 == 19 else '')
print "<option value='20' %s>20</option>" % ('selected' if Day4 == 20 else '')
print "<option value='21' %s>21</option>" % ('selected' if Day4 == 21 else '')
print "<option value='22' %s>22</option>" % ('selected' if Day4 == 22 else '')
print "<option value='23' %s>23</option>" % ('selected' if Day4 == 23 else '')
print "<option value='24' %s>24</option>" % ('selected' if Day4 == 24 else '')
print "<option value='25' %s>25</option>" % ('selected' if Day4 == 25 else '')
print "<option value='26' %s>26</option>" % ('selected' if Day4 == 26 else '')
print "<option value='27' %s>27</option>" % ('selected' if Day4 == 27 else '')
print "<option value='28' %s>28</option>" % ('selected' if Day4 == 28 else '')
print "<option value='29' %s>29</option>" % ('selected' if Day4 == 29 else '')
print "<option value='30' %s>30</option>" % ('selected' if Day4 == 30 else '')
print "<option value='31' %s>31</option>" % ('selected' if Day4 == 31 else '')
print u'</select>日</p>'
print u"<p>日程5: <select name=Mon5>"
print "<option value='0' %s>-</option>" % ('selected' if Mon5 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Mon5 == 4 else '')
print "<option value='2' %s>2</option>" % ('selected' if Mon5 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Mon5 == 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Mon5 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Mon5 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Mon5 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Mon5 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Mon5 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Mon5 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Mon5 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Mon5 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Mon5 == 12 else '')
print u'</select>月'
print "<select name=Day5>"
print "<option value='0' %s>-</option>" % ('selected' if Day5 == 0 else '')
print "<option value='1' %s>1</option>" % ('selected' if Day5 == 1 else '')
print "<option value='2' %s>2</option>" % ('selected' if Day5 == 2 else '')
print "<option value='3' %s>3</option>" % ('selected' if Day5== 3 else '')
print "<option value='4' %s>4</option>" % ('selected' if Day5 == 4 else '')
print "<option value='5' %s>5</option>" % ('selected' if Day5 == 5 else '')
print "<option value='6' %s>6</option>" % ('selected' if Day5 == 6 else '')
print "<option value='7' %s>7</option>" % ('selected' if Day5 == 7 else '')
print "<option value='8' %s>8</option>" % ('selected' if Day5 == 8 else '')
print "<option value='9' %s>9</option>" % ('selected' if Day5 == 9 else '')
print "<option value='10' %s>10</option>" % ('selected' if Day5 == 10 else '')
print "<option value='11' %s>11</option>" % ('selected' if Day5 == 11 else '')
print "<option value='12' %s>12</option>" % ('selected' if Day5 == 12 else '')
print "<option value='13' %s>13</option>" % ('selected' if Day5 == 13 else '')
print "<option value='14' %s>14</option>" % ('selected' if Day5 == 14 else '')
print "<option value='15' %s>15</option>" % ('selected' if Day5 == 15 else '')
print "<option value='16' %s>16</option>" % ('selected' if Day5 == 16 else '')
print "<option value='17' %s>17</option>" % ('selected' if Day5 == 17 else '')
print "<option value='18' %s>18</option>" % ('selected' if Day5 == 18 else '')
print "<option value='19' %s>19</option>" % ('selected' if Day5 == 19 else '')
print "<option value='20' %s>20</option>" % ('selected' if Day5 == 20 else '')
print "<option value='21' %s>21</option>" % ('selected' if Day5 == 21 else '')
print "<option value='22' %s>22</option>" % ('selected' if Day5 == 22 else '')
print "<option value='23' %s>23</option>" % ('selected' if Day5 == 23 else '')
print "<option value='24' %s>24</option>" % ('selected' if Day5 == 24 else '')
print "<option value='25' %s>25</option>" % ('selected' if Day5 == 25 else '')
print "<option value='26' %s>26</option>" % ('selected' if Day5 == 26 else '')
print "<option value='27' %s>27</option>" % ('selected' if Day5 == 27 else '')
print "<option value='28' %s>28</option>" % ('selected' if Day5 == 28 else '')
print "<option value='29' %s>29</option>" % ('selected' if Day5 == 29 else '')
print "<option value='30' %s>30</option>" % ('selected' if Day5 == 30 else '')
print "<option value='31' %s>31</option>" % ('selected' if Day5 == 31 else '')
print u'</select>日</p>'
print "<br><p><input type='submit' value='send'></p>"
print "</form>"
print u"<br><p><a href='list.py'>戻る</a></p>"
print'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>'
print'<script src="../js/bootstrap.min.js"></script>'
print '</body></html>'
