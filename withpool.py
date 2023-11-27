import multiprocessing

def square(no):
    return no * no

def main():
    Arr = [10,20,30,40]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(square,Arr)
    p.close()
    p.join()
    
    print(Result)

if __name__ == "__main__":
    main()