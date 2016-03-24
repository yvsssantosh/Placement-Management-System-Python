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
 
 <body onload="window.location='../manager/place_manager_comcr.py'">
 
 </body>
 
 </html>'''
 
 html6='''
  <html>
 
 <body onload="window.location='../manager/place_manager_home.py'">
 
 </body>
 
 </html>'''

 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
 
  if 'comcr' and 'nor' and 'manager' in cookie_string:
   company=ck['comcr'].value;
   nor=ck['nor'].value;
   
   
  else:
   company="";
   nor=0;
   print(html1);
   
 else:
  company="";
  nor=0;
  print(html1);
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 a='''select * from com_criteria where cid="'''+company+'''";''';
 
 cur.execute(a);
 
 
 data=cur.fetchall();
 cname="";
 for k in data:
 
  cname=k[0];
  break;
  
  
 drop=''
 i=0;
 nor=int(nor);
 while(i<nor):
  drop=drop+'''<select name="op'''+str(i)+'''">''';
  drop=drop+'''<option value="Technical">Technical</option>'''
  drop=drop+'''<option value="Machine">Machine </option>'''
  drop=drop+'''<option value="Aptitude">Aptitude</option>'''
  drop=drop+'''<option value="Online">Online</option>'''
  drop=drop+'''<option value="Other">Other</option>'''
  drop=drop+'''</select> <input class = "submit" type="date" placeholder="Date(dd/mm/yy)" name="dat'''+str(i)+'''" required><br>'''
  i=i+1;
 
 
 html='''
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
 <form>
 <h2 align = "center" >Assign Round Dates And Type Of Round</h2>
 <br>
 <br><p align = "center">'''+drop+''' 
 <br>
 
 <input class = "submit"type="submit" name='sub' value="INSERT" > 
 </p>
 </form>
 </body>
 </html>'''
 
 print(html);
  
 op0=form.getvalue('op0','none');
 op1=form.getvalue('op1','none');
 op2=form.getvalue('op2','none');
 op3=form.getvalue('op3','none');
 op4=form.getvalue('op4','none');
 dat0=form.getvalue('dat0','none');
 dat1=form.getvalue('dat1','none');
 dat2=form.getvalue('dat2','none');
 dat3=form.getvalue('dat3','none');
 dat4=form.getvalue('dat4','none');
 
 if "sub" in form:
 
  a='''select * from com_date;'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data)!=0):
  
   for i in data:
  
    if(dat0=="none" or (dat0!=i[2] and dat0!=i[4] and dat0!=i[6] and dat0!=i[8] and dat0!=i[10])):
   
     if(dat1=="none" or (dat1!=i[2] and dat1!=i[4] and dat1!=i[6] and dat1!=i[8] and dat1!=i[10])):
    
      if(dat2=="none" or (dat2!=i[2] and dat2!=i[4] and dat2!=i[6] and dat2!=i[8] and dat2!=i[10])):
    
       if(dat3=="none" or (dat3!=i[2] and dat3!=i[4] and dat3!=i[6] and dat3!=i[8] and dat3!=i[10])):
      
        if(dat4=="none" or (dat4!=i[2] and dat4!=i[4] and dat4!=i[6] and dat4!=i[8] and dat4!=i[10])):
   
 
         a='''insert into com_date values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'''%(cname,company,dat0,op0,dat1,op1,dat2,op2,dat3,op3,dat4,op4,str(nor));
  
         cur.execute(a);
  
         con.commit();
  
         print("<br><h5>Data Successfully Updates</h5>");
  
         print(html6);
        
        else:  
         print("<br><h5> %s Date Already Registered</h5>"%(dat4));
         break;
       else:
       
        print("<br><h5> %s Date Already Registered</h5>"%(dat3));
        break; 
      else:
        
       print("<br><h5> %s Date Already Registered</h5>"%(dat2));  
       break;
     else:
       
      print("<br><h5> %s Date Already Registered</h5>"%(dat1));
      break;
    else:
       
     print("<br><h5> %s Date Already Registered</h5>"%(dat0));
     break;
     
  else:
  
   a='''insert into com_date values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'''%(cname,company,dat0,op0,dat1,op1,dat2,op2,dat3,op3,dat4,op4,str(nor));
  
   cur.execute(a);
  
   con.commit();
  
   print("<br><h5>Data Successfully Updates</h5>");
  
   print(html6);
      
except:

 cgitb.handler();
