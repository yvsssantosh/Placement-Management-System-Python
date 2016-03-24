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
 
 a="select * from pm_info;"
 cur.execute(a);
 data=cur.fetchall();
 
 if(len(data) == 0):
 
  print(html3);
  pass;
 else:
 
  for i in data:
  
   username=i[0];
   password=i[1];
 
 
 
 
 print("content-type:text/html\n\n");
 print("""
  <!Doctype html>
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
<a href = "../place_home.py">
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
            
     <span id = "letters"><a href=../admin/place_adm_home.py><span class = "back">Back</span></a></span>
 </br>
 <form>
 <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 <tr>
 <td><br>
 Username
 </td>
 <td></br>:</td>
 <td><br><strong>
 
 """+username+"""</strong>
 </td>
 </tr>
 <tr>
 <td><br>
 Password
 </td>
 <td></br>:</td>
 <td><br><strong>
 """+password+"""</strong> </td>
 </tr>
 
 
 
 
 </table>
 <p align = "center">
 <input class = "submit"  type="submit" value="Edit Details" name="sub">
 </p>
 </form>
 <br>
 
 
 </body>
 
 </html>""");
  
 
 html3='''
  <html>
 
 <body onload="window.location='../admin/place_adm_sedit.py'">
 
 </body>
 
 </html>'''
 
 
 if 'sub' in form:
  
  
   ck['username']=username;
   print(ck.js_output());
   print(html3);
  
  
 
 #cur.execute("create table pm_info(username varchar(20) primary key,password varchar(20));");
except:
 cgitb.handler(); 
