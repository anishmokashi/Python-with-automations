import multiprocessing
import os

def Task1():
    print("Executing the first task...")
    print("PID of running process for task1 : ",os.getpid())

def Task2():
    print("Executing the second task...")
    print("PID of running process for task2 : ",os.getpid())

def main():
    print("Demonstration of Multiprocessing")
    print("PID of running process is : ",os.getpid())

    Task1()
    Task2()

if __name__ == "__main__":
    main()