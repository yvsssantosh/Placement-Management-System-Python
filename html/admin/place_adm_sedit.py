#!/usr/bin/env python3

from place_class import*
import os
import cgi
import cgitb
import sqlite3
from http.cookies import*


path="/var/www/html/plac_1.db"

try:
 ck=SimpleCookie() 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 print("content-type:text/html\n\n");
 
 html1='''
  <html>
 
 <body onload="window.location='../admin/place_adm_ms.py'">
 
 </body>
 
 </html>''' 
 
 html9='''
  <html>
 <head>
 <title>Update Staff</title>
 </head>
 
 <body>
 
 <h3>
 No Profile Or Profile Not Updated</h3>
 
 <br>
 
 <a href="../admin/place_adm_ms.py">GO BACK</a>
 
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
  
 
 a='''select * from pm_info where username="'''+username+'''";'''
 
 cur.execute(a);
 
 data=cur.fetchall();
 for i in data:
  password=i[1];
 if(len(data) == 0):
 
  print(html9); 
 
 else:
  
  print("""
<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<link rel="stylesheet" type="text/css" href= "/CSS/manager_home.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
 <script type="text/javascript" src="date_time.js"></script>
 <link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">
<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/cal.css">

</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = " ../admin/place_adm_home.py">
       
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
<a href = "../admin/place_adm_home.py">
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
 <h5 align = "right"><span id="date_time" ></span>
            <script type="text/javascript">window.onload = date_time('date_time');</script></h5>
            
     <span id = "letters"><a href="../admin/place_adm_ms.py"><span class = "back">Back</span></a></span>
 </br>
  <form>
  <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
  <tr>
  <td>
  New Username:
  </td>
  <td>
  <input class = "submit" type="text" required placeholder="enter new username" name="username">
  </td>
  </tr>
  <tr>
  <td>
  New Password:
  </td>
  <td>
  <input class = "submit" type="text" required placeholder="enter new password" name="password">
  </td>
  </tr>
 </table>
 
  <p align ="center">
  <input class = "submit" type="submit" value="Update" name="sub">
  </p>
 
  </form>
 
 
 
 
 
 </body>
 
 </html>""");
  
  
  usr=form.getvalue('username');
  pwd=form.getvalue('password');
  
  if 'sub' in form:
   a='''update pm_info set username="'''+usr+'''",password="'''+pwd+'''" where username="'''+username+'''" and password="'''+password+'''";'''
   cur.execute(a);
   con.commit();
   print("""
  <html>
  <body>
 
  <h3 align = "center" >
  Username and Password Successfully Updated !</h3>
 
 <br>
 

 </body>
 
 </html>""");
  

 
  
except:
 cgitb.handler();
   
  
 
