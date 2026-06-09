num =9
sq = num*num
sum = 0
while sq>0:
    rem = sq % 10
    sum += rem
    sq //= 10

if sum == num:
    print("neon")
else:
    print("hattt")
