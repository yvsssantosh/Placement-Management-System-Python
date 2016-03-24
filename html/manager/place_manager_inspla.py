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
  newitem=newitem+'''<br><input class = "submit" type=text placeholder="Enter Student ID"  name="s'''+str(i)   +'''"required><br>'''
  i=i+1;
   
 html='''
  <!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<link rel="stylesheet" type="text/css" href= "/CSS/cal.css">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/manager_home.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">
 <script type="text/javascript" src="date_time.js"></script>


</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = "../manager/place_manager_home.py">
       
       <div class="logop">
       <div class = "inlogop">
       RECRUITMENT
        </div>
         </div>
   </a>
   </td>
      <td align = "right">
      <a href = "http://www.kmit.in"> <img src = "../kmit0.jpg"> </a>
  </td>
 </tr>
</table>
</br>

<!-- navibar Starts here.................................................................................................... -->

<div class = "bar">

<div id = "bar1">
<table>
<tr>
<td id = "home">
<a href = "../manager/place_manager_home.py">
<span>
Home </span></a></td>
<td>
</td>
<td> | </td>
<td></td>
<td id = "about" >
<a href = "http://www.kmit.in/about.html">
<span>
About Us</span> </a></td>
</tr>
</table>
</div>

<div  id = "bar2"  >
<table>
<tr><td id  = "login">

</td>
</tr>
</table>
</div>

</div>

<!-- navibar Ends here.................................................................................................... -->
 

 
 <body>
 
  
 
 <div>
 <h1 align = "center" style = "color: silver"> <em>___________________________________________________________________________________</em></h1>
 </div>
 <h5 align = "right" ><span id="date_time" ></span>
            <script type="text/javascript">window.onload = date_time('date_time');</script></h5>
 </br><br>
       <span id = "letters"><a href="../manager/place_manager_stu_placed.py"><span class = "back">Back</span></a></span>
 </br>
 <h2 align = "center"> Enter All the Students' IDs</h2>
 <br>
 <form>
 <p align = "center">
 '''+newitem+'''
 <br>
 <input class = "submit" type="submit" name='sub2' value="Insert">
 </p>
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
   
    b='''<h2 align = "center">Student'''+k+''' already placed in this company''';
    
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
     a='''<h3 align = 'center'>'''+k+''' has already got Three Offers</h3>'''
     print(a); 
   
   #print(htm);
   
   print("<br><br><h3 align = 'center'>Placement Successfull</h3>");
except:
 cgitb.handler();   
  
