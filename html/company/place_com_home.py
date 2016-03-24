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
 
 <body onload="window.location='../company/place_com_log.py'">
 
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
  print(html1);
  
 
 #print("content-type:text/html"); 
 
 a='''select c_name from com_initial where key1_email="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 for m in data:
 
  cname1=m[0];
  break;
  
  
 html="""
 
 
<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<link rel="stylesheet" type="text/css" href= "/CSS/manager_home.css">
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
<form>
<input class="submit" type="submit" value="Logout" name="log">
</form>
logged in as """+cname1.upper()+"""
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
 </br>
<br>
<br>
<br>


<p  style = "position:absolute;left:60px;"><a href='../company/place_com_criteria.py' class = "badge1" ><span class = "buttons"> Add Criteria </span></a></p>
</br>

<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../company/place_com_vcr.py' ><span class = "buttons">View Criteria </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../company/place_com_cpas.py' ><span class = "buttons">Change Password </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>
</br>
</br>
</br>
</br>


</body>





</html>"""

 print(html);
 
 if "log" in form:
 
  ck['company']['expires']=0;
  print(ck.js_output());
  print(html1);

except:

 cgitb.handler();
