#!/usr/bin/env python3

import cgi
import cgitb
import sqlite3

cgitb.enable();

path="/var/www/html/plac_1.db";

try:
 
 con=sqlite3.connect(path);
 cur=con.cursor()
 
 cur.execute("create table stu_info(stu_id text primary key,stu_name varchar(20),stu_sex char,stu_branch varchar(10),stu_10 integer,stu_12 integer,stu_1 integer,stu_21 integer,stu_22 integer,stu_31 integer,stu_32 integer,stu_41 integer,stu_42 integer,stu_engg integer,stu_mob varchar(10),stu_email varchar(30),pass varchar(30),stu_age integer,stu_dob varchar(30),noff integer,so1 text,so2 text,so3 text);");
 
 cur.execute("create table adm_info(username varchar(10) primary key,password varchar(20));");
 
 cur.execute("insert into adm_info values('admin','password')");
 
 cur.execute("create table com_info(c_name varchar(20) primary key ,password varchar(20));");
 
 cur.execute("create table com_initial(c_name varchar(40),c_address varchar(200),c_mob varchar(10),c_web varchar(30),key1_name varchar(20),key1_email varchar(30) primary key,key1_mob varchar(10),key2_name varchar(20),key2_email varchar(30),key2_mob varchar(10),pwd varchar(30));");
 
 cur.execute("create table com_suc(c_name varchar(30) primary key,key1_email varchar(30))");
 
 cur.execute("create table stu_suc(stu_id varchar(30) primary key,stu_name varchar(40),stu_email varchar(30));");
 
 cur.execute("create table pm_info(username varchar(20) primary key,password varchar(20));");
 
 cur.execute("insert into pm_info values('pmanager','password')");
 
 cur.execute("create table pm_log(login datetime);");
 
 cur.execute("create table com_rej(c_name varchar(40),c_address varchar(200),c_mob varchar(10),c_web varchar(30),key1_name varchar(20),key1_email varchar(30) primary key,key1_mob varchar(10),key2_name varchar(20),key2_email varchar(30),key2_mob varchar(10),pwd varchar(30));");
 
 cur.execute("create table stu_skills(stu_id text primary key,c integer,data integer,java integer,python integer,html integer,oracle integer,sql integer,jquery integer,net integer,networks integer);");
 
 cur.execute("create table com_criteria(cname varchar(30),cid varchar(40) primary key,sof text,branch text,skills text,per text);");
 
 cur.execute("create table com_date(cname varchar(30),cid varchar(40) primary key,date1 text,type1 text,date2 text,type2 text,date3 text,type3 text,date4 text,type4 text,date5 text,type5 text,nor text)");
 
 cur.execute("create table stu_placed(stu_id text,cid text);");
 
 cur.execute("create trigger trig1 update of stu_id on stu_info begin update stu_skills set  stu_id=new.stu_id where stu_id=old.stu_id; update stu_placed set stu_id=new.stu_id where stu_id=old.stu_id;end;");
 
 cur.execute("create trigger trig2 delete on stu_info begin delete from stu_skills where stu_id=old.stu_id; delete from stu_placed where stu_id=old.stu_id;end;");
 
 cur.execute("create trigger trig3 update of key1_email on com_initial begin update com_criteria set cid=new.key1_email where cid=old.key1_email;update com_date set cid=new.key1_email where cid=old.key1_email; update stu_placed set cid=new.key1_email where cid=old.key1_email;end;");
 
 
  
 
 con.commit();
 
 con.close();
 
except:
 cgitb.handler();
