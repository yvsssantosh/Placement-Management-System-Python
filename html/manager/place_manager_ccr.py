#!/usr/bin/env python3

from place_class import*
from http.cookies import*

import cgi
import cgitb
import sqlite3
import smtplib
from random import*

ck=SimpleCookie();

path="/var/www/html/plac_1.db"

try:
 company="";

 newitem=""
 item1="<tr ><td><br>"
 item2="</td></tr>"
 drop="<form>";
 drop="<select name='company'>";
 item3="<option value='";
 item4=">";
 item5="</option>"
  
 print("content-type:text/html\n\n");

 html="""
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
            <span id = "letters"><a href="../manager/place_manager_home"><span class = "back">Back</span></a></span>
 </br>
 
<br>

<h1 align="center">
Check Eligible Students For These Company Based On Their Criteria Given
</h1>

</br>
</br>
<br>
 <br>
 
 </body>
 </html>
"""
 html4='''
 <br>
 <br>
 <p align = "center">
 <input class = "submit" type="submit" name="sub" value="Check Details">
 </p>
 <br>
 <br>
 </form>
 </body>
 </html>'''
 
 html1='''
  <html>
 
 <body onload="window.location='../manager/place_manager.py'">
 
 </body>
 
 </html>'''
 
 html9="""
 <html>
 <body onload="window.location='../manager/place_manager_semail.py'">
 </body>
 </html>"""
 
 nocontent='''
 
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
            <span id = "letters"><a href="../manager/place_manager_home"><span class = "back">Back</span></a></span>
 </br>
 
 <br>
 
 <h1 align="center">
 
 You Have No Notification Pending!!
 
 <br>
 <br>
 
 </body>
 </html>'''
 
 
 
 
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 cur.execute("select * from pm_log");
 
 data=cur.fetchall();
 
 if(len(data) == 0):
 
  print(html1);

 
 cur.execute("select * from com_criteria;");
 
 data=cur.fetchall();
 
 if(len(data) == 0):
 
  print(nocontent);
  
 else:
 
  newitem=""
  item1="<tr ><td><br>"
  item2="</td></tr>";
  
  
  for i in data:
  
   name=i[0];
   
   name=name.upper();
  
   newitem=newitem+item1+name+item2;
    
  newitem=newitem+"</table><br><br><br><br>";
  
  drop="<form>";
  drop=drop+'''<select name='company'>''';
  item3="<option value='";
  item4=">";
  item5="</option>"

  for i in data:
  
   name=i[0];
   
   name=name.upper();
   
   drop=drop+item3+i[1]+"'"+item4+name+item5;
   
  drop=drop+"</select>";
  
  html6='''<h4 align = "center" >Select the Company to Get the Information<br><br>''';
 
  htmlformat=html+html6+drop+html4;
 
  print(htmlformat);
  
  company=form.getvalue('company');
  
  if "sub" in form:
   
   ck['comccr']=company;
  
   print(ck.js_output());
  
   print(html9);
     
except:

 cgitb.handler();
