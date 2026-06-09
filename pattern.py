#n = int(input("Enter number"))
# i =1
# while i <= n:
#     j = 1
#     while  j <= n:
#         print("*",end=" ")
#         j+=1
#     i+=1
#     print()

i = 1
k =1
for i in range(3):
    j = 1
    for j in range(3):
        print(k,end=" ")

    k+=1
    print()

print()

i = 1
k =1
for i in range(3):
    j = 1
    for j in range(3):
        print(k,end=" ")
        k+=1

    print()

print()

i = 1
for i in range(3):
    j = 1
    for j in range(3):
        if i == j:
             print(1,end=" ")
        else:
            print(0,end=" ")

    print()

print()

i = 1
n = 4
for i in range(1,n+1):
    j = 1
    for j in range(1,n+1):
        if i == 2 or j == 3:
             print(" ",end=" ")
        else:
            print("X",end=" ")

    print()



