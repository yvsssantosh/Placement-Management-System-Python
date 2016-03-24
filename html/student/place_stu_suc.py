#!/usr/bin/env python3

from place_class import*

from random import*
import cgi
import cgitb
import sqlite3
import smtplib
from http.cookies import*
ck=SimpleCookie();
path="/var/www/html/plac_1.db"

try:

 flag=0;

 sname="Student";

 def email1():
  
  fadr="kmitpython21@gmail.com"
  
  tadr=semail; 
   
  gpwd=randrange(100000,9999999,1);
  
  gpwd=str(gpwd); 
   
  a='''update stu_info set pass="'''+gpwd+'''" where stu_id="'''+sid+'''"''';
    
  cur.execute(a);
    
  con.commit();
       
  msg='''hello  '''+sname+'''     \n Thank you for registering with us!!\n\nlogin details:\nUserid:'''+sid+''' \npassword:'''+gpwd+'''\n\nYou may change your password after login\n''';                                                   
                                                             
  print("");
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("kmitpython21@gmail.com","kmit@python21");      
  server.sendmail(fadr, tadr, msg)
  server.quit()
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check();
 
 print("content-type: text/html")
 html1="""
 <html>
 <body onload="window.location='../student/place_stu_log'">
 </body>
 </html>"""
 
 a="select * from stu_suc;";
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data)!=0):
 
  for i in data:
  
   sid=i[0];
   sname=i[1];
   semail=i[2];
  
  a="delete from stu_suc where stu_id='"+sid+"'";
 
  cur.execute(a);
  
  con.commit();
  
 else:
 
  print(html1); 
 
 sname=sname.upper();
   
 print("content-type: text/html")
 html="""
 
 <!doctype html>
<html>
<head>
<title>
Company Notification
</title>
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
 <script type="text/javascript" src="date_time.js"></script>
 <link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
 <link rel="stylesheet" type="text/css" href= "/CSS/table.css">
 <link rel="stylesheet" type="text/css" href= "/CSS/logo.css">


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
            
            <span id = "letters"><a href="../student/place_stu_log"><span class = "back">Back</span></a></span>
 </br>
 
 <h1 align = "Center">
 """+sname+"""  Your Registration Was Successfull!
 </h1>
 </br>
 </br>
 <h3 align="center">
 You will Recieve  Email with your login details.
 </h3> 
 </br>
 </br>
 </body>
 </html>"""
 
 

 
 
 html2="""
 <html>
 <body onload="window.location='../student/place_stu_home'">
 </body>
 </html>"""
 
 stu_id=form.getvalue("stu_id","-");
 p1=form.getvalue("pass");
 
 print(html.format(**locals()));

 if(flag == 0):
 
  email1();
  flag=1;
         
   
except:
 
 cgitb.handler();
 
finally:

 con.close();
