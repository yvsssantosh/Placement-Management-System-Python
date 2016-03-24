#!/usr/bin/env python3

from place_class import*
from http.cookies import*

import cgi
import cgitb
import sqlite3
import smtplib
import os
from random import*

ck=SimpleCookie();

path="/var/www/html/plac_1.db"

try:

 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 print("content-type:text/html\n\n");
 
 html1='''
  <html>
 
 <body onload="window.location='../manager/place_manager.py'">
 
 </body>
 
 </html>'''

 htm='''
  <html>
 
 <body onload="window.location='../manager/place_manager_home.py'">
 
 </body>
 
 </html>'''
 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck.load(cookie_string)
  
  if 'manager' and 'nsp' and 'cname' in cookie_string: 
   manager=ck['manager'].value;
   nsp=ck['nsp'].value;
   nsp=int(nsp);
   cname=ck['cname'].value;
  
  else: 
   print(html1);
   
 else:
  manager="";
  nsp=0;
  cname=''
  print(html1);
  
  
 i=1;

 newitem="";
  
 while (i<=nsp):
  newitem=newitem+'''<input type=text placeholder="Enter Student ID"  name="s'''+str(i)   +'''"required><br>'''
  i=i+1;
   
 html='''
 <html>
 <head>
 <title>Insert Placed Students</title>
 </head>
 <body>
 <br>
 <form>
 '''+newitem+'''
 <input type="submit" name='sub2' value="Insert">
 </form>
 </body>
 </html>'''
 
 
 print(html);
 
 i=1;
 l=[];
 
 while(i<=nsp):
  a='''s'''+str(i);
  l.append(form.getvalue(a));
  i=i+1;
  #(a);
    
 if 'sub2' in form:
  
  #print(l);
  
  a='''select sof from com_criteria where cid="'''+cname+'''";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  for k in data:
  
   sof=int(k[0]);
  
  
  for k in l:
  
   a='''select * from stu_placed where stu_id="'''+k+'''" and cid="'''+cname+'''";'''
   
   cur.execute(a);
   
   data=cur.fetchall()
   
   if(len(data)!=0):
   
    b='''<h2>Student'''+k+''' already placed in this company''';
    
    print(b);
    
   else:
   
    a='''insert into stu_placed values("%s","%s");'''%(k,cname);
   
    cur.execute(a);
   
    con.commit()
   
    a='''select noff from stu_info where stu_id="'''+k+'''";''';
   
    cur.execute(a);
   
    data=cur.fetchall();
    
    for u in data:
   
     noff=int(u[0]);
    
   
    
    if(noff==0):
   
     a='''update stu_info set so1="'''+str(sof)+'''",noff=1 where stu_id="'''+k+'''";''';
    
     cur.execute(a);
    
     con.commit();
    
    elif(noff==1):
   
     a='''update stu_info set so2="'''+str(sof)+'''",noff=2 where stu_id="'''+k+'''";''';
    
     cur.execute(a);
    
     con.commit();
    
    elif(noff==2):
   
     a='''update stu_info set so3="'''+str(sof)+'''",noff=3 where stu_id="'''+k+'''";''';
    
     cur.execute(a);
    
     con.commit(); 
    
    else:
     a='''<h3>'''+k+''' has already got Three Offers</h3>'''
     print(a); 
   
   #print(htm);
   
   print("<br><br><h3>Placement Successfull</h3>");
except:
 cgitb.handler();   
  
