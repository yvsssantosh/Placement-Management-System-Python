#!/usr/bin/env python3

from place_class import*
import cgi
import cgitb
import sqlite3

path="/var/www/html/plac_1.db"

try:
  
 print("content-type: text/html");
  
 html1="""
 
 <html>
 <body onload="window.location='../company/place_com_log'">
 </body>
 </html>"""
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check();
 
 a="select * from com_suc";
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 if(len(data)!=0):
 
  for i in data:
 
   cname=i[0];
   email=i[1];
  
  a="delete from com_suc where c_name='"+cname+"'";
 
  cur.execute(a);
 
  con.commit();
 
 else:
 
  print(html1);
 
 cname=cname.upper();
 
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
            
            <span id = "letters"><a href="../company/place_com_log"><span class = "back">Back</span></a></span>

 </br>
 
 <h1 align="center">
 """+cname+"""  """+"""Your Registration Was Successfull!!
 </h1>
 </br>
 <h4 align = "center">Once approved an e-mail will be sent to <u>"""+email+"""</u>  with your login details!</h4>
 </br>
 
             <span id = "letters"><a href="../place_home"><span class = "back">Home</span></a></span>

 
 
 </body>
 </html>
 
 """
 

 
 print(html);
 
except:

 cgitb.handler();
