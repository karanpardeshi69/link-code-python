for i in range(3):
    for j in range(3):
        if (i + j) % 2== 0:
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
print()

ch =  97
for i in range(3):
    for j in range(3):
        print(chr(ch),end=" ")
    print()
    ch+=1
print()

ch = 97
for i in range(3):
    for j in range(4):
         print(chr(ch),end=" ")
         ch+=1
    print()
   
print()
num = 9
for i in range(3):
    for j in range(3):
        print(num,end=" ")
        num-=1
    print()
print()

for i in range(1,6):
    for j in range(1,6):
        if ((i == 1 or i==5 or j==1 or j == 5)) or (i ==3 and j == 3):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print()