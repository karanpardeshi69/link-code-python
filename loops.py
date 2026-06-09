# fruits = ["Apple","Grapes","Pineapple"]
# for f_name in fruits:
#     print(f_name,end=" ")

# no = [1,2,3,4,5,6]
# for i in no:
#     print(i,end = " ")

# s = "India"
# for i in s:
#     print(i,end=" ")

# #print 1-5
# for i in range(1,6):
#     print(i,end=" ")

# #print 10-1
# for i in range(10,0,-1):
#       print(i,end=" ")

# st = int(input("Enter starting number:"))
# end = int(input("Enter ending number:"))
# count = 0
# for i in range(st,end+1):
#     if i%5==0 and i%7==0:
#         print(i)
#         count+=1

# print("count:",count)

for i in range(1,6):
    if i==4:
        continue;
    print(i)


for i in range(1,6):
    if i==4:
        print("Thanks")
        break;
    print(i)
