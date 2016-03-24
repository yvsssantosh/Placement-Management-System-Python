#!/usr/bin/env python3

from place_class import*

import cgi
import cgitb
import sqlite3
from http.cookies import *
path="/var/www/html/plac_1.db"

try:
 ck=SimpleCookie();
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 def insert():
 
  cur.execute("insert into pm_log values(datetime('now'));");
  con.commit();
  
   
 print("content-type:text/html");
 
 html="""
  
<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href= "/CSS/style2.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
<link rel="stylesheet" type="text/css" href= "/CSS/table.css">

 <script type="text/javascript" src="date_time.js"></script>


</head>



<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href= "/CSS/style2.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">

<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">
 <script type="text/javascript" src="date_time.js"></script>


</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = "../place_home.py">
       
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
 </br>
 


 <h1 align="center"> <em>Welcome Placement Manager</em> </h1>
 <h1 align = "center" style = "color:"> <strong><em>Login</em></strong> </h1>
 <br>

 <br>
 <form method="post">
 <table  id = "one" align = "center">
 <tr class = "row">
   <td>
   Username:
   </td>
   <td>
   <input type="text" name="usr" value={u} required autofocus>
   </td>
 </tr>
 
 <tr class = "row">
   <td>
   <br>
   Password
   </td>
   <td>
   <br>
   <input type="password" name="pwd" required>
   </td>
 </tr>
 
 
 
 </table>
 <br>
 
 
 <div id = "float1">
 <h3 align = ""><a href = "../place_home.py"><div id = "backbutton" > <p>Back</p></h3> </div></a>
 </div>
 

 
  <div id = "float3">
 <h2 align = "center"><em> <input id = "logbutton" type="submit" name="sub" value="Login"></em></h3>
 </div>
 
 </form>
 </body>
 
 </html>"""
 
 html1="""
 
 <html>
 
 <body onload="window.location='../manager/place_manager_home.py'">
 
 </body>
 
 </html>"""
 
 
 u=form.getvalue("usr","-");
 
 p1=form.getvalue("pwd");
 
 print(html.format(**locals()));
 
 if "sub" in form:
  
  if( (c.pm_id(u,p1)) == 0):
  
 
   insert();
   ck['manager']=u;
   ck['manager']['expires']=1*1*30*60;
   
   print(ck.js_output());
 
   print(html1);
  
except:
 
 cgitb.handler();
 
 
 
   
  
 
 
 
