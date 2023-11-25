''' write a program which accept n numbers from user and store it into list.Return addition of all
elements from that list.

Input: Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
'''
def Addition_of_listElements( Element_list ):
    sum=0
    for E in Element_list:
        sum=sum+E
    return sum
def main():
    List=[]
    Elements=int(input("Enter how many elements you want to store in the list : "))
    for i in range(Elements):
       element=int(input())
       List.append(element)
    print("Summation of elements in the list are :",Addition_of_listElements(List))
    

if __name__=="__main__":
    main()