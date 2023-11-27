
def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    Ans = 0

    try:
        Ans = no1 / no2


    except ZeroDivisionError as zobj:
        print("Divide by Zero is not allowed",zobj)
        return

    except Exception as zobj:
        print("Exception occured as ",zobj)
        return
        
    print("Division is : ",Ans)

if __name__ == "__main__":
    main()