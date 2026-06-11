# hello ---> olleh
str = "hello"
print("Reversed string 'hello':",end=" ")
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

print()
# evenchar ,oddchar,vowels
x = "Maharashtra"
even_char =0
odd_char = 0
for i in range(len(x)):
    if (i+1) % 2==0:
        even_char+=1
    else:
        odd_char+=1
print("Even count",even_char)
print("Odd count",odd_char)
print("Vowels:")
for i in x:
    if i in "aeiou":
        print(i,end=" ")
print()

# hello into HELLO
small = "abcdefghijklmonpqrstuvwxyz"
capital ="ABCDEFGHIJKLMONPQRSTUVWXYZ"
result = ""
x = "hello"
for ch in x:
    for i in range(len(small)):
        if ch == small[i]:
            result += capital[i]
            break
print("Capitalize string :",result)

# whitespace remove
x = " hey"
result = ""
for ch in x:
    if " " not in ch:
        result += ch

print("without white space:",result)
        
# letter replace
x = "python programming"
result = ""
for i in x:
    if i == "p":
        result += "x"
    else:
        result += i
print("Letter replaced ",result)