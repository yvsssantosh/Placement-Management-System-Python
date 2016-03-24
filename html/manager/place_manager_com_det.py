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
 
  tadr=company; 
   
  gpwd=randrange(100000,9999999,1);
  
  gpwd=str(gpwd); 
   
  a='''update com_initial set pwd="'''+gpwd+'''" where key1_email="'''+company+'''"'''
  
  cur.execute(a);  
    
  con.commit();
       
  msg='''Hello  '''+cname.upper()+'''\n\n\nlogin details:\nUserid:'''+company+''' \npassword:'''+gpwd+'''\n\nYou may change your password after login\n''';                                                   

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("kmitpython21@gmail.com","kmit@python21");      
  server.sendmail(fadr, tadr, msg)
  server.quit()
  
 def insert():
 
  global key1_email;
  
  for i in data:
    
   if(company == i[5]):
     
    a='''insert into com_rej values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","None");'''%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]);
        
    cur.execute(a);
    
    a='''delete from com_initial where key1_email="'''+company+'''";''';
    
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
 
 a='''select * from com_initial;'''
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 for i in data:
 
  d="";
  if(company == i[5]):   
 
   d='''
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
<a href = "../place_home">
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
            
            
            <span id = "letters"><a href="../manager/place_manager_com"><span class = "back">Back</span></a></span>
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
    <input class = "negate" type="submit"  name="disapp" value="Discard">
    <input class = "accept" type="submit" name="approve" value="Approve"> </p>
    </form>
 
    </body>
    </html>'''
   print(d);
     
  
 if "approve" in form:

  for i in data:
    
   if(company == i[5]):
    
    cname=i[0]; 
    email();
    print("Email successfull send!!");
    print("<br>")
    break;

 elif "disapp" in form:
   
  insert();
    
  print("""<h1 align = "center">  Registration DISCARDED</h1>""");
   
  print("<br>")
    
      
 else:
  
  pass;
 
 
except:
 cgitb.handler();
