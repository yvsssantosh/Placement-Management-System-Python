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
 flag=1;
 
 print("content-type:text/html\n\n");
 
 html1='''
  <html>
 
 <body onload="window.location='../student/place_stu_log.py'">
 
 </body>
 
 </html>'''
 
 html3='''
  <html>
 
 <body onload="window.location='../student/place_stu_home.py'">
 
 </body>
 
 </html>'''
 
 html2='''
 <!Doctype html>
<html>
<head>
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
  
  
    
      <a href = "../student/place_stu_home.py">
       
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
<a href = "../student/place_stu_home.py">
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
            
            
            <span id = "letters"><a href="../student/place_stu_home"><span class = "back">Back</span></a></span>
 </br>


<form>
 <table align="center" bgcolor="#f4f4f4" style = "padding:1% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >

<tr>
<td>
Name : 
</td>
<td>
<input type="text" value={stu_name} name="stu_name" required autofocus>
</td>
</tr>

<tr>
<td>
Mobile No: 
</td>
<td>
<input type="text" value={stu_mob} name="stu_mob" required maxlength="10">
</td>
</tr>

<tr>
<td>
Email Id
</td>
<td>
<input type="email" value={stu_email} name="stu_email" required >
</td>
</tr>

<tr>
<td>
Add Skills
</td>
<td>
<select name="drop">
<option value='skill'>SKILLS</option>
<option value='c'>C/C++</option>
<option value='data'>Data Structures</option>
<option value='java'>JAVA</option>
<option value='python'>Python</option>
<option value='html'>HTML/CSS</option>
<option value='oracle'>ORACLE</option>
<option value='sql'>SQL</option>
<option value='jquery'>JQUERY</option>
<option value='net'>.NET</option>
<option value='networks'>NETWORKS</option>
</select>
</td>
</tr>

<tr>
<td>
Delete Skills
</td>
<td>
<select name="ddrop">
<option value='skill'>SKILLS</option>
<option value='c'>C/C++</option>
<option value='data'>Data Structures</option>
<option value='java'>JAVA</option>
<option value='python'>Python</option>
<option value='html'>HTML/CSS</option>
<option value='oracle'>ORACLE</option>
<option value='sql'>SQL</option>
<option value='jquery'>JQUERY</option>
<option value='net'>.NET</option>
<option value='networks'>NETWORKS</option>
</select>
</td>
</tr>

<tr>
<td>
</td>

</tr>

</table>

<br>
<p align = "center">
<input class = "accept" type="submit" required value="Submit" name="sub2">
</p>

</form>
<br>
<br>
<br>
<h2 align = "center">Any Queries Regarding Change In Marks Please Contact Administrator</h2>
</body>
</html>'''

 
 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
  
  if 'username' in cookie_string: 
   username=ck['username'].value;
   
  else:
   username=""; 
   print(html1);
   
 else:
  username="";
  stu_name=""
  stu_email=""
  stu_mob=""
  print(html1);
  
  
 a='''select * from stu_info where stu_id="'''+username+'''";''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data) == 0):
 
  print(html1);
  
 else:
 
  for i in data:
  
   stu_name=i[1];
   stu_mob=i[14];
   stu_email=i[15];
  

 html='''
 <!Doctype html>
<html>
<head>
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
  
  
    
      <a href = "../student/place_stu_home.py">
       
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
<a href = "../student/place_stu_home.py">
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
            
            
            <span id = "letters"><a href="../student/place_stu_home"><span class = "back">Back</span></a></span>
 </br>
 
 
 
 
<h3 align = "center" style = "font-family:sans-serif;"><em><h3 style = "color:red;">Note:</h3>Check all details thoroughly. You will NOT be able to make changes once info is            submitted.</em></h3>
</br>
</br>
<form >
<table align="center" bgcolor="#f4f4f4" style = "padding:3% 3% 3% 3%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >

<tr class = "row">
<td>
Name : 
</td>
<td>
<input type="text" value={stu_name} name="stu_name" required autofocus>
</td>
</tr>

<tr class = "row">
<td>
Mobile No: 
</td>
<td>
<input type="number" value={stu_mob} name="stu_mob" required maxlength="10">
</td>
</tr>

