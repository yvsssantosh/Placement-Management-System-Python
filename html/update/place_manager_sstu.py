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
 
 <body onload="window.location='../manager/place_stu_det.py'">
 
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
  <title>Search Student</title>
  </head>
  <body>
  <form>
  <h4>Search By:</h4>
  <br>
  <input type="radio" name="stype" value="name" >Name
  <input type="radio" name="stype" value="id">Roll Number
  <input type="submit" name="sub" value="Submit">
  '''
  
 stype=form.getvalue('stype');
  
 print(html);
 
 if "sub" in form:
 
  if(stype=='id'):
  
   print('''
   <input type="text" name="sid" placeholder="Enter Roll Number">
   <input type="submit" name="sub1" value="Search">
   </form>
   </body>
   </html>''');
   
   sid=form.getvalue('sid');
   
  elif(stype=='name'):
  
   print('''<form>
   <input type="text" name="sname" placeholder="Enter Name">
   <input type="submit" name="sub1" value="Search">
   ''');
   sname=form.getvalue('sname');
  
  else:
  
   pass;
    
 elif 'sub1' in form:
   
   if 'sid' in form:
    sid=form.getvalue('sid');
    
    a='''select * from stu_info where stu_id="'''+sid+'''";'''
    cur.execute(a);
    data=cur.fetchall();
  
    if(len(data)==0):
  
     print("<br><h3>Profile Not Found</h3>");
   
    else:
     ck['sid']=sid;
     print(ck.js_output());
     print(html9);  
    
   elif 'sname' in form:
    
    sname=form.getvalue('sname');
    a='''select stu_id,stu_name,stu_branch from stu_info where stu_name like "%'''+sname  +'''%";'''
    

    cur.execute(a);
    
    data=cur.fetchall();
    
    if(len(data)==0):
    
     print("<br><h3>NO PROFILE FOUND");
     
    else:
    
     drop="<select name='sid'>";
     item3="<option value='";
     item4=">";
     item5="</option>"
    
     for i in data:
      drop=drop+item3+i[0]+"'"+item4+i[0]+"  "+i[1]+" "+i[2]+item5;

     
     drop=drop+"</select>"

     h='''
   '''+drop+'''
   <input type="submit" name="sub2" value="Search">
   </form>
   </body>
   </html>'''
   
     print(h);
   
 elif "sub2"  in form:
  sid=form.getvalue('sid');
  
  a='''select * from stu_info where stu_id="'''+sid+'''";'''
  cur.execute(a);
  data=cur.fetchall();
  
  if(len(data)==0):
  
   print("<br><h3>Profile Not Found</h3>");
   
  else:
   ck['sid']=sid;
   print(ck.js_output());
   print(html9);  
    
  
              
except:

 cgitb.handler();
  
  
