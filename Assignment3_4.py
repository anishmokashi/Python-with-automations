''' write a program which accept n numbers from user and store it into list.Accept one another number from user 
and return frequency of that number from list.
Input :Number of Elements :11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Input Element to find freq :5
Output : 3
'''
def Freq_of_numb(List,Num):
    Freq=0
    for i in List:
        if (Num==i):
            Freq=Freq+1
    return Freq

def main():
    Numbers=[]
    Size_of_list=int(input("Enter how many elements you want to store in the list"))
    for i in range(Size_of_list):
        numn=int(input())
        Numbers.append(numn)
    numb_to_count_freq=int(input("Enter which numbers frequency you want to find in that list"))
    print("Number of ",numb_to_count_freq,"in list are :",Freq_of_numb(Numbers,numb_to_count_freq))


   
    

if __name__=="__main__":
    main()