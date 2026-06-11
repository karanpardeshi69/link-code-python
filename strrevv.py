str = "nayan"
rev = ""
print("Reversed string 'hello':",end=" ")
for i in range(len(str)-1,-1,-1):
    rev += str[i]
print(rev)
if str == rev:
    print("palidrome")
else:
    print("hatt")
