'''Design python application which contains two threads named as thread 1 and thread 2.
Thread 1 will display 1 to 50 on screen and thread 2 will display 50 to 1 in reverse order on screen.
After execution of thread1 gets completed then schedule thread2. '''
import threading
def Display():
    for i in range(1,51):
        print(i,end=" ")

def DisplayRev():
    for i in range(50,0,-1):
        print(i,end=" ")
def main():
    Thread1=threading.Thread(target=Display)
    print("Starting thread 1")
    Thread1.start()
    Thread1.join()
    print()
    Thread2=threading.Thread(target=DisplayRev)
    print("Starting thread 2")
    Thread2.start()
    Thread2.join()
if __name__=="__main__":
    main()