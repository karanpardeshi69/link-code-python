class bank:
    def __init__(self,acc_no,acc_holder,balance):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = balance

    def check_bal(self):
        print(f"Available balance is:{self.balance}\n--------------------")

    def deposite(self):
        val = int(input("Enter amount to deposite:"))
        self.balance += val
        print(f"Amount {val} is credited in your account..!!\nnow your balance is :{self.balance}.\n--------------------")
    
    def withdraw(self):
        val = int(input("Enter amount to Withdraw:"))
        if val <= self.balance:
            self.balance -= val
            print(f"Amount {val} is debited from your account..! \nnow your balance is :{self.balance}.\n--------------------")
        else:
            print("Insufficient funds\n")

# user = bank(121,"Karan",500)
# user.check_bal()
# user.deposite()
# user.withdraw()
# user.check_bal()