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
 
 def email1(semail,sname):
   
  fadr="kmitpython21@gmail.com"
  #semail=key1_email;
  tadr=semail; 
   
 
       
  msg='''Hello '''+sname+'''\n\n\nCongratulation You are Eligible For First Round Of Placement Camp Organised By '''+cname.upper()+''' which will be held on '''+pdate+''' Which is a '''+ptype+''' type of test.Followed By Further Rounds. Please contact administrator for Further details. ''';                                                   

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("kmitpython21@gmail.com","kmit@python21");      
  server.sendmail(fadr, tadr, msg)
  server.quit()
  
 
 
 

 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
 
  if 'comccr' and 'manager' in cookie_string:
   company=ck['comccr'].value;
   
   
  else:
   ptype="";
   company="";
   pdate="";
   print(html1);
   
 else:
  company="";
  ptype="";
  pdate="";
  
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 sof="";
 slist="";
 blist="";
 per=0;
 a='''select * from com_date where cid="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 for o in data:
  cname=o[0];
  pdate=o[2];
  ptype=o[3];
  break;
    
 a='''select * from com_criteria where cid="'''+company+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 for k in data:
  cname=k[0];
  cid=k[1];
  sof=k[2];
  blist=k[3];
  slist=k[4];
  per=int(k[5]);
  break;
  
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
 if(slist[0]!=""):
 
  for w in slist:
  
    f=f+" and skl."+w+"=1";
   
   
 #print(f);
 #print("<br>");
 v="";
 if(blist[0]!=""):  
  
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
    
 
 a='''select stu.stu_id,stu.stu_name,stu.stu_branch,stu.stu_engg,skl.c,skl.data,skl.python,skl.html,skl.sql,skl.java,skl.oracle,skl.net,skl.networks,skl.jquery,stu.so1,stu.so2,stu.so3,stu.stu_email  from stu_info stu join stu_skills skl on stu.stu_id=skl.stu_id where stu.stu_engg>='''+str(per)+'''  '''+v+'''  '''+f+''' and stu.noff <3 ;'''
 
 

 #print(a);
 
 cur.execute(a);
 data=cur.fetchall();
  
 selectedlist=[];
  
 for i in data:
  
  slist=[i[14],i[15]];
   
  sma=max(slist);
   
  sof=int(sof);
   
  sma=int(sma);
   
  sma=sma+(sma*(0.3))
   
  if(sof >= sma):
   
   selectedlist.append([i[0],i[1],i[2],i[17]]);
    
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
  
            
            <span id = "letters"><a href="../manager/place_manager_ccr.py"><span class = "back">Back</span></a></span>
 </br>

 <form>
 <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >
 
 <tr>
 <td><strong>
 Given Criteria:</strong>
 </td>
 <td>
 Salary:
 '''+str(sof)+'''
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
 <h3 align = "center">Do you Want to Send All This Students Email?</h3>
 <br>
 <p align = "center">
 <input class = "accept" type="submit" name="yes" value="YES">
 
 </p>
 </form>
 
 </body>
 </html>'''
 
  
 print(html);
 
 
 
 
 if "yes" in form:

  elist=[];
  
  if(len(selectedlist)!=0):
  
   for k in selectedlist:
  
    elist.append([k[3],k[1]]);
   
   for k in elist:
  
    email1(k[0],k[1]);
   
   print("<br><h5align='center'>Emails Send SuccessFully!!</h5>");   
   
  else:
  
   print("<br><h5align='center'>None Eligible, Email Not Sent!!</h5>");
  
except:

 cgitb.handler();
