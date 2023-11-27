
def Add(A, B):  # 0x1027fbeb0
    return A+B

# Function accepts parameters as another function
def Marvellous(FPTR):
    print(type(FPTR))
    print(FPTR)
    Ans = FPTR(11,7)    # Ans = 0x1027fbeb0(11,7)
    print("Addition is : ",Ans)

def main():
    Marvellous(Add) # Marvellous(0x1027fbeb0)

if __name__ == "__main__":
    main()