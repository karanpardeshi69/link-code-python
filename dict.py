x = {}
print(x,type(x))
x["rollno"] = 101
x["name"] = "Karan"
print(x)
# acess
print(x["name"])
# update 
x["rollno"] = 21
print(x["rollno"])

stud = {
    "roll no":101,
    "name":"Karan",
    "Age":21,
    "sub":["maths","english","science"],
    "marks":(89,76,90)
}
print(stud)
#methods
print(stud.keys())
print(stud.values())
print(stud.items())
print("-------------------------------------------")
# loop
for key in stud:
    print(key)
print("-------------------------------------------")
for values in stud.values():
    print(values)
print("-------------------------------------------")
for k,v in stud.items():
    print(k,v)
print("-------------------------------------------")
for i in stud:
    if i == "sub":
        for j in stud[i]:
            print(j)
print("-------------------------------------------")
for i in range(len(stud["sub"])):
    print(f"{stud["sub"][i]}---{stud["marks"][i]}")
print("-------------------------------------------")
# zip()
for sv ,mv in zip(stud["sub"],stud["marks"]):
    print(sv,mv)
print("-------------------------------------------")
