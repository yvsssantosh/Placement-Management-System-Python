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
 
 <body onload="window.location='../company/place_com_log.py'">
 
 </body>
 
 </html>'''
 
 html2='''
  <html>
 
 <body onload="window.location='../company/place_com_criteria.py'">
 
 </body>
 
 </html>'''
 

 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
 
  if 'company' in cookie_string:
   company=ck['company'].value;
   
  else:
   print(html1);
   
 else:
  company="";
  
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 sof="";
 blist="";
 slist="";
 
 a='''select * from com_criteria where cid="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data)==0):
  print(html2);
 
 for i in data:
 
  cname=i[0];
  sof=i[2];
  blist=i[3];
  slist=i[4];

   
 html='''
<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">


 <script type="text/javascript" src="date_time.js"></script>


</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = "../company/place_com_home.py">
       
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
<a href = "../company/place_com_home.py">
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
             <span id = "letters"><a href="../company/place_com_home"><span class = "back">Back</span></a></span>
 </br>
   <table align="center" bgcolor="#f4f4f4" style = "padding:3% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 
 <tr>
 <td>
 <br>
 Salary Offered
 </td><td></br>:</td>
 <td><br>
 '''+sof+'''
 </td>
 </tr>
 
 
 <tr>
 <td><br>
 Selected Branch

 </td><td></br>:</td>
 <td><br>
 '''+blist+'''
 </td>
 </tr>
 
 
 <tr>
 <td>
 <br>
 Selected Skills
 </td><td></br>:</td>
 <td><br>
 '''+slist+'''
 </td>
 </tr>
 
 </table>
 
 </body>
 </html>'''
 
 print(html);
 
except:

 cgitb.handler();
 
 
 
