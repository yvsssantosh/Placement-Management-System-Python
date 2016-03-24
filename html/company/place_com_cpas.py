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
 flag=1;
 
 print("content-type:text/html\n\n");
 
 html1='''
  <html>
 
 <body onload="window.location='../company/place_com_log.py'">
 
 </body>
 
 </html>'''
 
 html3='''
  <html>
 
 <body onload="window.location='../company/place_com_home.py'">
 
 </body>
 
 </html>'''
 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck.load(cookie_string)
  
  if 'company' in cookie_string: 
   username=ck['company'].value;
   
  else:
   username=""; 
   print(html1);
   
 else:
  username="";
 
  print(html1);
 
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
 </br>
 </br>
 <h3 align = "center"> Change Password</h3>
 <table align="center" bgcolor="#f4f4f4" style = "padding:3% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 
 <form method="post">
 
 <tr>
 <td>
 Current Password:
 </td>
 <td>
 <input type="text" name="opas" required autofocus>
 </td>
 </tr>
 
 <tr>
 <td>
 Password:
 </td>
 <td>
 <input type="text" name="npas1" placeholder="Min 6 Char" maxlength="14" required>
 </td>
 </tr>
 
 <tr>
 <td>
 Re-Type Password:
 </td>
 <td>
 <input type="text" name="npas2" placeholder="Min 6 Char" maxlength="14" required >
 </td>
 </tr>
 
 <tr>
 <td>
 <br>
 <br>
 </td>
 <td>
 <br>
 <br>
 <input class="accept" type="submit" name="sub" value="Change Password">
 </td>
 </tr>
 
 </table>
 </form>
 </html>'''
 
 opas=form.getvalue('opas');
 npas1=form.getvalue('npas1');
 npas2=form.getvalue('npas2');
 
 print(html);
 
 if "sub" in form:
 
  c.com_cpas(opas,npas1,npas2,username);
 
  
except:

 cgitb.handler();
