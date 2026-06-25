x = {1, 2, 3, 4, 5}
print(x,type(x))

x = set()
x.add(10)
x.add(20)
print(x,type(x))

x = {10,20,30,40,50,60,60,70,80,90,100}
print(x)
#loop
for i in x:
    print(i)
#Functions(sum min max len) and methods
x.add(110)
x.remove(20)
x.discard(300)
print(x)

x.pop()
print(x)
x.clear()
print(x)

a = {1,2}
b = a.copy()
print(a,b)

a.update([3,4,5])
print(a,b)

print(sum(a),len(a),min(a),max(a))
print("----------------------------------------")
# set operations
a = {1,2,3}
b ={3,4,5}
print("Union",a.union(b))
print("----------------------------------------")

print("Intersection",a.intersection(b),a & b)
print("----------------------------------------")
print("Difference",a.difference(b),a-b)
print("----------------------------------------")
print("Symmetric Difference",a.symmetric_difference(b),a^b)
print("----------------------------------------")
print()

py_student = {"ram","sita","komal","ramu"}
java_student = {"ram","pawan","gita"}
fd_student ={"gita","komal","payal","ram"}
all_stud = py_student | java_student | fd_student
print(py_student | java_student | fd_student)
print("----------------------------------------")
print("Total count of students\n",len(py_student | java_student | fd_student))
print("----------------------------------------")
print("Studernts who are attending java & python\n",py_student & java_student)
print("----------------------------------------")
print("Only java batch students\n",java_student)
print("----------------------------------------")
print("Only python batch students\n",py_student)
print("----------------------------------------")
print("Name of students who are not attending java & python\n",fd_student - (py_student | java_student))
print("----------------------------------------")
print("count of who attending 3 batches at a time\n",len(py_student & java_student & fd_student))
print("----------------------------------------")
for stud in all_stud:
    ct = 0
    if stud == py_student:
        ct+=1
    elif stud == 
print("name of student who attending only one batch\n")
print("----------------------------------------")
