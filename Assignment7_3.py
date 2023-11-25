''' Design python application which creates two threads as evenlist and oddlist.Both the threads accept list of integers as parameter.
Evenlist thread add all even elements from input list and display the addition.
Oddlist thread add all odd elements from input list and display the addition.
'''
import threading
def evenlist(list):
    evensum=0
    for i in list:
        if(i%2==0):
            evensum=evensum+i
    print(evensum)

def oddlist(list):
    oddsum=0
    for i in list:
        if(i%2!=0):
            oddsum=oddsum+i
    print(oddsum)    

def main():
    list=[]
    for i in range (1,21):
        list.append(i)
    
    thread1=threading.Thread(target=evenlist,args=(list,))
    thread2=threading.Thread(target=oddlist,args=(list,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
if __name__=="__main__":
    main()