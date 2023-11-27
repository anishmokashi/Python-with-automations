class HDFC:
    ROI = 9.5       # Class variable

    def __init__(self,Name,Amount):  # Constructor
        self.AccountHolder = Name   # Instance Variable
        self.Balance = Amount       # Instance Variable
        print("Welcome ",self.AccountHolder)
        print("Your Account gets succesfully created with initial balance : ",self.Balance)

    def DisplayBalance(self):       # Instance methos
        print("Hello ",self.AccountHolder)
        print("Your account balance is : ",self.Balance)

    def Withdraw(self,Amount):      # Instance method
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance = self.Balance-Amount
            print("Amount withdawal succesfully...")

    def Deposit(self,Amount):       # Instance method
        self.Balance = self.Balance + Amount
        print("Amount deposited succesfully...")

    @classmethod
    def DisplayBankInfo(cls):       # Class method
        print("Welcome to HDFC bank portal")
        print("Our bank is PVT LTD bank")
        print("We provide the Rate Of Intrest on saving account is : ",cls.ROI)
        
    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI you should provide below documents for KYC")
        print("Your Aadhar card")
        print("Your PAN card")
        print("Your Passport size photo")

def main():
    print("ROI of HDFC bank is : ",HDFC.ROI)

    HDFC.DisplayBankInfo()

    HDFC.DisplayKYCInfo()

    print("Createing new account ...")
    Amit = HDFC("Amit",5000)   # __init__(100,"Amit",5000)

    print("Createing new account ...")
    Sagar = HDFC("Sagar",3000)   # __init__(200,"Sagar",3000)

    print("Performing operations on Amit's Account")
    Amit.Deposit(2000)
    Amit.DisplayBalance()

    Amit.Withdraw(1000)
    Amit.DisplayBalance()

    print("Performing operations on Sagar's Account")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()

    Sagar.Withdraw(500)
    Sagar.DisplayBalance()

if __name__ == "__main__":
    main()