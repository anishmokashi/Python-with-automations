''' write a program which contains filter(),map() and reduce() in it.
Python application which contains one list of numbers.List contains the numbers which are accepted from user.
 Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90.
 Map function will increase will increase each number by 10.Reduce will return product of all that numbers.

 Input List=[4,34,36,76,68,24,89,23,86,90,45,70]
 List after filter=[76,89,86,90,70]
 List after map=[86,99,96,100,80]
 output of reduce=6538752000


'''
from functools import reduce


def checking_nm(num):
    
    if(num>=70 and num<=90):
        return True
def Increase_by_10(num):
    return num+10
def mult_List(num1,num2):
    return num1*num2
 
def main():
    Input_List=[]
    size=int(input("Enter how many elements you want to enter in the list : "))
    for i in range(size):
        num=int(input())
        Input_List.append(num)
    print("Input List",Input_List)

    List_after_filter=(list(filter(checking_nm,Input_List)))
    ''' Here we are giving two inputs to filter function one is the checking_num function
    which checks if the given number is greater than 70 and less than 90 and returns true if it is.
    Other paramter to filter is the input list which can be static or taken from user.
    what filter function does is takes one parameter at a time and pass it to the checking num fucntion 
    (we have not given opening closing circular bracket to checking num function because the filter function will be calling
    the checking_num function and not the user.).So after passing the number to check sum number the function checks the input as per the logic and return true
    and if filter function gets true as a return value then it adds that number to the new list which is List_after_filter  
    '''
    print("List after filter",List_after_filter)
    List_after_map=list(map(Increase_by_10,List_after_filter))
    '''map function is used to do a specific(map)operation on list which is output of filter function. Here we are adding 10 to every element of the list.
    Like filter function map function also takes list as a input and pass it to the particular function one by one
    '''
    print("List after map",List_after_map)
    List_after_reduce=reduce(mult_List,List_after_map)
    '''For using reduce function we have to import it from functools module. It performs computation on whole list an return result.
    It applies rolling computation to sequential pairs of values in the list.It also takes two parameters like map function , one is the function which 
    will multiplay and give a result. so the reduce function will multiply all the elements in the list and give the desired output.
    It takes two parameters and after getting result of it , it multiplies result obtained with the next parameter in the list. 
    '''
    print("List after reduce",List_after_reduce)

    

if __name__=="__main__":
    main()