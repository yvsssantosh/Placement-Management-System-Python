#!/usr/bin/env python3

from place_class import*

import cgi
import cgitb
import sqlite3
import calendar
from datetime import *
import re

path="/var/www/html/plac_1.db"

try:
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 c=check()
 
 print("content-type:text/html");
 
 cur.execute("select * from com_initial where pwd='None';");
 
 data=cur.fetchall();
 
 lnot=len(data);
 
 cur.execute("select * from com_initial where pwd!='None';");
 
 data=cur.fetchall()
 
 lacc=len(data);
 
 cur.execute("select * from com_rej;");
 
 data=cur.fetchall();
 
 lrej=len(data);
 
 a='''select * from com_criteria;''';
 
 cur.execute(a);
 
 data=cur.fetchall();
 
 a='''select * from com_date;'''
  
 cur.execute(a);
  
 data1=cur.fetchall();
  
 l=[]
 l1=[];
  #print(data,data1);
  
 for i in data:
  
  l1.append(i[0]);
   
 for i in data1:
  
  for k in l1:
   
   if(k == i[0]):
    
    l1.pop(l1.index(k)); 
 
 lccr=len(l1);
 
 mon=int(datetime.today().strftime("%m"));
 da=int(datetime.today().strftime("%d"));
 yea=int(datetime.today().strftime("%y"));
 
 cur.execute("select * from com_date;");
 
 data=cur.fetchall();
 
 if(len(data)==0):
  mycal = calendar.HTMLCalendar(calendar.SUNDAY)
  mystr = mycal.formatmonth(int(yea),int(mon));
  alt=re.sub('cellpadding="0"','cellpadding="10" class = "months" ',mystr); 
  alt=re.sub('th class="mon"','th class = "mon days"',alt); 
  alt=re.sub('th class="tue"','th class = "tue days"',alt);
  alt=re.sub('th class="wed"','th class = "wed days"',alt);
  alt=re.sub('th class="thu"','th class = "thu days"',alt);
  alt=re.sub('th class="fri"','th class = "fri days"',alt); 
  alt=re.sub('th class="sat"','th class = "sat days"',alt);
  alt=re.sub('th class="sun"','th class = "sun days"',alt);
  mystr=alt;     
 else:
  mycal = calendar.HTMLCalendar(calendar.SUNDAY)
  mystr = mycal.formatmonth(int(yea),int(mon));
  alt=re.sub('cellpadding="0"','cellpadding="15" class = "months" ',mystr); 
  alt=re.sub('th class="mon"','th class = "mon days"',alt); 
  alt=re.sub('th class="tue"','th class = "tue days"',alt);
  alt=re.sub('th class="wed"','th class = "wed days"',alt);
  alt=re.sub('th class="thu"','th class = "thu days"',alt);
  alt=re.sub('th class="fri"','th class = "fri days"',alt); 
  alt=re.sub('th class="sat"','th class = "sat days"',alt);
  alt=re.sub('th class="sun"','th class = "sun days"',alt);
 
  for i in data:
  
   cname=i[0];
   nor=int(i[12]);
   var=2;
   f=1;
   
   while(nor!=0):
   
    rdate=i[var];
    rtype=i[var+1];
    
    ld=rdate.split('/');
    da1=int(ld[0]);
    mon1=int(ld[1]);
    yea1=int(ld[2]);
    
    if(yea1 == yea):
    
     if(mon1 == mon):
      
      temp='''">'''+str(da1)+'''</'''
      temp1=''' block badge2" data-badge="'''+cname.upper()+''', Round-'''+str(var-f)+''', '''+rtype+'''" >'''+str(da1)+'''</''';
      alt=re.sub(temp,temp1,alt);
      #print(alt);
    var=var+2;
    f=f+1;
    nor=nor-1; 
     
    
  mystr=alt; 
    
 
 
 

 
 html1='''
  <html>
 
 <body onload="window.location='../manager/place_manager.py'">
 
 </body>
 
 </html>'''
 
 cur.execute("select * from pm_log;");
 
 data=cur.fetchall();
 
 if(len(data) == 0):
 
  print(html1); 
 
 html="""
 
<!doctype html>
<html>


<head >
<title> KMIT - Recruitment</title>

<link rel="stylesheet" type="text/css" href= "/CSS/manager_home.css">
<link rel="stylesheet" type="text/css" href= "/CSS/navibar.css">
<link rel="stylesheet" type="text/css" href= "/CSS/logo.css">
<link rel="stylesheet" type="text/css" href= "/CSS/cal.css">

<script type="text/javascript" src="date_time.js"></script>
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
<a href = "http://www.kmit.in/aboutus">
<span>
About Us</span> </a></td>
</tr>
</table>
</div>

<div  id = "bar2"  >
<table>
<tr><td id  = "login">
<a href = "../place_home.py">
<span>

Logout
</span>
</a>
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
 </br>
<br>
<br>
<br>
<div class = "calen"  >"""+mystr+"""</div>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_com.py' class = "badge1" data-badge='"""+str(lnot)+"""'><span class = "buttons"> Notifications </span></a></p>
</br>

<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_accepted.py' class = "badge1" data-badge='"""+str(lacc)+"""'><span class = "buttons">Accepted List</span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_rejected.py' class = "badge1" data-badge='"""+str(lrej)+"""'><span class = "buttons">Rejected List </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_comcr.py' class = "badge1" data-badge='"""+str(lccr)+"""'><span class = "buttons">Company Criteria </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_ccr.py'><span class = "buttons">Send Email </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_sstu.py' ><span class = "buttons">Search Student </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>

<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_scom.py' ><span class = "buttons">Search Company </span></a></p>
</br>
<h1  style = "color: silver"> <em>____________</em></h1>
<p  style = "position:absolute;left:60px;"><a href='../manager/place_manager_stu_placed.py' ><span class = "buttons">Insert Placed Students </span></a></p>
   
</br>
</br>
</br>
</br>


</body>





</html>"""

 print(html);

except:

 cgitb.handler();
