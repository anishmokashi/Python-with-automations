''' Design python application which creates three threads as small,capital,digits.
All the threads accepts string as parameter.Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of digits.
Display id and name of each thread.'''
import threading
def small(str):
     small_cnt=0
     for i in str:
         if(i<='z'and i>='a'):
             small_cnt=small_cnt+1
     print("count of small letters is",small_cnt)
def capital(str):
     capital_cnt=0
     for i in str:
         if(i>='A'and i<='Z' ):
             capital_cnt=capital_cnt+1
     print("count of capital letters is",capital_cnt)

def digits(str):
     digits_cnt=0
     for i in str:
         if(i<='9' and i>='1'):
             digits_cnt=digits_cnt+1
     print("count of digits is",digits_cnt)

def main():
    list='Marvellous_Infosystems@123'

    Thread1=threading.Thread(target=small,args=(list,))
    print("Thread id - ",threading.get_ident())
    print("Thread name - ",Thread1.name)
    Thread1.start()
    Thread1.join()
    Thread2=threading.Thread(target=capital,args=(list,))
    print("Thread id - ",threading.get_ident())
    print("Thread name - ",Thread2.name)
    Thread2.start()
    Thread2.join()
    Thread3=threading.Thread(target=digits,args=(list,))
    print("Thread id - ",threading.get_ident())
    print("Thread name - ",Thread3.name)
    Thread3.start()
    Thread3.join()

if __name__=="__main__":
    main()
