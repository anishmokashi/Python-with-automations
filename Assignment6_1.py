''' Write a program which contains one class named as BookStore.
BookStore class contains two instance variables as Name , Author.
That class contains one class variable as BoOfBooks which is initialise to 0.
There is one instance methods of class as Display which displays name,Author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.

After creating the class create the two objects of BookStore class as
Obj1=BookStore("Linux System programming","Robert Love")
Obj1.Display() #Linnux System Programming by Robert Love.No of books : 1

Obj2=BookStore("C Programming","Dennis Ritchie")
Obj2.Display() # C Programing by Dennis Ritchie . No of Books : 2
'''
class BookStore:
    NoOfBooks=0
    def __init__(self,str1,str2):
        self.Name=str1
        self.Author=str2
        BookStore.NoOfBooks=BookStore.NoOfBooks + 1


    def Display(self):
        print("Name : ",self.Name)
        print("Author : ",self.Author)
        print("Number of Books : ",BookStore.NoOfBooks)

def main():
    Obj1=BookStore("Linux System programming","Robert Love")
    Obj1.Display()
    
    Obj2=BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__=="__main__":
    main()
