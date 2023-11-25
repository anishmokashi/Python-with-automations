'''write a program which accept n numbers from user and store it into list.Return maximum number from that list
Input: Number of elements :4
Input Elements : 13 5 45 7 
Output : 5
'''
def Minimum_of_listElements( Element_list ):
    Min=Element_list[0]
    for E in Element_list:
        if (E<Min):
            Min=E

    return Min
def main():
    List=[]
    Elements=int(input("Enter how many elements you want to store in the list : "))
    for i in range(Elements):
       element=int(input())
       List.append(element)
    print("Min element in the list is :",Minimum_of_listElements(List))
    

if __name__=="__main__":
    main()