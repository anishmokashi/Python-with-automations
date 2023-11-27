import multiprocessing
import os

def Task1(Value):
    print("Executing the first task...")
    print("PID of running process for task1 : ",os.getpid())

def Task2(Value):
    print("Executing the second task...")
    print("PID of running process for task2 : ",os.getpid())

def main():
    print("Demonstration of Multiprocessing")
    print("PID of running process is : ",os.getpid())

    No = 5
    p1 = multiprocessing.Process(target = Task1, args = (No,))
    p2 = multiprocessing.Process(target = Task2, args = (No,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()