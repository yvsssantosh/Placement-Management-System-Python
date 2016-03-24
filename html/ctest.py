#/usr/bin/env python3

import calendar
import re
import sqlite3
import cgi
import cgitb
from datetime import *

path="/var/www/html/plac_1.db"
try:

 #ck=SimpleCookie() 
 con=sqlite3.connect(path);
 cur=con.cursor()
 form=cgi.FieldStorage()
 #c=check()
 
 print("content-type:text/html\n\n");
 
 mon=datetime.today().strftime("%m");
 da=datetime.today().strftime("%d");
 yea=datetime.today().strftime("%y");
 
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
      temp1=''' block badge1" data-badge="'''+cname.upper()+''', Round-'''+str(var-f)+''', '''+rtype+'''" >'''+str(da1)+'''</''';
      alt=re.sub(temp,temp1,alt);
      print(alt);
    var=var+2;
    f=f+1;
    nor=nor-1; 
     
    
  mystr=alt; 
    
 html="""
 <html>
 <head>
 <title>calendar</title>
 </head>
 <body>
 <div class = "calen" align= "right" >"""+mystr+"""</div>
 </body>
 </html>"""
 
except:

 cgitb.handler();
