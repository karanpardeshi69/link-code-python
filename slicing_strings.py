x  = "India"
print(x[0:5:2])
print(x[0:3])
print(x[1:4])
print(x[0:5:2])
print(x[1:4])
print()
x = "India is my country!"
print(x[6:8])
print(x[12:17])
print(x[7:10])
print(x[16:])
print(x[-10:-15:-1])
print(x[::-1])
 
# str1  = input("Enter string to check its pall or not : ")
# if str1 == str1[::-1]:
#     print("its pallindrome")
# else:
#     print("its not pallindrome")

x = "1234abcdefg"
ct_dig = 0
ct_letter = 0

for ch in x:
    if ch >= "0" and ch <= "9":
        ct_dig+=1
    elif (ch>="a" and ch <= "z") or (ch>="A" and ch <= "Z"):
        ct_letter += 1

print(f"count of  digit {ct_dig}\ncount of letter {ct_letter}")

x = "hello"
new_str = ""
for i in x:
    if i>="a" and i <="z":
        new_str += chr(ord(i)-32)
print(new_str)

x = "sWapCaSe"
new = ""
for i in x:
    if i>="A" and i <="Z":
        new += chr(ord(i)+32)
    elif i>="a" and i <="z":
        new += chr(ord(i)-32)
print(new)

x = "programming"
for i in x:
    if ord(i) % 2 !=0:
        print(i,ord(i))

unique = ""
for ch in x:
    if ch not in unique:
        unique+=ch 
print(unique)

x  = "I Like python programming"
ct = 1
for i in x:
    if i in " ":
        ct+=1
print("Count of words" , ct)