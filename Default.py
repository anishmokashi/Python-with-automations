
def Display(Name, Age, Marks = 90):
    print("Name is : ",Name)
    print("Age is : ",Age)
    print("Marks are : ",Marks)

def main():
    print("Demonstration of Keyword arguments")

    Display("Amit",23)
    Display("Sagar",22,78)
    
if __name__ == "__main__":
    main()
