#!/usr/bin/env python3

from place_class import*
from http.cookies import*
import os
import cgi
import cgitb
import sqlite3
import smtplib
from random import*

path="/var/www/html/plac_1.db"

try:

 print("content-type:text/html\n\n");

 html1='''
  <html>
 
 <body onload="window.location='../manager/place_manager_comcr.py'">
 
 </body>
 
 </html>'''
 
 html6='''
  <html>
 
 <body onload="window.location='../manager/place_manager_home.py'">
 
 </body>
 
 </html>'''

 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
 
  if 'comcr' in cookie_string:
   company=ck['comcr'].value;
   nor=ck['nor'].value;
   
  else:
   print(html1);
   
 else:
  company="";
  nor=0;
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 a='''select * from com_criteria where cname="'''+company+'''";''';
 
 cur.execute(a);
 
 
 data=cur.fetchall();
 
 for k in data:
 
  cid=k[1];
  break;
  
  
 drop=''
 i=0;
 nor=int(nor);
 while(i<nor):
  drop=drop+'''<select name="op'''+str(i)+'''">''';
  drop=drop+'''<option value="Technical">Technical</option>'''
  drop=drop+'''<option value="Machine">Machine </option>'''
  drop=drop+'''<option value="Aptitude">Aptitude</option>'''
  drop=drop+'''<option value="Online">Online</option>'''
  drop=drop+'''<option value="Other">Other</option>'''
  drop=drop+'''</select> <input type="date" placeholder="Date(dd/mm/yyyy)" name="dat'''+str(i)+'''"><br>'''
  i=i+1;
 
 
 html='''
 <html>
 <head>
 <title>Select Dates</title>
 </head>
 <body>
 <form>
 <h2>Assign Round Dates And Type Of Round</h2>
 <br>
 <br>'''+drop+''' 
 <br>
 <input type="submit" name='sub' value="INSERT"> 
 </form>
 </body>
 </html>'''
 
 print(html);
  
 op0=form.getvalue('op0','none');
 op1=form.getvalue('op1','none');
 op2=form.getvalue('op2','none');
 op3=form.getvalue('op3','none');
 op4=form.getvalue('op4','none');
 dat0=form.getvalue('dat0','none');
 dat1=form.getvalue('dat1','none');
 dat2=form.getvalue('dat2','none');
 dat3=form.getvalue('dat3','none');
 dat4=form.getvalue('dat4','none');
 
 if "sub" in form:
 
  a='''insert into com_date values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'''%(company,cid,dat0,op0,dat1,op1,dat2,op2,dat3,op3,dat4,op4,str(nor));
  
  cur.execute(a);
  
  con.commit();
  
  print("<br><h5>Data Successfully Updates</h5>");
  
  print(html6);
  
except:

 cgitb.handler();
