#!/usr/bin/env python3

import cgi
import cgitb
import calendar
import re
form=cgi.FieldStorage();
try:

 myCal = calendar.HTMLCalendar(calendar.SUNDAY)
 myStr = myCal.formatmonth(2015, 11)

 k=re.sub('</td>','</td>',myStr);
 #k=str(k);
 #k=re.sub('</tr>','</tr>',k);
 #k=str(k);
 k=re.sub('cellpadding="0"','cellpadding="10" class = "months" ',k);
 k=re.sub('cellspacing="0"','cellspacing="0"',k); 
 k=re.sub('th class="mon"','th class = "mon days"',k); 
 k=re.sub('th class="tue"','th class = "tue days"',k);
 k=re.sub('th class="wed"','th class = "wed days"',k);
 k=re.sub('th class="thu"','th class = "thu days"',k);
 k=re.sub('th class="fri"','th class = "fri days"',k); 
 k=re.sub('th class="sat"','th class = "sat days"',k);
 k=re.sub('th class="sun"','th class = "sun days"',k);
       
 
 #k=str(k);
 k=re.sub('border="0"','border="0"',k);
 
 #k=str(k);
 #k=re.sub('</th>','</th>',k);
 #k=str(k);
 k=re.sub('">3</',' block badge1" data-badge="M21sdft, Round-1, 28/11/2015" > 3</',k);
 k=re.sub('">28</',' block badge1" data-badge="adfsoft, Round-1, 28/11/2015" >28   </',k);
 k=re.sub('">13</',' block badge1" data-badge="Google, Round-2, 13/11/2015" >13</',k);
 k=re.sub('">2</',' block badge1" data-badge="Oracle, Round-2, 02/11/2015" >2</',k);
 #k=re.sub('">28</',' block" width = 42px ;><span class = "badge1" data-badge="Test" >28</span></',k);
 #k=re.sub('">13</',' block"><span class = "badge1" data-badge="Test" >13</span></',k);
 #k=re.sub('">2</',' block" ><span class = "badge1" data-badge="Test" >2</span></',k);
 
 #k=str(k);
 #k=re.sub('21','21<br>',k);
 #k=str(k);
 #k=re.sub("\\"," ",k);
 da1=5;
 cname="microsoft";
 var=2;
 f=1;
 rtype="Technical";
 temp='''">'''+str(da1)+'''</'''
 temp1=''' block badge1" data-badge="'''+cname.upper()+''', Round-'''+str(var-f)+''', '''+rtype+'''" >'''+str(da1)+'''</''';
 k=re.sub(temp,temp1,k);
     
 

 
 
 print("content-type:text/html\n\n");
 html='''
 <html>
 <head>
 <title>calendar</title>
 <link rel="stylesheet" type="text/css" href= "/CSS/cal.css">
 </head>
 <body style = "font-family:sans-serif;">
 
 <div class = "calen" align= "center" >
'''
 html2='''

 </div>
 </body>
 </html>'''
 k=str(k);
 print(html+k+html2);

except:

 cgitb.handler();
