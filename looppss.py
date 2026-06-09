# num = 12345
# sum = 0
# while num > 0:
#     rem = num %10
#     sum = sum+ rem
#     num //= 10
# print("sum of numbers is:", sum)

# num = 12345
# rev = 0
# while num > 0:
#     rem = num %10
#     rev = rev * 10+ rem
#     num //= 10
# print("reversed number is:", rev)


# num  = int(input("Enter number"))
# temp = num
# rev = 0
# while num > 0:
#     rem = num %10
#     rev = rev * 10+ rem
#     num //= 10
# if temp == rev:      
#      print("number is palindrome")
# else:
#         print("number is not palindrome")
# print("reversed number is:", rev)

num = int(input("Enter number"))
ct = 0
temp = num
while temp > 0:
    ct += 1
    temp //= 10
print("count ",ct)
temp = num
sum = 0
while temp > 0:
    rem = temp %10
    sum += rem ** ct
    temp//=10

if num == sum:
    print("armstrong")
else:
    print("not armsteong")

print(sum)