<tr class = "row">
<td>
Email Id
</td>
<td>
<input type="email" value={stu_email} name="stu_email" required >
</td>
</tr>

<tr class = "row">
<td>
Date Of Birth:
</td>
<td>
<input type="date" required value={stu_dob} name="stu_dob">
</td>
</tr>

<tr class = "row">
<td>
Age:
</td>
<td>
<input type="number" required maxlength="2" value={stu_age} name="stu_age">
</td>
</tr>
</table>
     
     <table align="center" bgcolor="#e8e8e8" style = "margin-top:1%;padding:2% 5% 3% 5%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >


<tr>
<td colspan="3" align="center">
ACADEMICS:
</td>
</tr>

<tr>
<td colspan="3" align="center">
------------------------------------------
</td
</tr>


<tr class = "row">
<td>
Class 10:
</td>
<td>
<input type="number" maxlength="2" value={stu_10} name="stu_10">%
</td>
</tr>

<tr class = "row">
<td>
Class 12:
</td>
<td>
<input type="number" required maxlength="2" value={stu_12} name="stu_12">%
</td>
</tr>
<tr>
<td colspan="3" align="center">
------------------------------------------
</td
</tr>

<tr>
<td colspan="3" align="center">
B.tech:


</td>
</tr>




<tr class = "row">
<td>

First Year:
</td>
<td>
<input type="number" required maxlength="2" value={stu_1} name="stu_1">%
</td>
</tr>

<tr >
<td colspan="3" align="center">
Second Year
</td>
</tr>

<tr class = "row">
<td>
I-Sem:
</td>
<td>
<input type="number" required maxlength="2" value={stu_21} name="stu_21">%
</td>
</tr>

<tr class = "row">
<td>
II-Sem:
</td>
<td>
<input type="number" required maxlength="2" value={stu_22} name="stu_22">%
</td>
</tr>

<tr>
<td colspan="3" align="center">
Third Year
</td>
</tr>

<tr class = "row">
<td>
I-sem:
</td>
<td>
<input type="number" maxlength="2" required value={stu_31} name="stu_31">%
</td>
</tr>

<tr class = "row">
<td>
II-sem:
</td>
<td>
<input type="number" maxlength="2" value={stu_32} name="stu_32">%
</td>
</tr>

<tr>
<td colspan="3" align="center">
Fourth Year
</td>
</tr>

<tr class = "row">
<td>
I-Sem:
</td>
<td>
<input type="number" maxlength="2" value={stu_41} name="stu_41">%
</td>
</tr>

<tr class= "row">
<td>
II-Sem:
</td>
<td>
<input type="number" maxlength="2" value={stu_42} name="stu_42">%
</td>
</tr>
<tr>
<td colspan="3" align="center">
                                -
</td
</tr>

<tr class = "row">
<td >
Aggregate:
</td>
<td>
<input type="number" maxlength="2" value={stu_engg} name="stu_engg" required>%
</td>
</tr>

</table>
     
     <table align="center" bgcolor="#e8e8e8" style = "margin-top:1%;padding:2% 4% 3% 4%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >

<tr>
<td colspan="2" align="center">
PROFESSIONAL SKILLS:
</td>
</tr>

<tr>
<td colspan="2" align="center">
------------------------------------------
</td
</tr>

<tr >
<td class = "row">
 <input type="checkbox"  name="c"  value="1">C/C++

</td>
<td class = "row">
 <input type="checkbox"  name="data1" value="1">Data Structures
</td>
</tr>
<tr>
<td class = "row">

 <input type="checkbox"  name="java" value="1">JAVA
</td>
<td class = "row">
<input type="checkbox"  name="python"  value="1">Python<br>
</td>
</tr>
<tr>
<td class = "row">
 <input type="checkbox"  name="html1"  value="1">HTML/CSS

</td>
<td class = "row">
 <input type="checkbox"  name="oracle"  value="1">ORACLE
</td>
</tr>
<tr>
<td class = "row">
<input type="checkbox"  name="sql"  value="1">SQL

