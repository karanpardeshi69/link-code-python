from parent1 import p1
from parent2 import p2

class child(p1,p2):
    def __init__(self,c_name, p1_name,p2_name):
        self.c_name = c_name
        p1.__init__(self,p1_name)
        p2.__init__(self,p2_name)

obj = child("Karan","Chandan","Manisha")
print(obj.c_name)
print(obj.p1_name)
print(obj.p2_name)