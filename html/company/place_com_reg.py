#!/usr/bin/env python3

from place_class import*

import cgi
import cgitb
import sqlite3

path="/var/www/html/plac_1.db"

try:
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 def insert():
 
  a='''insert into com_initial values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","None");'''%(cname,c_add,c_mob,c_web,key1_name,key1_email,key1_mob,key2_name,key2_email,key2_mob);
  
  cur.execute(a);
  
  con.commit();
  
 def repeat():
 
  a='''select * from com_initial where key1_email="'''+key1_email+'''";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data) == 0):
  
   a='''select * from com_rej where key1_email="'''+key1_email+'''";'''
   
   cur.execute(a)
   
   data=cur.fetchall();
   
   if(len(data)==0):
   
    return(0)
    
   else:
    
    print("<p align = 'center' style = 'color:red;'>This Email Already Registered!! </p>");
    
    return(1);
    
  else:
  
   print("<p align = 'center' style = 'color:red;'>This Email Already Registered!! </p>");
  
   return(1);
 
 def name():
 
  a='''insert into com_suc values("%s","%s");'''%(cname,key1_email);
  
  cur.execute(a);
  
  con.commit();
 
 print("content-type:text/html");
 
 
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
            
            <span id = "letters"><a href="../company/place_com_log"><span class = "back">Back</span></a></span>

 </br>
 <h2 align = "center">Company Registration</h2>
 </br>
 </br>
 <form method="post">
 <table id = "one" align ="center">
 <tr class = "row">
   <td>
     Company's Name:
   </td>
   <td>
     <input type="text" name="c_name" value={cname} required autofocus>
   </td>
 </tr>
 <tr class = "row">
   <td>
     Company's Address:
   </td>
   <td>
     <textarea row="10" cols="20" name="c_add" maxlength="200" value={c_add} required>
     max 200 char
     </textarea> 
   </td>
 </tr>
 <tr class = "row">
   <td>
     company's contact:
   </td>
   <td>
     <input type="number" name="c_mob" value={c_mob} maxlength="10" required>
   </td>
 </tr>
 <tr class = "row">
   <td>
     website:
   </td>
   <td>
      <input type="text" name="c_web" value={c_web} required>
   </td>
 </tr>
 <tr>
   <td align="center" colspan="2">
   Key Person 1 Details:
   </td>
 </tr>
 <tr class = "row">
   <td>
     Name: 
   </td>
   <td>
     <input type="text" name="key1_name" value={key1_name} required>
   </td>
 </tr>
 <tr class = "row">
   <td>
   Email Id:
   </td>
   <td>
   <input type="email" name="key1_email" value={key1_email} required >
   </td>
  </tr> 
  <tr class = "row">
   <td>
   mobile number:
   </td>
   <td >
   <input type="text"  name="key1_mob" required value={key1_mob}>
   </td>
  </tr> 
   <tr>
   <td align="center" colspan="2">
   Key Person 2 Details:
   </td>
 </tr>
 <tr class = "row">
   <td>
     Name: 
   </td>
   <td>
     <input type="text" name="key2_name" value={key2_name} required>
   </td>
 </tr>
 <tr class = "row">
   <td>
   Email Id:
   </td>
   <td>
   <input type="email" name="key2_email" value={key2_email} required >
   </td>
  </tr> 
  <tr class = "row">
   <td>
   mobile number:
   </td>
   <td >
   <input type="text"  name="key2_mob" required value={key2_mob}>
   </td>
  </tr> 
  <tr class = "row">
   <td>
   </td>
   <td>
   </br>
   <input class = "accept" type="submit" name="sub1" value="Submit">
     <input class = "submit" type="reset" name="res1" value="Reset">
   </td>
 </tr>
 </table>
 </form>
 
 
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </br>
 </body>
 </html>"""
  
  
 
 html1="""
 <html>
 <body onload="window.location='../company/place_com_suc.py'">
 </body>
 </html>"""
 
 cname=form.getvalue("c_name","-");
 
 c_add=form.getvalue("c_add","-");
 
 c_web=form.getvalue("c_web","-");
 
 c_mob=form.getvalue("c_mob","-");
 
 key1_name=form.getvalue("key1_name");
 
 key1_email=form.getvalue("key1_email");

 key1_mob=form.getvalue("key1_mob");
 
 key2_name=form.getvalue("key2_name");
 
 key2_email=form.getvalue("key2_email");
 
 key2_mob=form.getvalue("key2_mob");
  
 print(html.format(**locals()));
 
 if "sub1" in form:
 
  res=repeat();
 
  if( res==0):
   
   insert();
   name();
   
   print(html1);
   
   
   
   
  
 
 
except:

 cgitb.handler();
