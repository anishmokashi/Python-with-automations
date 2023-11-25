''' Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer.Evenfactor thread will display addition of even factors of given number and oddfactor 
will display addition of odd factors of given number.After execution of both the thread gets compeleted main thread should display message as "exit from main".
'''
import threading
def evenfactor(num):
    evenfactoraddition=0
    for i in range(1,int((num+1)/2)):
        if(i%2==0):
            evenfactoraddition=evenfactoraddition+i
    print(evenfactoraddition)

def oddfactor(num):
    oddfactoraddition=0
    for i in range(1,int((num+1)/2)):
        if(i%2!=0):
            oddfactoraddition=oddfactoraddition+i
    print(oddfactoraddition)
def main():
   
    
    num=20
    thread1=threading.Thread(target=evenfactor,args=(num,))
    thread2=threading.Thread(target=oddfactor,args=(num,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Exit from main")

    
if __name__=="__main__":
    main()

