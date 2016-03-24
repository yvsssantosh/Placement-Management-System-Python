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
 
 <body onload="window.location='../admin/place_adm_log.py'">
 
 </body>
 
 </html>'''
 
 html3='''
  <html>
 
 <body onload="window.location='../admin/place_adm_home.py'">
 
 </body>
 
 </html>'''
 
 
 
 
 if 'HTTP_COOKIE' in os.environ:
  cookie_string=os.environ.get('HTTP_COOKIE')
  ck=SimpleCookie();
  ck.load(cookie_string)
  
  if 'sid' and 'admin' in cookie_string: 
   username=ck['sid'].value;
   
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
   stu_10=i[4];
   stu_12=i[5];
   stu_1=i[6];
   stu_21=i[7];
   stu_22=i[8];
   stu_31=i[9];
   stu_32=i[10];
   stu_41=i[11];
   stu_42=i[12];
   stu_engg=i[13];  
   stu_dob=i[18];
   stu_age=i[17]; 
  

 html='''
  
<html>
<head>
<title>Student reg.</title>
<link rel="stylesheet" type="text/css" href= "/CSS/table.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
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
            
            
            <span id = "letters"><a href="../admin/place_adm_sstu"><span class = "back">Back</span></a></span>
 </br>

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
<input type="text" value={stu_mob} name="stu_mob" required maxlength="10">
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
<input type="number" maxlength="2" value={stu_engg} name="stu_engg">%
</td>
</tr>

</table>
     
     <table align="center" bgcolor="#e8e8e8" style = "margin-top:1%;padding:2% 4% 3% 4%; font-family:sans-serif; border: 1px solid black; border-radius:1%;"  >

</td>
</tr> 


 
</table>
<input class = "accept" type="submit" value="Update" name="sub1">
<input class="negate" type="submit" value="Delete Recored" name="sub2">
</p>
</form>
</body>
</html>

'''
 
 
 
 stu_name=form.getvalue("stu_name",stu_name);
 stu_mob=form.getvalue("stu_mob",stu_mob);
 stu_email=form.getvalue("stu_email",stu_email);
 stu_dob=form.getvalue("stu_dob",stu_dob);
 stu_10=int(form.getvalue("stu_10",stu_10));
 stu_12=int(form.getvalue("stu_12",stu_12));
 stu_1=int(form.getvalue("stu_1",stu_1));
 stu_21=int(form.getvalue("stu_21",stu_21));
 stu_22=int(form.getvalue("stu_22",stu_22));
 stu_31=int(form.getvalue("stu_31",stu_31));
 stu_32=int(form.getvalue("stu_32",stu_32));
 stu_41=int(form.getvalue("stu_41",stu_41));
 stu_42=int(form.getvalue("stu_42",stu_42));
 stu_engg=int(form.getvalue("stu_engg",stu_engg))
 stu_age=int(form.getvalue("stu_age",stu_age));
  
 print(html.format(**locals()))
 flag=1;
 
 if "sub1" in form:
 
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
  
   a='''update stu_info set stu_name='%s',stu_mob='%s',stu_email='%s',stu_10=%d,stu_12=%d,stu_1=%d,stu_21=%d,stu_22=%d,stu_31=%d,stu_32=%d,stu_41=%d,stu_42=%d,stu_engg=%d,stu_age=%d,stu_dob="%s"  where stu_id="%s"'''%(stu_name,stu_mob,stu_email,stu_10,stu_12,stu_1,stu_21,stu_22,stu_31,stu_32,stu_41,stu_42,stu_engg,stu_age,stu_dob,username);
      
  cur.execute(a);
  
  con.commit();
  
  print("<br><h3>Student Record Updated</h3>");    
   
 elif "sub2" in form:
 
  a='''delete from stu_info where stu_id="'''+username+'''";''';
  
  cur.execute(a);
  
  con.commit();
  
  print(html3);
 
  pass;

    
except:

 cgitb.handler();

