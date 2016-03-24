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

 def email():
   
  fadr="kmitpython21@gmail.com"
  semail=company;
  tadr=company; 
   
  gpwd=randrange(100000,9999999,1);
  
  gpwd=str(gpwd); 
   
  a='''update com_initial set pwd="'''+gpwd+'''" where key1_email="'''+semail+'''"'''
  
  cur.execute(a);  
    
  con.commit();
       
  msg='''Hello  '''+cname.upper()+'''\n\n\nlogin details:\nUserid:'''+semail+''' \npassword:'''+gpwd+'''\n\nYou may change your password after login\n''';                                                   

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("kmitpython21@gmail.com","kmit@python21");      
  server.sendmail(fadr, tadr, msg)
  server.quit()
  
 def insert():
 
  global key1_email;
  
  for i in data:
    
   if(company == i[5]):
     
    a='''insert into com_initial values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","None");'''%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]);
        
    cur.execute(a);
    
    a='''delete from com_rej where key1_email="'''+i[5]+'''";''';
    
    key1_email=i[5];
    
    cur.execute(a);
      
    con.commit();
   
   
 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
  company=ck['company'].value;
 
 else:
  company="";
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 print("content-type:text/html\n\n");
 
 a='''select * from com_rej;'''
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 for i in data:
 
  d="";
  if(company == i[5]):   
 
   d='''
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
            <span id = "letters"><a href="../manager/place_manager_rejected"><span class = "back">Back</span></a></span>
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
     <tr>
     <td>
     <br>
     Address
     </td>
     <td></br>:</td>
     <td><br>'''+i[1]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Contact Number
     <br>
     </td>
     <td></br>:</td>
     <td><br>'''+i[2]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Website
     </td>
     <td></br>:</td>
     <td><br>'''+i[3]+'''
     </td>
     </tr>
     </table>
     
     <table align="center" bgcolor="#e8e8e8" style = "margin-top:5px;margin-left:20%;display:inline-block;padding:0% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
     <tr>
     <td colspan="3" align="center">
     <br>
     <br><strong>
     Key person1 Details</strong>
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Name
     </td>
     <td></br>:</td>
     <td><br>'''+i[4]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Email Address
     </td>
     <td></br>:</td>
     <td><br>'''+i[5]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Contact Number
     </td>
     <td></br>:</td>
     <td><br>'''+i[6]+'''
     </td>
     </tr>
     </table>
     <table align="center" bgcolor="#e8e8e8" style = "display:inline-block;padding:0% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
     <tr>
     <td colspan="3" align="center">
     <br>
     <br><strong>
     Key person 2 Details</strong>
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Name
     </td>
     <td></br>:</td>
     <td><br>'''+i[7]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Email Address
     </td>
     <td></br>:</td>
     <td><br>'''+i[8]+'''
     </td>
     </tr>
     <tr>
     <td>
     <br>
     Contact Number
     </td>
     <td></br>:</td>
     <td><br>  '''+i[9]+'''
     </td>
     </tr>
     </table>
     <form>
    <h1 align ="center">
    <input class = "accept" type="submit" name="approve" value="Approve"> 
    </h1>
    </form>
    </body>
    </html>'''
   print(d);
     
  
 if "approve" in form:
 
  for i in data:
    
   if(company == i[5]):
    
    cname=i[0]; 
    insert();
    email();
    print("Email successfully sent!!");
    print("<br><a href='../manager/place_manager_review.py'>GO BACK</a>")
    break;


 
 
except:
 cgitb.handler();
