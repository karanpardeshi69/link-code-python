name  = "Ram"
print(name) 
print(id(name))
print(name[0])  
name = "Sita"
print(name[0])  
print(name)
print(id(name))

for i in name:
    print(i)
x = "Maharashtra"
print(len(x))

for i in range(len(x)-1,-1,-1):
    print(x[i],end="")
print()
# count len without len 
count = 0
for i in x:
    count += 1
print(count)

# string methods
x = "India is my country"
print(x.upper())
print(x.lower())
print(x.title())
print(x.capitalize())
print(x.swapcase())
print(x.replace("ndia","NDIA"))
print(x.replace(" ","_"))
print(x.count("i"))
print(x.index("i"))
print(x.find("v"))
y = x.replace(" ","_")
print(y.split("_"))

## Checking methods
print(x.isupper())
print(x.islower())
print(x.isdigit())
print(x.isalpha())
print(x.isdigit())
print(x.startswith("I"))
print(x.endswith("y"))