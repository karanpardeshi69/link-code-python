li = [1,2,3,56,4,3,223,54,56,7,8,97]
# flag = 0
# ip = int(input("Enter key to find"))
# for i in li:
#     if i == ip:
#         print("key found")
#         flag = 1
#         break
# if flag == 0:
#     print("key not found")

lii = []
for i in li:
    if li.count(i)>1 and i not in lii:
        lii.append(i)
print("Dupliacte eliments",lii)

print("Unique keys")
for i in li:
    if li.count(i)<=1:
        print(i)

