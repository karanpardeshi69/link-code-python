class bank:
    bank_name = "SBI"
    ifsc = "SBI15099"

    def __init__(self,name,bal,mail):
        self.name = name
        self.bal = bal
        self.mail = mail

    def show_details(self):
        print(f"name :{self.name}\nbal :{self.bal}\nmail :{self.mail}\nbankname :{self.bank_name}")

    def check_bal(self):
        print("Available balance is:",self.bal)

    def deposite(self,val):
        self.bal += val
        print(f"Amount {val} is credited in your account..!!\nnow your balance is :{self.bal}.\n")
    
    def withdraw(self,val):
        if val <= self.bal:
            self.bal -= val
            print(f"Amount {val} is debited from your account..! \nnow your balance is :{self.bal}.\n")
        else:
            print("Insufficient funds\n")
    
    def fd(self):
        val = int(input("FD amount : "))
        dur = int(input("how many months??"))
        if dur == 3:
            print(f"for amount{val} you will get '7%'return with total amout of {val*0.07}Extra")
        elif dur == 6:
            print(f"for amount{val} you will get '9%'return with total amout of {val*0.09}Extra")
        elif dur == 9:
            print(f"for amount{val} you will get '12%'return with total amout of {val*0.12}Extra")
        elif dur == 12:
            print(f"for amount{val} you will get '15%'return with total amout of {val*0.15}Extra")
            
        
        

u1 = bank("Karan",500,"karanp@gmail.com")
u1.show_details()   
print("-----------------------------------")
# u1.check_bal()     
# u1.deposite(100)
# u1.withdraw(2000)
# u1.check_bal()
# print("-----------------------------------")
#u1.fd()
u2 = bank("Tejas",5000,"tejas@gmail.com")
u2.show_details()  

x = [u1,u2]
max = 1
str = ""
for i in x:
    if i.bal >= max:
        max = i.bal
        str = i
print("---------------------------------")
print("max balance:",max)
print("details:")
str.show_details()
    
