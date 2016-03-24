#!/usr/bin/env python3

from g import *
from place_class import*
from http.cookies import*
import os
import cgi
import cgitb
import sqlite3
import smtplib
from random import*

path="/var/www/html/plac_1.db"

l=[];
try:
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check();
 
 print("content-type:text/html\n\n");
 
 html1='''
  <html>
 
 <body onload="window.location='../student/place_stu_log.py'">
 
 </body>
 
 </html>'''
 
 html2='''
  <html>
 
 <body onload="window.location='../student/place_stu_pro.py'">
 
 </body>
 
 </html>'''
 
 html4='''
 <tr>
<td colspan="2" align="center">
------------------------------------------
</td
</tr>
   <tr>
    <td colspan='2' align = "center">
    <strong>
    SKILLS:</strong>
     </td>
     </tr>
      <tr>
      <td><ul>'''
      
 html5='''
 
 </table>

 </body>
 </html>'''
 
 

 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
  
  if 'username' in cookie_string: 
   username=ck['username'].value;
  
  else: 
   print(html1);
   
 else:
  username="";
  print(html1);
  
 
 a='''select * from stu_skills where stu_id="'''+username+'''";'''
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data) == 0):
 
  print(html2);
 
 else:
 
  
  
  b='''select * from stu_info where stu_id="'''+username+'''";'''
  
  cur.execute(b);
  
  data2=cur.fetchall();
  
  for v in data2:
  
   barchart([1,2,3,4,5,6,7,8,9,10],[v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13]],username,10);
   
   break;
   
  count=1;
  
  for j in data:
  
   while(count<=10):
   
    if(j[count]==1):
     
     if(count == 1):
    
      l.append("C/C++");
      
     if(count == 2):
    
      l.append("Data Structures");
      
     if(count == 3):
    
      l.append("Java");
     
     if(count == 4):
    
      l.append("Python");
      
     if(count == 5):
    
      l.append("HTML/CSS");
      
     if(count == 6):
    
      l.append("Oracle");
      
     if(count == 7):
    
      l.append("SQL");
      
     if(count == 8):
    
      l.append("Jquery");
      
     if(count == 9):
    
      l.append(".NET");
      
     if(count == 10):
    
      l.append("Networks");
     
    count=count+1; 
    
  
  for i in data2:
  
   html3='''
      <html>
     
<head>
<title> KMIT - Recruitment - Admin</title>
<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">

 <script type="text/javascript" src="date_time.js"></script>

</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = " ../place_home.py">
       
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
<a href = "../place_home">
<span>
Home </span></a></td>
<td>
</td>
<td> | </td>
<td></td>
<td id = "about" >
<a href = "http://www.kmit.in/aboutus">
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
 <h5 align = "right"><span id="date_time" ></span>
            <script type="text/javascript">window.onload = date_time('date_time');</script></h5>
            
            
            <span id = "letters"><a href="../student/place_stu_home"><span class = "back">Back</span></a></span>
 </br>

     

     
 <table align="center" bgcolor="#f4f4f4" style = "margin-top:7%;padding:3% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 <tr><td colspan = '2' align= "center"><strong>
 
 DETAILS</strong></td>
 </tr>
 
 
 <tr>
 <td>
 Roll no:
 </td>
 <td>
 '''+i[0]+'''
 </td>
 </tr>
 
 <tr>
 <td>
 Name:
 </td>
 <td>
 '''+i[1]+'''
 </td>
 </tr>
 
 <tr>
 <td>
 Gender:
 </td>
 <td>
 '''+i[2]+'''
 </td>
 </tr>
 
 <tr>
 <td>
DOB:
 </td>
 <td>
 '''+i[18]+'''
 </td>
 </tr>
 
 <tr>
 <td>
 Age:
 </td>
 <td>
 '''+str(i[17])+'''
 </td>
 </tr>
 
 <tr>
 <td>
 Branch:
 </td>
 <td>
 '''+i[3]+'''
 </td>
 </tr>
 
 <tr>
 <td>
 Mobile no:
 </td>
 <td>
 '''+i[14]+'''
 </td>
 </tr>
 
 <tr>
 <td>
E-mail:
 </td>
 <td>
 '''+i[15]+'''
 </td>
 </tr>'''
 
 
  for k in l:
   
   html4=html4+"<li>"+k+"</li>";
   
  html4=html4+"</td>"+"</tr>";
  
  
  
  html6='''
  
  <div id = "header">
  <h2 align = "center"> Your Statistics</h2>
  <img align="right"  src ="../student/graphs/'''+username+'''.png"/>
  </div>'''
  
  htmlformat=html3+html4+html6+html5;
  
  
  
  print(htmlformat);
  
except:

 cgitb.handler();
 
    
