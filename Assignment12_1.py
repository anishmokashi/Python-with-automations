''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

 1.Design automation script which display information of running processes as its name , PID ,Username.
    Usage : ProcInfo.py

'''

from sys import *
import psutil
def ProcessDisplay():
    listprocess=[]
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
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
        print("usage : ApplicationName anydigit")

    
    
    try:
        listprocess=ProcessDisplay()
        for elem in listprocess:
            print(elem)
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()

