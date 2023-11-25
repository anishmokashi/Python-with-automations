''' write a program which accept n numbers from user and store it into list.Return maximum number from that list
Input: Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
'''
def Maximum_of_listElements( Element_list ):
    Max=Element_list[0]
    for E in Element_list:
        if (E>Max):
            Max=E

    return Max
def main():
    List=[]
    Elements=int(input("Enter how many elements you want to store in the list : "))
    for i in range(Elements):
       element=int(input())
       List.append(element)
    print("Max element in the list is :",Maximum_of_listElements(List))
    

if __name__=="__main__":
    main()