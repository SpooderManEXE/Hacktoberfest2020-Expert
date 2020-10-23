class Deposit: 
    def __init__(self, deposit = 0): 
         self._deposit = deposit 
      
    def getDeposit(self): 
        return self._deposit 
      
    def setDeposit(self, deposit): 
        self._deposit = deposit 

class Withdraw:
    
    def __init__(self, withdraw = 0): 
         self._withdraw = withdraw 
      
    def getWithdraw(self): 
        return self._withdraw 
      
    def setWithdraw(self, withdraw): 
        self._withdraw = withdraw 

class Balance:

    def __init__(self, balance = 0): 
         self._balance = balance 
      
    def getBalance(self): 
        return self._balance 
      
    def setBalance(self, balance): 
        self._balance = balance 

class Exit:
    def exitMachine(self):

        print("Thank for using Simple ATM")
        exit()
        

bal = Balance()
wit = Withdraw()
dep = Deposit()

class Index:

    def otherSelection():

        print("Try Another Transaction?")
        select=int(input("Press [1] Yes \t Press [2] No\t"))
        if select == 2:
            Exit().exitMachine()
        elif select == 1:
            print()

    def checkBalance():

        if bal.getBalance() == 0:
            print("Your current balance is zero.")
            print("You need to deposit money first.")
        elif bal.getBalance()-wit.getWithdraw() <10:
            print("You do not have sufficient money to withdraw.")
            print("You need to deposit money first.")
        elif wit.getWithdraw() >= bal.getBalance():
            print("The amount you withdraw is greater than to your balance.")
        else:
            balance_amount =  bal.getBalance()-wit.getWithdraw()
            bal.setBalance(balance_amount)


    print("Welcome to simple ATM")
    loop = 1
    while loop == 1:
        print("\nPlease Select ATM Transactions")
        print("Press [1] Deposit")
        print("Press [2] Withdraw")
        print("Press [3] Balance Inquiry")
        print("Press [4] Exit")
        while True:
            try:
                select=int(input("What would you like to do?\t"))
                break
            except ValueError:
                print("Please input number of selection!")
        if select == 1:

            print("Select 1")
            deposit_amount = int(input("Enter amount of money to deposit\t"))
            dep.setDeposit(deposit_amount)

            balance_amount =  bal.getBalance()+dep.getDeposit()
            bal.setBalance(balance_amount)
            print("Your Balance is {}".format(bal.getBalance()))
            print()
            otherSelection()

        elif select == 2:

            print("Select 2")
            withdraw_amount = int(input("Enter amount of money to withdraw\t"))
            wit.setWithdraw(withdraw_amount)
            checkBalance()
            print("Your Balance is {}".format(bal.getBalance()))
            print()
            otherSelection()

        elif select == 3:

            print("Select 3")
            print("Your Balance is {}".format(bal.getBalance()))
            otherSelection()

        elif select == 4:

            Exit().exitMachine()
            loop = 0
        else:

            print("Try Another Selection?")
            select=int(input("Press [1] Yes \t Press [2] No\t"))
            if select == 2:
                Exit().exitMachine()
                loop = 0
            elif select == 1:
                loop == 1