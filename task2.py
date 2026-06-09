# sum of 23 to 58
count=0
for i in range(23,59):
    count = count+i;
print("Sum of all nos form 23 to 58 :",count)
# table
num = int(input("Enter a number for table"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#7 factorial
fact = 1
for i in range(num,0,-1):
    fact *= i
print("Factorial of 7 is ",fact)
#5 fact
num = 5
for i in range(1,6):
    if num % i==0:
        print("factor of 5 ",i)