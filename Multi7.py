import os
import threading

def Task1(Value):
    print("PID of task1 is : ",os.getpid())

def Task2(Value):
    print("PID of task2 is : ",os.getpid())

def main():
    print("PID of parent process is : ",os.getpid())
    
    No = 5
    t1 = threading.Thread(target = Task1, args = (No,))
    t2 = threading.Thread(target = Task2, args = (No,))
     
    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__ == "__main__":
    main()