''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

 4.Design automation script which accept directory name and email id from user and create log
 file in that directory which contains information of running processes as its name , pid 
 username.After creating log file send that log file to the specified mail.
    Usage: ProcInfoLog.py Demo Marvellousinfosystem@gmail.com

    Demo is the name of Directory
    marvellousinfosystem@gmail.com is the mail id .

'''

from email import encoders
from sys import *
import psutil
import re
import os
import time
import hashlib
import smtplib	
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import urllib.request
from email.mime.application import MIMEApplication
from urllib.error import URLError
def is_connected():
    try:
        urllib.request.urlopen('http://google.com', timeout=0.5)
        return True
    except URLError as err: 
        
        return False
def ProcessDisplay(email_id,Dir_name,filename="Procinfo.txt"):
    filename_bkup=filename
    listprocess=[]
    
    if not os.path.exists(Dir_name): 
        try:
            os.mkdir(Dir_name)
        except:
            pass
        
        filename=os.path.join(Dir_name,filename)
        filename=os.path.abspath(filename)
        
        
        
        fd=open(filename,'w')

        for proc in psutil.process_iter():
            try:
                pinfo=proc.as_dict(attrs=['pid','name','username'])
                listprocess.append(pinfo)
                
            except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                pass
        for element in listprocess:
            fd.write("%s\n"%element)
        connected = is_connected()
        if connected:
        
         Sending_mail_of_log_file(email_id,filename,)
        
        
            
    else:
        pass
    
def Sending_mail_of_log_file(email_id,filename): 
    # Dir_name=os.path.abspath(Dir_name)
    # file_name=os.path.join(Dir_name,"Procinfo.txt")  
    try :
        email_sender='anish.mokashi13@gmail.com'   
        email_pwd="duab kydh gfzf dvcg"
        email_receiver=email_id

        subject="Process Files Log"
        body='Log file was send at %s'%time.ctime() 

        msg=MIMEMultipart()
        msg['From']=email_sender
        msg['To']=email_receiver
        msg['Subject']=subject
        msg['Body']=body 

        msg.attach(MIMEText(body,'plain'))
        attachment=open(filename,'rb')
        p=MIMEBase('application','octet-stream')
         

        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
        msg.attach(p)

        mailserver=smtplib.SMTP("smtp.gmail.com:587")
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(email_sender,email_pwd)
        mailserver.sendmail(email_sender,email_receiver,msg.as_string())
        mailserver.close()
        print("successfully sent the mail")
    except Exception as error:
        print(str(error))

        


def main():
    print("----------------Process Monitor--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=3):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to show the running processes on your computer")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName foldername")

    
    
    try:
        Foldername=argv[1]
        Emailid=argv[2]
        ProcessDisplay(Emailid,Foldername)
        # Sending_mail_of_log_file(Emailid,Foldername)
        
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()

