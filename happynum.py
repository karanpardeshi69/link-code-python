for num in range(201, 5001):
    temp = num

    while temp != 1 and temp != 4:
        s = 0

        while temp > 0:
            rem = temp % 10
            s += rem * rem
            temp //= 10

        temp = s

    if temp == 1:
        print(num,end=",")