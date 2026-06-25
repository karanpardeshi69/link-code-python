s1 = {12,35,8,25,5}
s2 = {25,6,35,15,8}
all = s1.union(s2)
common = s1.intersection(s2)
print(common)
print(all)
print("divisible by 5 :")
for i in all:
    if i % 5 == 0:
        print(i,end=" ")

print()


sum = 0
for i in all:
    if i %2 ==0:
        sum+=i
print("Even number sum",sum)

common_sum = 0
for i in common:
    common_sum +=i

print("Sum of common",common_sum)
sq  = common_sum * common_sum 
print("Square of common sun",sq)
cube = sq*sq*sq
print("Cube of the sqaure of common sum",cube)

mul = 1
for i in all:
    mul*=i
print("multipliaction of non repeating values ",mul)
