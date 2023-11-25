''' Write a program which contains one lambda function which accepts one parameter and return 
power of two.
Input : 4   output:16
Input : 6   output:64

'''
power_of_two=lambda A:A**2
def main():
    num=int(input("Enter number to find its power"))
    print("Power of ",num,"is",power_of_two(num))

if __name__=="__main__":
    main()