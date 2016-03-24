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
    
 html9='''
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
            
            <span id = "letters"><a href="../admin/place_adm_scom"><span class = "back">Back</span></a></span>

 </br>
 
 <h3 align ="center" >
 No Profile Or Profile Not Updated</h3>
 
 <br>
 
 <a href="../admin/place_adm_scom.py">GO BACK</a>
 
 </body>
 
 </html>'''
 
 html15='''
  <html>
 
 <body onload="window.location='../admin/place_adm_comcri.py'">
 
 </body>
 
 </html>'''
 
 html1='''
  <html>
 
 <body onload="window.location='../admin/place_adm_log.py'">
 
 </body>
 
 </html>'''
 
 html7='''
  <html>
 
 <body onload="window.location='../admin/place_adm_comedit.py'">
 
 </body>
 
 </html>'''
 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  
  if 'cid' and 'admin' in cookie_string:
   ck.load(cookie_string)
   cid=ck['cid'].value;
 
  else:
   print(html1);
   
 else:
  cid="";
  print(html1);
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 print("content-type:text/html\n\n");
 
 a='''select * from com_initial where key1_email="'''+cid+'''";'''
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data)==0):
 
  print(html9);
 
 else:
 
  for i in data:
   d="";
   if(cid == i[5]):  
    d='''
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
            
            
            <span id = "letters"><a href="../admin/place_adm_scom.py"><span class = "back">Back</span></a></span>
 </br>

     
     <h2 align ="center" style = "font-family:sans-serif;" >Details of <em>'''+i[0]+'''</em></h2>
     
    
     <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
     <tr>
     <td>
     <br>
     Name
     </td>
     <td></br>:</td>
     <td><br>'''+i[0]+'''
     </td>
     </tr>
     <tr >
     <td>
     <br>
     Address
     </td><td></br>:</td>
     <td><br>'''+i[1]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Contact Number
     <br>
     </td><td></br>:</td>
     <td><br>'''+i[2]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Website
     </td> <td></br>:</td>
     <td><br>'''+i[3]+'''
     </td>
     </tr>
     </table>
     
     <table align="center" bgcolor="#e8e8e8" style = "margin-top:5px;margin-left:20%;display:inline-block;padding:0% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
     <tr>
     <td colspan="3" align="center">
     <br>
     <br>
     <strong>Key Person 1 Details</strong>
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Name
     </td> <td></br>:</td>
     <td><br>'''+i[4]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Email Address
     </td> <td></br>:</td>
     <td><br>'''+i[5]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Contact Number
     </td> <td></br>:</td>
     <td><br>'''+i[6]+'''
     </td>
     </tr>
     </table>
     <table align="center" bgcolor="#e8e8e8" style = "display:inline-block;padding:0% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
     <tr>
     <td colspan="3" align="center">
     <br>
     <br>
     <strong>Key Person 2 Details</strong>
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Name
     </td> <td></br>:</td>
     <td><br>'''+i[7]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Email Address
     </td> <td></br>:</td>
     <td><br>'''+i[8]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
   Contact Number
     </td> <td></br>:</td>
     <td><br>  '''+i[9]+'''
     </td>
     </tr>
     </table>
     <form>
     <p align = "center">
     <input class="submit" type="submit" value="Edit Details" name="sub">
     <input class="submit" type="submit" value="Edit Criteria" name="sub2">
     </p>
     </form>
    </body>
    </html>'''
   print(d);
 
 if "sub" in form:
 
  ck['cid']=cid;
  print(ck.js_output());
  print(html7);
 
 if "sub2" in form:
  ck['cid']=cid;
  print(ck.js_output());
  print(html15);
   
except:

 cgitb.handler(); 
