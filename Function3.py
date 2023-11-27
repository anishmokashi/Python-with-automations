
# Function accepts more parameter and return nothing
def Marvellous(Name, Age, City):
    print("Inside Marvellous Function")
    print("Welcome : ",Name)
    print("Your age is : ",Age)
    print("Your City is : ",City)

def main():
    Marvellous("Amit", 28, "Pune")
    Marvellous(City = "Mumbai", Age = 30, Name = "Sagar")

if __name__ == "__main__":
    main()