def square(no):
    return no * no

def main():
    Arr = [10,20,30,40]
    Result = []

    for value in Arr:
        Ans = square(value)
        Result.append(Ans)
    
    print(Result)

if __name__ == "__main__":
    main()