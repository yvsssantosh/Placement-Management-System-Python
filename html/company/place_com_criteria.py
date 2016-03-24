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

 print("content-type:text/html\n\n");

 html1='''
  <html>
 
 <body onload="window.location='../company/place_com_log.py'">
 
 </body>
 
 </html>'''
 
 html9='''
  <html>
 
 <body onload="window.location='../company/place_com_scr.py'">
 
 </body>
 
 </html>'''
 
 html15='''
 <!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">


 <script type="text/javascript" src="date_time.js"></script>


</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = "../company/place_com_home.py">
       
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
<a href = "../company/place_com_home.py">
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
             <span id = "letters"><a href="../company/place_com_home"><span class = "back">Back</span></a></span>
 </br>
 <body>
 <h3 align ="center" >
 KMIT Has Already Recieved A Criteria From You.<br>
 To Update Criteria Please Contact Concerned KMIT Officials.
 </h3>
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
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 #print("content-type:text/html\n\n");
 
 a='''select cname from com_criteria where cid="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data)!=0):
 
  print(html15);
  
 else:
 
  html='''
  <!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logbuttons.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">


 <script type="text/javascript" src="date_time.js"></script>


</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = "../company/place_com_home.py">
       
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
<a href = "../company/place_com_home.py">
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
             <span id = "letters"><a href="../company/place_com_home"><span class = "back">Back</span></a></span>
 </br>
 <form>

 
  <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 
 <tr>
 <td>
 Approx Salary Offering:
 </td>
 <td>
 <input type="text" name="salary" value={salary} required autofocus>p.a
 </td>
 </tr>
 
 <tr>
   <td>
   <br>
     Branch
   </td>
   <td>
   <br>
   <input type="checkbox"  name="cse"  value="1">CSE
  <input type="checkbox"  name="ece" value="1">ECE
  <input type="checkbox"  name="it" value="1">IT
  <input type="checkbox"  name="eie"  value="1">EIE<br>
   </td>
 </tr>
  
 <tr>
 <td>
 <br>
 Desired Skills:
 </td>
 <td>
 <br>

 <input type="checkbox"  name="c"  value="1">C/C++
 <input type="checkbox"  name="data1" value="1">Data Structures
 <input type="checkbox"  name="java" value="1">JAVA
 <input type="checkbox"  name="python"  value="1">Python<br>
 <input type="checkbox"  name="html1"  value="1">HTML/CSS
 <input type="checkbox"  name="oracle"  value="1">ORACLE
 <input type="checkbox"  name="sql"  value="1">SQL
 <input type="checkbox"  name="jquery"   value="1">JQuery<br>
 <input type="checkbox"  name="net"      value="1">.NET
 <input type="checkbox"  name="networks"  value="1">Networks
</td>
</tr> 
 
 <tr>
 <td>
 <br>
 Desired Percentage
 </td>
 <td>
 <br>
 <select name="per">
 <option value='85'>Above 85%</option>
 <option value='80'>Above 80%</option>
 <option value='75'>Above 75%</option>
 <option value='70'>Above 70%</option>
 <option value='65'>Above 65%</option>  
 <option value='60'>Above 60%</option>
 <option value='55'>Above 55%</option>  
 </td>
 </tr>
 </table>
 
 
 <p align = "center">
 <input class = "accept" type="submit" name="sub" value="Check Eligible Students">
 <input class = "submit" type="reset" name="res" value="Reset">
 </p>
 </form>
 </body>
 </html>'''
 
  salary=int(form.getvalue('salary',0));
  cse=int(form.getvalue('cse',0));
  ece=int(form.getvalue('ece',0));
  it=int(form.getvalue('it',0));
  eie=int(form.getvalue('eie',0));
  c=int(form.getvalue("c",0));
  data1=int(form.getvalue("data1",0));
  java=int(form.getvalue("java",0));
  python=int(form.getvalue("python",0));
  html1=int(form.getvalue("html1",0));
  oracle=int(form.getvalue("oracle",0));
  sql=int(form.getvalue("sql",0));
  jquery=int(form.getvalue("jquery",0));
  net=int(form.getvalue("net",0));
  networks=int(form.getvalue("networks",0));
  per=int(form.getvalue("per",0));
 
  print(html.format(**locals()));
 
 
  l=[];  
  l2=[];
  
  if(c == 1):
   l.append("c");

      
  if(data1 == 1):
   l.append("data"); 

  if(java == 1):
   l.append("java");

  if(python == 1):
   l.append("python");
 
      
  if(html1 == 1):
   l.append("html");
 
  if(oracle == 1):
   l.append("oracle");
 
      
  if(sql == 1):
   l.append("sql");
 
      
  if(jquery == 1):
   l.append("jquery");
 
      
  if(net== 1):
   l.append("net");

      
  if(networks == 1):
   l.append("networks");
 

  
  if(cse == 1):
   l2.append("cse");
      
  if(ece == 1):
   l2.append("ece"); 

      
  if(it == 1):
   l2.append("it");
     
  if(eie == 1):
   l2.append("eie");

  
 
 
 
  blist="";
  slist="";
  lblist=len(l2)-1;
  lslist=len(l)-1;

 
  for k in l2:
 
   if(l2.index(k) == lblist):
    blist=blist+k;
   
   else:
    blist=blist+k+",";
  
  for k in l:
 
   if(l.index(k) == lslist):
    slist=slist+k;
   
   else:
    slist=slist+k+",";
 
  if "sub" in form:
 
   if(len(l2) == 0):
  
    print("<br><h3>Branch Not Selected!!</h3>");
   
   elif(len(l) == 0):
  
    print("<br><h3>Skills Not Selected</h3>");
   
   else:
   #print(blist);
   #print(slist);
    ck['blist']=blist; 
    ck['slist']=slist;
    ck['salary']=salary;
    ck['percentage']=per;
   
    print(ck.js_output());
   
    print(html9);
  
  
  
except:
 cgitb.handler();
