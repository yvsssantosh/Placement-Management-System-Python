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
 
 html5='''
  <html>
 
 <body onload="window.location='../manager/place_manager_com_ins.py'">
 
 </body>
 
 </html>'''

 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
 
  if 'comcr' and 'manager' in cookie_string:
   company=ck['comcr'].value;
   
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
 per="";
 
 a='''select * from com_criteria where cid="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 
 for i in data:
 
  cname=i[0];
  sof=i[2];
  blist=i[3];
  slist=i[4];
  per=int(i[5]);
   
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

     <span id = "letters"><a href="../manager/place_manager_accepted.py"><span class = "back">Back</span></a></span>
 </br>
 
 <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 
 <tr>
 <td>
 Salary Offered:
 </td>
 <td>
 '''+sof+'''
 </td>
 </tr>
 
 
 <tr>
 <td>
 Selected Branch:
 </td>
 <td>
 '''+blist+'''
 </td>
 </tr>
 
 
 <tr>
 <td>
 Selected Skills
 </td>
 <td>
 '''+slist+'''
 </td>
 </tr>
 
 <tr>
 <td>
 Percentage Required:
 </td>
 <td>  above 
 '''+str(per)+''' %
 </td>
 </tr>
 
 </table>
 
 <form>
 <br>
 <br>
 <h2 align = "center">Select the no of rounds the company wants to conduct:</h2>
 <p align = "center">
 <select name="nor">
 <option value="1">One</option>
 <option value="2">Two</option>
 <option value="3">Three</option>
 <option value="4">Four</option>
 <option value="5">Five</option>
 </select>
 <input class = "submit" type="submit" name="sub1" value="submit">
 </p>
 </form>
 </body>
 </html>
 '''
 print(html);
 nor=int(form.getvalue("nor",0));

 if "sub1" in form:
  ck['nor']=nor;
  print(ck.js_output());
  print(html5); 
   
 
except:

 cgitb.handler();
 
 
 
