#!/usr/bin/env python3

from place_class import*
from http.cookies import*

import cgi
import cgitb
import sqlite3
import smtplib
from random import*
import os

ck=SimpleCookie();

path="/var/www/html/plac_1.db"
try:

 print("content-type:text/html\n\n");
 html9='''
  <html>
 
 <body onload="window.location='../manager/place_manager_comdet.py'">
 
 </body>
 
 </html>'''
 
 html1='''
  <html>
 
 <body onload="window.location='../manager/place_manager.py'">
 
 </body>
 
 </html>'''
 

 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 if 'HTTP_COOKIE' in os.environ:
   cookie_string=os.environ.get('HTTP_COOKIE')
   ck.load(cookie_string)
  
   if  'manager' in cookie_string: 
    manager=ck['manager'].value;
  
   else: 
    print(html1);
   
 else:
  manager="";
  print(html1);
  
 html='''
  <html>
  <head>
  <title>Search Company</title>
  </head>
  <body>
  <form>
  <br>
  <input type="text" name="cname" placeholder="Enter Name">
  <input type="submit" name="sub" value="Submit">
  '''
  
 cname=form.getvalue('cname');
  
 print(html);
 
 if "sub" in form:
 
  a='''select c_name,key1_email from com_initial where pwd!="None"  and c_name like "%'''+cname+'''%";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  drop="<select name='cid'>";
  item3="<option value='";
  item4=">";
  item5="</option>"

  for i in data:
   drop=drop+item3+i[1]+"'"+item4+i[0]+"  "+i[1]+item5;

     
  drop=drop+"</select>"
    
  h='''
   '''+drop+'''
   <br>
   <input type="submit" name="sub2" value="Search">
   </form>
   </body>
   </html>'''
   
  print(h); 
    
 elif "sub2" in form:
 
  cid=form.getvalue('cid');
  
  ck['cid']=cid;
  print(ck.js_output());
  print(html9);
  
except:

 cgitb.handler();  
  
