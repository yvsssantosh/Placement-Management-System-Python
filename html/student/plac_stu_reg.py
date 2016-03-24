#!/usr/bin/env python3
from place_class import*
import cgi
import cgitb
import sqlite3

path="/var/www/html/plac_1.db"

try:
 
 con=sqlite3.connect(path);
 cur=con.cursor();
 form=cgi.FieldStorage()
 c=check();
 
 def checkrepeat():
 
  a='''select stu_name from stu_info where stu_id="'''+stu_id+'''";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data) == 0):
     
   a='''select stu_name from stu_info where stu_email="'''+stu_email+'''";'''
   
   cur.execute(a);
  
   data=cur.fetchall();
   
   if(len(data) == 0):
   
    return(0);
    
   else:
   
    print("<p align = 'center' style = 'color:red'>This Email already registered </p>");
    
    return(1);
    
       
  else:
  
   print("<p align = 'center' style = 'color:red'>This Roll number already registered </p>");
    
     
   return 1;

 def checkpas():
 
  if(p1 == p2):
    
   return 0;
    
  else:
   
   print("<p align = 'center' style = 'color:red;'>Passwords Do Not Match!! </p>");
   
   return(1); 
  
 def insert():
 
   a='''insert into stu_info (stu_id,stu_name,stu_sex,stu_branch,stu_mob,stu_email) values("%s","%s","%s","%s","%s","%s");'''%(stu_id,name,gender,branch,mob,stu_email);
   
   cur.execute(a);
    
   #con.commit();
     
   b='''insert into stu_suc values("%s","%s","%s");'''%(stu_id,name,stu_email);
  
   cur.execute(b);
  
   con.commit();  
 
 
    
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
            
            <span id = "letters"><a href="../student/place_stu_log"><span class = "back">Back</span></a></span>
 </br>



<h1 align ="center">Student Registration</h1>
</br>


<form method="post">
 <table id = "one" align = "center" height = "400px">
 <tr class = "row">
   <td>
     Roll number:
   </td>
   <td>
     <input type="text" name="stu_id" value={stu_id} required autofocus maxlength="10">
   </td>
 </tr>
 <tr class = "row">
   <td>
     Name:
   </td>
   <td>
     <input type="text" name="stu_name" value={name} required>
   </td>
 </tr>
 <tr >
   <td class = "row">
     Gender:
   </td>
   <td>
     <input type="radio" name="stu_sex" value="male">Male
     <input type="radio" name="stu_sex" value="female">Female
   </td>
 </tr>
 <tr class = "row">
   <td>
     Branch
   </td>
   <td>
      <select name="stu_branch">
        <option value="cse">CSE</option>
        <option value="it">IT</option>
        <option value="ece">ECE</option>
        <option value="eie">EIE</option>
      </select>
   </td>
 </tr>
 <tr class = "row">
   <td>
     Mobile No:
   </td>
   <td>
     <input type="number" name="stu_mob" value={mob} min="10" required maxlength="10" value={mob}>
   </td>
 </tr>
 <tr class = "row">
   <td>
   Email:
   </td>
   <td>
   <input type="email" name="stu_email"  required value={stu_email}>
   </td>
  </tr> 
  <tr>
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
</body>
</html>
 """
  
 
 
 html1="""
 <html>
 <body onload="window.location='../student/place_stu_suc'">
 </body>
 </html>"""
 
 
 stu_id=str(form.getvalue("stu_id","-"));
 
 name=form.getvalue("stu_name","-");
 
 gender=form.getvalue("stu_sex","");
 
 branch=form.getvalue("stu_branch");
 
 mob=form.getvalue("stu_mob");
 
 stu_email=form.getvalue("stu_email","-");
 
 
 print(html.format(**locals()));
 
 
 if "sub1" in form:   
   
  res=checkrepeat();
   
  if(res == 0):
  
   print(" <p align = 'center'><img src = '../gifs/load.gif'/></p>");
   
   insert();
   
   #suc();
    
   print(html1);
 
except:

 cgitb.handler();
 
finally:
 
 con.close(); 
   
