#!/usr/bin/env python3

from place_class import*

import cgi
import cgitb
import sqlite3

print("Content-type:text/html");
print("""


<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href= "/CSS/style2.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/manager_home.css">

<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">
 <script type="text/javascript" src="date_time.js"></script>


</head>


<table    width = "100%"> 
<tr ><td class = "bglogop" > 
  
  
    
      <a href = "../place_home.py">
       
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
 <h5 align = "right" ><span id="date_time" ></span>
            <script type="text/javascript">window.onload = date_time('date_time');</script></h5>
 </br>
 
 <div>
 <h1 align = "center" style = "color: silver"> <em>Who are you?</em></h1>
 </div>
 </br>


<div id = "1ot">
 <h2 align = "center"><a href = "/admin/place_adm_log.py"><div id = "link1" ><h2 align =  "center" style = "font-style: Arial"> <p><em> Admin</em></p></h2> </div></a></h3>
 </div>

<div id = "2ot">
 <h2 align = "center"><a href = "/student/place_stu_log.py"><div id = "link2" ><h2 align =  "center" style = "font-style: Arial"> <p><em> Student</em></p></h2> </div></a></h3>
 </div>
 
 <div id = "3ot">
 <h2 align = "center"><a href = "/company/place_com_log.py"><div id = "link3" ><h2 align =  "center" style = "font-style: Arial"> <p><em> Company</em></p></h2> </div></a></h3>
 </div>
 
 <div id = "4ot">
 <h2 align = "center"><a href = "/manager/place_manager.py"><div id = "link4" ><h2 align =  "center" style = "font-style: Arial"> <p><em> Placement Manager</em></p></h2> </div></a></h3>
 </div>



</br>
</br>
</br>
</body>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
<footer>
 <p style = "font-family:sans-serif;" align = "right"> Designed and Created by: Ravi Ashish Sagar Vaishnavi </p> 
     </html>
     
     """);

