class mobile:
    def __init__(self,uname,ubrand,ucolor,uprice):
        self.name = uname
        self.brand = ubrand
        self.color = ucolor
        self.price = uprice
    
obj = mobile("Iphone15","Apple","Black","1000")
obj2 = mobile("Iphone16","Apple","Blue","2000")
print(obj.name,obj.color,obj.brand,obj.price)
print(obj2.name,obj2.color,obj2.brand,obj2.price)
#store object inside list and access using loop
x = [obj,obj2]
for i in x:
    print(i.name)