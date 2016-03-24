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
  
   print("<p align = 'center'style = 'color:red;'>Invalid UserId!!</p>");
  
   return(1);
   
  else:
  
   for i in data:
   
    if( i[0] == self.pas):
    
     return(0);
    
    else:
     
     print("<p align = 'center' style = 'color:red;'>Invalid Password!! </p>");
     
     return(1);
 
 def stu_id(self,usr,pas):
 
  self.usr=usr;
  
  self.pas=pas;
  
  a="select pass from stu_info where stu_id='"+self.usr+"';"
  
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
  
   print("<p align = 'center'style = 'color:red;'>Invalid UserId!!</p>");
  
   return(1);
   
  else:
  
   for i in data:
   
    if( i[0] == self.pas):
    
     return(0);
    
    else:
     
     print("<p align = 'center' style = 'color:red;'>Invalid Password!! </p>");
     
     return(1);
     
