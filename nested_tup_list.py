x = [10,[20,30],40,(50,60)]
print(x[2])
print(x[3][0])
print(x[1][1])
for i in x:
    if type(i) == list or type(i) == tuple:
        for j in i:
            print(j)
        continue
    print(i)

print("-----------------------------------------------------")

x = (90,"hi",("red",[10,20]),[100,200])
for i in x:
    if type(i) == list or type(i) == tuple:
        for j in i:
            if type(j) == list:
                for k in j:
                    print(k)
                continue
            print(j)
        continue
    print(i)