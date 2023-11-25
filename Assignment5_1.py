''' Write a program which contains one class as Demo.
Demo class contains two instance variables as no1,no2.
That class contains one class variable as value.
There are two instance methods of class as fun and gun which displays values of instance variables.
Initialise instance vairable in init method by accepting the values from user.

After creating the class create the two objects of demo class as
Obj1=Demo(11,21)
Obj2=Demo(51,101)

Now call the instance methods as 
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
'''
class Demo:
    Value=3.14
    def __init__(self,num1,num2):
        self.no1=num1
        self.no2=num2
    def Fun(self):
        print("Printing instance variables from fun",self.no1," ",self.no2)
    def Gun(self):
        print("Printing instance variables from Gun",self.no1," ",self.no2)
    
def main():
    numb1=int(input("Enter value for object 1 number 1 : "))
    numb2=int(input("Enter value for object 1 number 2 : "))
    Obj1=Demo(numb1,numb2)
    numb1=int(input("Enter value for object 2 number 1 : "))
    numb2=int(input("Enter value for object 2 number 2 : "))
    Obj2=Demo(numb1,numb2)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

    print("Printing instance variable for object 1 :",Demo.Value)
    print("Printing instance variable for object 2 :",Demo.Value)

if __name__=="__main__":
    main()