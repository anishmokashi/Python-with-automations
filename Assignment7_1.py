''' Design python application which creates two thread named as even and odd.
    Even thread will display first 10 even numbers and odd thread will display first 10
    odd numbers. 
'''
import threading
def Even():
    for i in range(1,21):
        if(i%2==0):
            print(i)

def Odd():
    for i in range(1,21):
        if(i%2!=0):
            print(i)
def main():
    t1=threading.Thread(target=Even)
    
    t2=threading.Thread(target=Odd)
    

    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__=="__main__":
    main()