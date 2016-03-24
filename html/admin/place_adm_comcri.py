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
ck=SimpleCookie();
try:
 cname=""; 
 cid="";
 print("content-type:text/html\n\n");

 html15='''
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
 <h5 align = "right" ><span id="date_time" ></span>
            <script type="text/javascript">window.onload = date_time('date_time');</script></h5>
            
            
             <span id = "letters"><a href="../admin/place_adm_comdet.py"><span class = "back">Back</span></a></span>
            
 </br>
 
 <h3 align = "center">
 KMIT Is Yet to Recieve A Recruitment Criteria From This Company

 </h3>
 <br>
 </body>
 </html>'''  
 
 html1='''
  <html>
 
 <body onload="window.location='../manager/place_manager_comdet.py'">
 
 </body>
 
 </html>'''
 
 html5='''
  <html>
 
 <body onload="window.location='../manager/place_manager_com_ins.py'">
 
 </body>
 
 </html>'''

  
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 sof="";
 blist="";
 slist="";
 per="";
 
 if 'HTTP_COOKIE' in os.environ:
   cookie_string=os.environ.get('HTTP_COOKIE')
   ck.load(cookie_string)
  
   if  'admin' and 'cid' in cookie_string: 
    username=ck['admin'].value;
    cid=ck['cid'].value;
    
   else: 
    username="";
    cid="";
    print(html1);
   
 else:
  username="";
  cid=""
  print(html1);
  
 
 
 
 a='''select * from com_criteria where cid="'''+cid+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data)==0):
 
  print(html15);
  
 else:
  
  for i in data:
 
   cname=i[0];
   sof=i[2];
   blist=i[3];
   slist=i[4];
   per=int(i[5])
   
  html='''
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
            
            <span id = "letters"><a href="../admin/place_adm_comdet.py"><span class = "back">Back</span></a></span>

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
 <td> above 
 '''+str(per)+'''%
 </td>
 </tr>
 
 </table>
 
 <form>

<p align = "center"> <input class = "negate" type="submit" name="sub1" value="Delete Criteria"></p>
 <p align = "center">Deleting Crteria Will Allow The Company to Set A New Criteria</p>  
 </form>
 </body>
 </html>
 '''
  print(html);
 

 if "sub1" in form:
  
  a='''delete from com_criteria where cid="'''+cid+'''";'''
  cur.execute(a);
  
  a='''delete from com_date where cid="'''+cid+'''";'''
  
  cur.execute(a);
  
  a='''delete from stu_placed where cid="'''+cid+'''";'''
  
  cur.execute(a);
  
  con.commit();
  
  print("""
  <html>
  <body onload="window.location='../admin/place_adm_dpage.py'">
  </body>
  </html>""");
 
except:

 cgitb.handler();
 
 
 
