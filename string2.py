print("Given String : 'INDIA IS MY COUNTRY' ")
ch = input("Enter a character to count in the string : ")
ct = 0
for i in "INDIA IS MY COUNTRY":
    if i == ch:
        ct += 1

print("Count of character ",ch," is : ",ct)
        