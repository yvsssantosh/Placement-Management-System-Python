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
 
 
 

 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
 
  if 'company' in cookie_string:
   company=ck['company'].value;
   #print(os.environ);
   slist=ck['slist'].value;
   blist=ck['blist'].value;
   per=ck['percentage'].value;
   salary=ck['salary'].value;
   #print(slist);
   #print(blist);
  
   
  
  else:
   print(html1);
   
 else:
  company="";
  slist="";
  blist="";
  per=0;
  salary=0;
  #print(os.environ);
  #print(html1);
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 
   
 a='''select c_name from com_initial where key1_email="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchone();
 
 for k in data:
 
  cname=k;
  
 sklist=slist;
 branchlist=blist;
 slist=slist.split(",");
 blist=blist.split(",");
 
 #branchlist="";
 #skilllist=""; 
 f="";    

 #print("<br><br>");

 #print(slist);
 
 #print(isinstance(slist,list));


 for w in slist:
 
  if(slist.index(w)==0 and len(slist)>1):
  
   f=f+"and skl."+w+"=1";
   
  elif(slist.index(w) == (len(slist)-1)):
  
   f=f+" and skl."+w+"=1";
   
 #print(f);
 #print("<br>");
   
 v=""; 
 ll2=len(blist);
  
 if(ll2==1):
  
  v=v+"and ( stu.stu_branch='"+blist[0]+"' )";
  
 elif(ll2==0):
 
  v=v+"and ( stu.stu_branch='dsadf2hjh' )";
  
 else:
     
  for k in blist:
 
   if(blist.index(k) == 0):
  
    v=v+"and ( stu.stu_branch='"+k+"' or ";
   
   elif(blist.index(k) == ll2-1):
   
    v=v+"stu.stu_branch='"+k+"' )";
    
   else:
  
    v=v+"stu.stu_branch='"+k+"' or ";
    
 
 a='''select stu.stu_id,stu.stu_name,stu.stu_branch,stu.stu_engg,skl.c,skl.data,skl.python,skl.html,skl.sql,skl.java,skl.oracle,skl.net,skl.networks,skl.jquery,stu.so1,stu.so2,stu.so3  from stu_info stu join stu_skills skl on stu.stu_id=skl.stu_id where stu.stu_engg>='''+str(per)+'''  '''+v+'''  '''+f+''' and stu.noff <3 ;'''
 
 

 #print(a);
 
 cur.execute(a);
 data=cur.fetchall();
  
 selectedlist=[];
  
 for i in data:
  
  slist=[i[14],i[15]];
   
  sma=max(slist);
   
  salary=int(salary);
   
  sma=int(sma);
   
  sma=sma+(sma*(0.3))
   
  if(salary >= sma):
   
   selectedlist.append([i[0],i[1],i[2]]);
    
 lselectedlist=len(selectedlist);
 
 if(lselectedlist == 0):
 
  msg="None Eligible";
  
 else:
 
  msg="";
  
  for k in selectedlist:
  
   msg=msg+"<br> "+k[0]+" "+k[1]+" "+k[2];
  
 
  
 
 
 
 
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
 <td><strong>
 Given Criteria:</strong>
 </td>
 <td>
 Salary:
 '''+str(salary)+'''
 <br>
 Branch:'''+branchlist+'''
 <br>
 Percentage: above '''+str(per)+'''
 <br>
 Skills: '''+sklist+'''
 </td>
 </tr>
 
 <tr>
 <td>
 <br>
 <strong>Eligible Students:</strong>
 </td>
 <br>
 <td><br>'''+str(msg)+'''
 
 </td>
 </td>
 
 </table>
 <h3 align = "center">Do you Want to Send This Criteria To Kmit?</h3>
 <br>
 <p align = "center">
 <input class = "accept" type="submit" name="yes" value="YES">
 
 </p>
 </form>
 
 </body>
 </html>'''
 
  
 print(html);
 
 
 html66='''
  <html>
 
 <body onload="window.location='../company/place_com_home.py'">
 
 </body>
 
 </html>'''
 
 
 
 
 
 
 
 if "yes" in form:
 
  
  #print(cname);
  a='''insert into com_criteria values("%s","%s","%s","%s","%s",%s);'''%(cname,company,str(salary),branchlist,sklist,str(per))
   
  cur.execute(a);
   
  con.commit();
  
  print(html66);
   
  
except:

 cgitb.handler();
