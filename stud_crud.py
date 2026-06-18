stud = [
    [101,"ram",90],
    [102,"laxman",89],
    [103,"bharat",85],
    [104,"shatrughna",79]
]
while True:
    print("Student Management System \n1.Add \n2.View \n3.Update \n4.Delete \n5.Topper \n6.exit")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            stud.append([roll, name, marks])

            print("Student Added Successfully!")
        case 2:
            for i in stud:
                print(i)
        case 3:
            sid = int(input("Enter your id:"))
            for i in stud:
                if sid == i[0]:
                    print("1.Update marks\n2.Update name \n3.All details \n4.Exit")
                    choice = int(input("Enter your choice:\n"))
                    if choice==1:
                        ex_marks = i[2]
                        new_marks = int(input("Enter New marks to update:"))
                        i[2]=new_marks
                        print(f"{ex_marks} updated to {new_marks} marks")
                    elif choice==2:
                        ex_name = i[1]
                        new_name = input("Enter New Name to update:")
                        i[1] = new_name
                        print(f"{ex_name} updated to {new_name}.")
                    elif choice == 3:
                        ex_marks = i[2]
                        new_marks = int(input("Enter New marks to update:"))
                        i[2]=new_marks
                        print(f"{ex_marks} updated to {new_marks} marks")
                        ex_name = i[1]
                        new_name = input("Enter New Name to update:")
                        i[1] = new_name
                        print(f"{ex_name} updated to {new_name}.")
                    elif choice == 4:
                        pass
        case 4:
            sid = int(input("Enter your id to Delete:"))
            for i in stud:
                if sid == i[0]:
                    stud.remove(i)
            print(f"Record of {sid} removed")



                    




