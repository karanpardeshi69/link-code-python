import math
import random as r
import datetime 
#math
print(math.sqrt(5))
print(math.factorial(6))
print(math.ceil(45.23))
print(math.floor(34.77))
print(math.pow(3,2))
print(math.pi)

calc = 2*math.pi*12
print(calc)
print("--------------------------------------------------------------------------------------------------------------")
#random
print(r.randint(1000,9999))
print(r.random())
print(r.randrange(1,20,2))
x = ["red","blue","yellow","black"]
print(r.choice(x))
print(r.choices(x,k=2))
r.shuffle(x)
print(x)
print("--------------------------------------------------------------------------------------------------------------")
#date & time
d = datetime.datetime.now()#timetsamp
print(d)
print(d.time())
print(d.day)
print(d.year)
print(d.month)
# date
today_date = datetime.date.today()
print(today_date)

#after days
after = today_date+datetime.timedelta(days=5)
print(after)

dob = datetime.date(2006,12,1)
cd = datetime.date.today()

print(cd-dob)
print(cd.year-dob.year)