from savings_account import savings_acc
class premimum(savings_acc):
    def __init__(self, acc_no, acc_holder, balance):
        super().__init__(acc_no, acc_holder, balance)

    def calculate_benefits(self):
        if self.balance >= 5000:
            benefits = 500
            print(f"u earn rs {benefits} till now..!")
            ch = input("Do u want to add this is in your account?? (y/n)")
            if ch == "y":
                self.balance += benefits
                print(f"{benefits} rs successFully added to you account balance..!!\n Now you account balance is {self.balance}\n--------------------")
            else:
                print("Ok..thats fine.. you can add your reward whenever you want..\n--------------------")
        else:
            print("Maintain basic limit of premimum Account rs 5000\n--------------------")

# user3 = premimum(123,"Kiran",7000)
# user3.calculate_benefits()