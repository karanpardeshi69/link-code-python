num = 18
sum = 0
while num >0:
    sum += num%10
    num//=10
if num % sum == 0:
    print("Harshal")
else:
    print("hatt")    
 