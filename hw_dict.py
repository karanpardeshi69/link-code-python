stud = {
    101: {"Name": "Karan", "Age": 21, "Sub": ["Math", "Eng", "Sci"], "Marks": [78, 89, 65]},
    102: {"Name": "Aryan", "Age": 21, "Sub": ["Math", "Eng", "Sci"], "Marks": [67, 98, 56]},
    103: {"Name": "Tejas", "Age": 21, "Sub": ["Math", "Eng", "Sci"], "Marks": [58, 67, 45]},
}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Total marks and percentage")
    print("4. Topper & Lower")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    match ch:

        case 1:
            sid = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            sub = []
            marks = []

            for i in range(3):
                s = input("Enter Subject: ")
                m = int(input("Enter Marks: "))
                sub.append(s)
                marks.append(m)

            stud[sid] = {
                "Name": name,
                "Age": age,
                "Sub": sub,
                "Marks": marks
            }

            print("Student Added Successfully")
        case 2:
                    for sid, data in stud.items():
                        print("\nID:", sid)
                        print("Name:", data["Name"])
                        print("Age:", data["Age"])
                        print("Subjects:", data["Sub"])
                        print("Marks:", data["Marks"])
        case 3:
            print("\n1. Total Marks of One Student")
            print("2. Total Marks of All Students")
            print("3. Percentage of One Student")
            print("4. Percentage of All Students")

            op = int(input("Enter Option : "))

            match op:

                case 1:
                    sid = int(input("Enter ID : "))
                    if sid in stud:
                        total = sum(stud[sid]["Marks"])
                        print("Total Marks =", total)
                    else:
                        print("Student Not Found")

                case 2:
                    for sid, data in stud.items():
                        total = sum(data["Marks"])
                        print(sid, data["Name"], "=", total)

                case 3:
                    sid = int(input("Enter ID : "))
                    if sid in stud:
                        total = sum(stud[sid]["Marks"])
                        per = total / len(stud[sid]["Marks"])
                        print("Percentage =", per)
                    else:
                        print("Student Not Found")

                case 4:
                    for sid, data in stud.items():
                        total = sum(data["Marks"])
                        per = total / len(data["Marks"])
                        print(sid, data["Name"], "=", per, "%")

                case _:
                    print("Invalid Option")
        case 4:
            print("\n1. Topper")
            print("2. Lowest")

            op = int(input("Enter Choice : "))

            print("\n1. Overall")
            print("2. Math")
            print("3. Eng")
            print("4. Sci")

            sub = int(input("Enter Choice : "))

            match op:

                case 1:  # Topper

                    match sub:

                        case 1:
                            sid = max(stud, key=lambda x: sum(stud[x]["Marks"]))

                        case 2:
                            sid = max(stud, key=lambda x: stud[x]["Marks"][0])

                        case 3:
                            sid = max(stud, key=lambda x: stud[x]["Marks"][1])

                        case 4:
                            sid = max(stud, key=lambda x: stud[x]["Marks"][2])

                        case _:
                            print("Invalid Choice")
                            continue

                    print("ID :", sid)
                    print("Name :", stud[sid]["Name"])

                case 2:  # Lowest

                    match sub:

                        case 1:
                            sid = min(stud, key=lambda x: sum(stud[x]["Marks"]))

                        case 2:
                            sid = min(stud, key=lambda x: stud[x]["Marks"][0])

                        case 3:
                            sid = min(stud, key=lambda x: stud[x]["Marks"][1])

                        case 4:
                            sid = min(stud, key=lambda x: stud[x]["Marks"][2])

                        case _:
                            print("Invalid Choice")
                            continue

                    print("ID :", sid)
                    print("Name :", stud[sid]["Name"])

                case _:
                    print("Invalid Choice")
