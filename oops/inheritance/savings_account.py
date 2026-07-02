from bank_account import bank
class savings_acc(bank):
    def __init__(self, acc_no, acc_holder, balance,):
        super().__init__(acc_no, acc_holder, balance)
        #elf.interest_rate = self.interest_rate

    def calculate_interest(self):
        amt = int(input("Enter amount to calculate:"))
        mon = int(input("1. 3 mon\n2. 6 mon\n3. 9 mon\n4. 12 mon\nEnter months:"))
        self.interest = 0
        if mon == 3:
            self.interest = amt*0.07
            print(f"for amount{amt} you will get '7%'return with total amout of {self.interest}Extra\n--------------------")
        elif mon == 6:
            self.interest = amt*0.09
            print(f"for amount{amt} you will get '9%'return with total amout of {self.interest}Extra\n--------------------")
        elif mon == 9:
            self.interest = amt*0.12
            print(f"for amount{amt} you will get '12%'return with total amout of {self.interest}Extra\n--------------------")
        elif mon == 12:
            self.interest = amt*0.15
            print(f"for amount{amt} you will get '15%'return with total amout of {self.interest}Extra\n--------------------")

        ch = input("You want to apply this interest?? (Y/N):")
        if ch == "Y":
            self.balance += self.interest
        else:
            print("thanks \n--------------------")


#user1 = savings_acc(121,"karan",500)
# user1.check_bal()
# user1.deposite()
# user1.withdraw()
# user1.calculate_interest()
# user1.check_bal()
