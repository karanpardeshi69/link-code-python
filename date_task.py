import datetime

print("Enter info for person1:")
year1 = int(input("Enter birth year:"))
month1 = int(input("Enter birth month:"))
day1 = int(input("Enter birth day:"))
person1 = datetime.date(year1,month1,day1)
print("--------------------------------------------------------------------------------------------------------------")
print("Enter info for person2:")
year2 = int(input("Enter birth year:"))
month2 = int(input("Enter birth month:"))
day2= int(input("Enter birth day:"))
person2 = datetime.date(year2,month2,day2)
if person1 > person2:
    print("Person 1 has the greater date")
elif person2 > person1:
    print("Person 2 has the greater date")
else:
    print("Both have the same date")   