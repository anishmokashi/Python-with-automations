''' write a program which contains filter(),map() and reduce() in it.
Python application which contains one list of numbers.List contains the numbers which are accepted from user.
 Filter should filter out all prime numbers .Map function will multiply each number by 2.
 Reduce will return maximum number from that numbers.(You can also use normal functions instead of lambda functions)

 Input List=[2,70,11,10,17,23,31,77]
 List after filter=[2,11,17,23,31]
 List after map=[4,22,34,46,62]
 output of reduce=62


'''
from functools import reduce


def checking_prime_num(num):
    if (num<1):
        return False
    elif (num>1):
        for i in range(2,int(num/2)+1):
            if((num%i)==0):
                return False
        
        else:
            return True
def Mult_by_2(num):
    return num*2
def max_from_list(self,num):
    max=0
    if(num>max):
        max=num

    return max

 
def main():
    Input_List=[]
    size=int(input("Enter how many elements you want to enter in the list : "))
    for i in range(size):
        num=int(input())
        Input_List.append(num)
    print("Input List",Input_List)

    List_after_filter=(list(filter(checking_prime_num,Input_List)))

    print("List after filter",List_after_filter)
    List_after_map=list(map(Mult_by_2,List_after_filter))

    print("List after map",List_after_map)
    List_after_reduce=reduce(max_from_list,List_after_map)

    print("List after reduce",List_after_reduce)

    

if __name__=="__main__":
    main()