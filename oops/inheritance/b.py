from a import engine
class car:
    def __init__(self,uip):
        self.age = 90
        self.a = engine(uip)

obj = car(200)
print(obj.age,obj.a.name,obj.a.horsepower)
print(engine.brand)