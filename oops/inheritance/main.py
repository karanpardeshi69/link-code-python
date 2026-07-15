from premimumSA import premimum

while True:
    ch = int(input("Welcome to the BABA bank...!\n1.ADMIN\n2.USER\n3.EXIT\n"))
    match ch:
        case 1:
            while True:
                ch1 = int(input("Welcome ADMIN..\n1.create user\n2.get balance\n3.check interest\n4.check benfits\n5.exit"))
                match ch1:
                    case 1:
                        name = input("Enter user name:")
                        acc_no = int(input("Enter user account no:"))
                        balance = int(input("Enter amount to add in users account:"))
                        user = premimum(acc_no,name,balance)
                        print("UsersAccount created successfully...!\n--------------------")
                    case 2:
                        user.check_bal()
                    case 3:
                        user.calculate_interest()
                    case 4:
                        user.calculate_benefits()
                    case 5:
                        print("Thank You ..!! admin")
                        break
        case 2:
            while True:
                ch1 = int(input("welcome USER..\n1.create account\n2.Withdraw\n3.Deposite\n4.Get balance\n5.Exit"))
                match ch1:
                    case 1:
                        name = input("Enter your name:")
                        acc_no = int(input("Enter your account no:"))
                        balance = int(input("Enter amount to add in account:"))
                        user = premimum(acc_no,name,balance)
                        print("Account created successfully...!\n--------------------")
                    case 2:
                        user.withdraw()
                    case 3:
                        user.deposite()
                    case 4 :
                        user.check_bal()
                    case 5:
                        print("Thank you....!!User")
                        break