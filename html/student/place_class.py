#!/usr/bin/env python3

import cgi
import cgitb
import sqlite3

path="/var/www/html/plac_1.db"

 
con=sqlite3.connect(path);
cur=con.cursor();

class check:


 def admin_id(self,usr,pas):
 
  self.usr=usr;
  
  self.pas=pas;
  
  a="select password from adm_info where username='"+self.usr+"';"
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data) == 0):
  
   print("<p align = 'center'style = 'color:red;'>Invalid UserId!!</p><br>");
  
   return(1);
   
  else:
  
   for i in data:
   
    if( i[0] == self.pas):
    
     return(0);
    
    else:
     
     print("<p align = 'center' style = 'color:red;'>Invalid Password!! </p><br>");
     
     return(1);
 
 def stu_id(self,usr,pas):
 
  self.usr=usr;
  
  self.pas=pas;
  
  a="select pass from stu_info where stu_id='"+self.usr+"';"
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if( len(data) == 0):
  
   print("<p  align = 'center' style = 'color:red'>Invalid UserId!! </p></br><br></br><br>");
  
   return(1);
   
  else:
  
   for i in data:
   
    if( i[0] == self.pas):
 
     return(0);
    
    else:
     
     print("<p align ='center' style = 'color:red'>Invalid Password!! </p></br>");
     
     return(1);

 
 def com_id(self,usr,pas):
 
  self.usr=usr;
  
  self.pas=pas;
  
  a="select pwd from com_initial where key1_email='"+self.usr+"';"
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if( len(data) == 0):
  
   print("<p  align = 'center' style = 'color:red'>Invalid UserId!! </p>");
  
   return(1);
   
  else:
  
   for i in data: 
   
    if( i[0] == self.pas):
    
     return(0);
    
    else:
     
     print("<p align ='center' style = 'color:red'>Invalid Password!! </p>");
     
     return(1);

 def pm_id(self,usr,pas):
 
  self.usr=usr;
  
  self.pas=pas;
  
  a="select password from pm_info where username='"+self.usr+"';"
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  if(len(data) == 0):
  
   print("<p align = 'center'style = 'color:red;'>Invalid UserId!!</p></br>");
  
   return(1);
   
  else:
  
   for i in data:
   
    if( i[0] == self.pas):
    
     return(0);
    
    else:
     
     print("<p align = 'center' style = 'color:red;'>Invalid Password!! </p></br>");
     
     return(1);



 
 def adm_cpas(self,opas,npas1,npas2):
 
  self.opas=opas;
  self.npas1=npas1;
  self.npas2=npas2;
  
  a='''select password from adm_info;'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  for k in data:
   
   oldpas=k[0];
   
  if(oldpas == self.opas):
  
   if(len(self.npas1) >= 6):
   
    if(self.npas1 == self.npas2):
    
     a='''update adm_info set password="'''+npas1+'''";''';
     
     cur.execute(a);
     
     con.commit();
     
     print("<h3 align='center'> Password Successfully Updates </h3>");
     
   
     
    else:
    
     print("<p align = 'center' style = 'color:red;'>Passwords Donot Match!! </p><br>");
     
    
     
   else:
   
    print("<p align = 'center' style = 'color:red;'>Invalid Length Of Password </p><br>");
     
  else:
  
   print("<p align = 'center' style = 'color:red;'>Invalid Old Password!! </p><br>");
   
 
 def com_cpas(self,opas,npas1,npas2,cid):
 
  self.opas=opas;
  self.npas1=npas1;
  self.npas2=npas2;
  
  a='''select pwd from com_initial where key1_email="'''+cid+'''";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  for k in data:
   
   oldpas=k[0];
   
  if(oldpas == self.opas):
  
   if(len(self.npas1) >= 6):
   
    if(self.npas1 == self.npas2):
    
     a='''update com_initial set pwd="'''+npas1+'''";''';
     
     cur.execute(a);
     
     con.commit();
     
     print("<h3 align='center'> Password Successfully Updates </h3>");
     
    
     
    else:
    
     print("<p align = 'center' style = 'color:red;'>Passwords Donot Match!! </p><br>");
     
     
     
   else:
   
    print("<p align = 'center' style = 'color:red;'>Invalid Length Of Password </p><br>");
     
  else:
  
   print("<p align = 'center' style = 'color:red;'>Invalid Old Password!! </p><br>");
   
 
 def stu_cpas(self,opas,npas1,npas2,sid):
 
  self.opas=opas;
  self.npas1=npas1;
  self.npas2=npas2;
  
  a='''select pass from stu_info where stu_id="'''+sid+'''";'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  for k in data:
   
   oldpas=k[0];
   
  if(oldpas == self.opas):
  
   if(len(self.npas1) >= 6):
   
    if(self.npas1 == self.npas2):
    
     a='''update stu_info set pass="'''+npas1+'''";''';
     
     cur.execute(a);
     
     con.commit();
     
     print("<h3 align='center'> Password Successfully Updates </h3>");
     
 
     
    else:
    
     print("<p align = 'center' style = 'color:red;'>Passwords Donot Match!! </p><br>");
     

     
   else:
   
    print("<p align = 'center' style = 'color:red;'>Invalid Length Of Password </p><br>");
     
  else:
  
   print("<p align = 'center' style = 'color:red;'>Invalid Old Password!! </p><br>");
   
 
 def pm_cpas(self,opas,npas1,npas2):
 
  self.opas=opas;
  self.npas1=npas1;
  self.npas2=npas2;
  
  a='''select password from pm_info;'''
  
  cur.execute(a);
  
  data=cur.fetchall();
  
  for k in data:
   
   oldpas=k[0];
   
  if(oldpas == self.opas):
  
   if(len(self.npas1) >= 6):
   
    if(self.npas1 == self.npas2):
    
     a='''update pm_info set password="'''+npas1+'''";''';
     
     cur.execute(a);
     
     con.commit();
     
     print("<h3 align='center'> Password Successfully Updates </h3>");
     
      
    else:
    
     print("<p align = 'center' style = 'color:red;'>Passwords Donot Match!! </p><br>");
   
     
   else:
   
    print("<p align = 'center' style = 'color:red;'>Invalid Length Of Password </p><br>");
     
  else:
  
   print("<p align = 'center' style = 'color:red;'>Invalid Old Password!! </p><br>");
