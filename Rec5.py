i = 0

def Display():
    global i
    print("Inside Display",i)
    i+=1
    Display()
    
def main():
    Display()

if __name__ == "__main__":
    main()