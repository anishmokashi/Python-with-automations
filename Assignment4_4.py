''' write a program which contains filter(),map() and reduce() in it.
Python application which contains one list of numbers.List contains the numbers which are accepted from user.
 Filter should filter out all such numbers which are even.Map function will calculate its square.
 Reduce will return addition of all that numbers.

 Input List=[5,2,3,4,3,4,1,2,8,10]
 List after filter=[2,4,4,2,8,10]
 List after map=[4,16,16,4,64,100]
 output of reduce=204


'''
from functools import reduce


def checking_Even_num(num):
    if ((num%2)==0):
        return True
def calc_square(num):
    return num**2
def add_List(num1,num2):
    return num1+num2
 
def main():
    Input_List=[]
    size=int(input("Enter how many elements you want to enter in the list : "))
    for i in range(size):
        num=int(input())
        Input_List.append(num)
    print("Input List",Input_List)

    List_after_filter=(list(filter(checking_Even_num,Input_List)))

    print("List after filter",List_after_filter)
    List_after_map=list(map(calc_square,List_after_filter))

    print("List after map",List_after_map)
    List_after_reduce=reduce(add_List,List_after_map)

    print("List after reduce",List_after_reduce)

    

if __name__=="__main__":
    main()