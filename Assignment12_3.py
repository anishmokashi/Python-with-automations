''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

 3.Design automation script which accept directory name from user and create log file in that directory
    which contains information of running processes as its name ,PID , Username.
 
    Usage : ProcInfo.py Demo

'''

from sys import *
import psutil
import os
def ProcessDisplay(Dir_name,filename="Procinfo.log"):
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
        fd.close()
    else:
        pass
        
def main():
    print("----------------Process Monitor--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to show the running processes on your computer")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName foldername")

    
    
    try:
        ProcessDisplay(argv[1])
        
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()

