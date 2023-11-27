import os
import threading

def Task1(Value):
    print("PID of task1 is : ",os.getpid())
    print("Thread ID of First thread is : ",threading.current_thread())

def Task2(Value):
    print("PID of task2 is : ",os.getpid())
    print("Thread ID of Second thread is : ",threading.current_thread())

def main():
    print("PID of parent process is : ",os.getpid())
    print("Thread ID of main thread is : ",threading.current_thread())
    No = 5
    t1 = threading.Thread(target = Task1, args = (No,))
    t2 = threading.Thread(target = Task2, args = (No,))
     
    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__ == "__main__":
    main()