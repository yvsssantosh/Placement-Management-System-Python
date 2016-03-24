#!/usr/bin/env python3

from place_class import*
from http.cookies import*

import cgi
import cgitb
import sqlite3
import smtplib
from random import*
import os

ck=SimpleCookie();

path="/var/www/html/plac_1.db"
try:

 print("content-type:text/html\n\n");
 
 html9='''
  <html>
 
 <body onload="window.location='../admin/place_adm_comdet.py'">
 
 </body>
 
 </html>'''
 
 html1='''
  <html>
 
 <body onload="window.location='../admin/place_adm_log.py'">
 
 </body>
 
 </html>'''
 

 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 if 'HTTP_COOKIE' in os.environ:
   cookie_string=os.environ.get('HTTP_COOKIE')
   ck.load(cookie_string)
  
   if  'admin' in cookie_string: 
    username=ck['admin'].value;
  
   else: 
    print(html1);
   
 else:
  cid="";
  print(html1);
  
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
      
            
     <span id = "letters"><a href="../admin/place_adm_home.py"><span class = "back">Back</span></a></span>
 </br>
  <body>
  <form>
  <br>
  <p align = "center">
  <input class = "submit"  type="text" name="cname" placeholder="Enter Name">
  <input class = "submit"  type="submit" name="sub" value="Submit">
  </p>
  '''
  
 cname=form.getvalue('cname');
  
 print(html);
 
 if "sub" in form:
 
  a='''select c_name,key1_email from com_initial where c_name like "%'''+cname+'''%";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data)==0):
  
   print("<br><h3 align = 'center' >NO DATA FOUND</h3>");
   
  else:
  
   drop="<br><p align = 'center'><select name='cid'>";
   item3="<option value='";
   item4=">";
   item5="</option>"

   for i in data:
    drop=drop+item3+i[1]+"'"+item4+i[0]+"  "+i[1]+item5;

     
   drop=drop+"</select></p>"
    
   h='''
   '''+drop+'''
   <br>
   <p align = "center">
   <input class ="submit" type="submit" name="sub2" value="Search">
   </p>
   </form>
   </body>
   </html>'''
   
   print(h); 
    
 elif "sub2" in form:
 
  cid=form.getvalue('cid');
  
  
  ck['cid']=cid;
  print(ck.js_output());
  print(html9);
  
except:

 cgitb.handler();  
  
