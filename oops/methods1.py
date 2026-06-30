class demo:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
    #instant method
    def welcome(self):
        return "Hello Students...!"
    
    def modify(self):
        new = input("Enter new name:")
        ex_name = self.name
        self.name = new
        print(f"existing name {ex_name}, updated name {new}.")

s1 = demo("karan",21,19)
print(s1.name,s1.id,s1.age)
print(s1.welcome())
s1.modify()