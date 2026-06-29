class car:
    def __init__(self,name,model,wheels,price,avail_qty):
        self.brand = "BWM"
        self.name = name
        self.model = model
        self.wheels = wheels
        self.price = price
        self.avail_qty = avail_qty

car1  = car("M1","A1",4,2000,4)
car2 = car("M2","A2",4,3000,5)
car3 = car("M3","A3",3,30000,6)
car4 = car("M4","A4",4,3000,3)
car5 = car("M5","A5",4,5000,10)

x = [car1,car2,car3,car4,car5]
n = 0
for i in x:
    n +=1
    print("car :",n)
    print("Name:",i.name)
    print("Model:",i.model)
    print("No of Wheels:",i.wheels)
    print("Price:",i.price)
    print("Available Quantity:",i.avail_qty)
    print("----------------------------")

total = 0
for i in x:
    total += i.price * i.avail_qty

print("Total price of availble model:",total)

print()

print("Availabilty more than 5 and less than 10:")
for i in x:
    if i.avail_qty >= 5 and i.avail_qty <= 10:
        print(i.name,i.avail_qty)





