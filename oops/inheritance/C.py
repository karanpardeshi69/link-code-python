from P import p
class c(p):
    pqr = "byee"
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.makrs = marks

obj = c("karan",20,45)
print(obj.abc,obj.xyz,obj.pqr)
print(obj.name,obj.age,obj.makrs)