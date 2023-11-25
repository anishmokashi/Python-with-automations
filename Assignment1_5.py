# write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1 


def Display():
   for i in range(10,0,-1):
       print(i,end=" ")
def main():
    Display()
    

if __name__=="__main__":
    main()