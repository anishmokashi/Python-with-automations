''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

 2.Design automation script which accept process name and display information of that process if it is running.
    Usage : ProcInfo.py Notepad

'''

from sys import *
import psutil
def ProcessDisplay(process_name):
    listprocess=[]
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            if(pinfo['name']==process_name):

                listprocess.append(pinfo['name'])
            
            

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess
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
        print("usage : ApplicationName name_of_the_process_that_you_want_to_see_if_running_or_not")

    
    
    try:
        listprocess=ProcessDisplay(argv[1])
        if argv[1] in listprocess:
            print(argv[1],"is currently running")
        else:
            print(argv[1],"is currently not running")

        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()

