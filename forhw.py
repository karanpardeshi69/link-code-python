for i in range(1, 6):
    print("\nStudent", i)

    total = 0

    for j in range(5):
        mark = int(input("Enter mark: "))
        total += mark

    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Total =", total)
    print("Percentage =", percentage)
    print("Grade =", grade)