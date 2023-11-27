''' Automation script which accept directory name from user from and create log file in that 
directory which contains information of all running processes.'''
import psutil
import time
from sys import *
import os
import re

def ProcessDisplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    separator="_"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))#log navachi file banwaychi
    abs_path=os.path.abspath(log_dir)#jithe banwaychi tya folder cha path kadaycha
    
    
    log_path= re.sub(r'[^\w_. -]', '_', log_path)#log_path navachya file name madhun special symbol kadayche
    abs_path=os.path.join(abs_path,log_path)#folder cha absolute path kadaycha ani toh 
    print(abs_path)
    
    f=open(abs_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous Infosystems Process Logger :"+time.ctime()+"\n")
    f.write(separator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    for element in listprocess:
        f.write("%s\n"%element)
    # f.close()
def main():
    print("---------------------Process Monitor With Log--------------------")
    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This Script is used to log record of running processess")
        exit()

    if(argv[1]=="-u")or(argv[1]=="U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    ProcessDisplay(argv[1])
    try:
        pass
        
        
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")
if __name__=="__main__":
    main()  