</td>
<td class = "row">
<input type="checkbox"  name="jquery"   value="1">JQuery<br>
</td>
</tr>
<tr>
<td class = "row">

<input type="checkbox"  name="net"      value="1">.NET
</td>
<td class = "row">
 <input type="checkbox"  name="networks"  value="1">Networks
</td>
</tr>


 
 
</td>
</tr> 
<tr>
<td>
</td>
<td>

</td>
</tr>

 
</table>
<p align="center" style="font-family:sans-serif;"><strong> By clicking submit I certify that the above facts are true to
the best of my
knowledge and belief
and I understand that I subject myself to
disciplinary action in the event that
the above facts are found to be falsified. </strong></p>
<p align = "center" >
<input class = "accept" type="submit" value="Submit" name="sub1">
</p>
</form>
</body>
</html>

'''
 
 
 
 stu_name=form.getvalue("stu_name",stu_name);
 stu_mob=form.getvalue("stu_mob",stu_mob);
 stu_email=form.getvalue("stu_email",stu_email);
 stu_dob=form.getvalue("stu_dob",'-');
 stu_10=int(form.getvalue("stu_10",0));
 stu_12=int(form.getvalue("stu_12",0));
 stu_1=int(form.getvalue("stu_1",0));
 stu_21=int(form.getvalue("stu_21",0));
 stu_22=int(form.getvalue("stu_22",0));
 stu_31=int(form.getvalue("stu_31",0));
 stu_32=int(form.getvalue("stu_32",0));
 stu_41=int(form.getvalue("stu_41",0));
 stu_42=int(form.getvalue("stu_42",0));
 stu_engg=int(form.getvalue("stu_engg",0))
 stu_age=int(form.getvalue("stu_age",0));
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
 lskills=form.getvalue('drop');
 dskills=form.getvalue('ddrop');
 
 a='''select * from stu_skills where stu_id="'''+username+'''"''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data) == 0):
  print(html.format(**locals()))
 
 else:
  print(html2.format(**locals())); 
  
 if "sub1" in form:
 
  a='''update stu_info set stu_name='%s',stu_mob='%s',stu_email='%s',stu_10=%d,stu_12=%d,stu_1=%d,stu_21=%d,stu_22=%d,stu_31=%d,stu_32=%d,stu_41=%d,stu_42=%d,stu_engg=%d,stu_age=%d,stu_dob="%s",noff=0,so1="0",so2="0",so3="0" where stu_id="%s"'''%(stu_name,stu_mob,stu_email,stu_10,stu_12,stu_1,stu_21,stu_22,stu_31,stu_32,stu_41,stu_42,stu_engg,stu_age,stu_dob,username);
      
  cur.execute(a);
  
  a='''insert into stu_skills values("%s",%d,%d,%d,%d,%d,%d,%d,%d,%d,%d);'''%(username,c,data1,java,python,html1,oracle,sql,jquery,net,networks);
  
  cur.execute(a);
  con.commit();
    
  print(html3);
    
 elif "sub2"in form:
 
  b='''select stu_email from stu_info where stu_id="'''+username+'''"''';
  
  cur.execute(b);
  
  data3=cur.fetchall();
  
  for i in data3:
  
   e=i[0];
   
   
  a='''select stu_email from stu_info;'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data) == 0):
   flag=1;
   
  else:
  
   for i in data:
   
    if(i[0] == stu_email and i[0]!=e):
    
     print("<p align ='center' style = 'color:red'>Email Already Registered!! </p>");
     
     flag=0;
     
     
  if(flag==1):   
   a='''update stu_info set stu_name='%s',stu_mob='%s',stu_email='%s' where stu_id="%s"'''%(stu_name,stu_mob,stu_email,username);
   cur.execute(a);
   
   if( lskills != 'skill' ):
   
    a='''update stu_skills set '''+lskills+'''=1 where stu_id="'''+username+'''";''';
    
    
    cur.execute(a);
    
   if( dskills != 'skill' ):
   
    a='''update stu_skills set '''+dskills+'''=0 where stu_id="'''+username+'''";''';
    
    
    cur.execute(a);
    
    
   con.commit();
   print(html3);
   
 else:
 
  pass;

    
except:

 cgitb.handler();

