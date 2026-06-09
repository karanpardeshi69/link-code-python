for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()

print()

for i in range(4,0,-1):
    for j in range(i):
        print(i,end="")
    print()
print()

for i in range(1,5):
    for j in range(i):
        if i %2 ==0:
            print(0,end="")
        else:
            print(1,end="")
    print()
print()

num = 1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
    print()
    num+=2

print()

num = 1
for i in range(4,0,-1):
    for j in range(i):
        print(num*num,end="")
    print()
    num+=1