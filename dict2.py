stud = {
    101:{"Name":"Karan","Age":21,"Sub":["Math","Eng","Sci"],"Marks":[78,89,65]},
    102:{"Name":"Aryan","Age":21,"Sub":["Math","Eng","Sci"],"Marks":[67,98,56]},
    103:{"Name":"Tejas","Age":21,"Sub":["Math","Eng","Sci"],"Marks":[58,67,45]},
}
print(stud[101])
print(stud[101]["Sub"])
print(stud[101]["Sub"][2])
print(stud[102]["Marks"][2])
print("----------------------------------------------")
for v in stud.values():
    print("--------------------")
    for key in v:
        print(key)

print("----------------------------------------------")

for key in stud:
    for v in stud[key]["Marks"]:
        print(v,end=" ")
    print()

print("----------------------------------------------")
for key in stud:
    print("Student Id",key)
    for k,v in stud[key].items():
        print(F"{k}:{v}")
    print("----------------------------------------------")