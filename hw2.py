for i in range(5):
    for j in range(5):
        if (i ==0 or j == 4 or j ==0 or i == 4 or i ==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

for i in range(1,4):
    print("*"*i)
for j in range(2,0,-1):
    print("*"*j)

print()

num = 1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
    print()
    num += 2

num = 5
for i in range(3,0,-1):
    for j in range(i):
        print(num,end="")
    print()
    num -= 2

print()

n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or i+j == 2 or i-j==2: 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

