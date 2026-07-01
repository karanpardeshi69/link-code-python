from a import engine
class car:
    def __init__(self):
        self.age = 90
        self.a = engine()

obj = car()
print(obj.age)
print(obj.a.name)