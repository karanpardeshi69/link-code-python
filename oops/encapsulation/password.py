import random as r
import time
class user_login:
    def __init__(self):
        self.mob_no = ""
        self.__otp = None
        self.__attempt = 0

    def check_attempt(self):
        if self.__attempt<3:
            self.check_login()

    def check_login(self):
        self.mob_no = input("Enter your Mobile number")
        if len(self.mob_no) == 10 and self.mob_no.isdigit():

            self.__otp = r.randint(1000,9999)
            self.sending_time = time.time()
            print("Your otp is :",self.__otp)
            otp = int(input("Enter your OTP:"))
            self.current_time = time.time()
            if self.current_time - self.sending_time > 10:
                print("OTP Expired...!")
                ch = input("do yo want to resend otp?(y/n)")
                if ch == "y":
                    


                return
            if otp == self.__otp:
                print("WELCOME...!!")
                return
            else:
                print("OTP not matched..")
                self.__attempt+=1
                print("ATTEMPST LEFT",3-self.__attempt)
                if self.__attempt ==3:
                    print("Attempt reached.. trry after some time")
                    return
                self.check_attempt()
        else:
            print("Enter valid number")

obj = user_login()
obj.check_login()