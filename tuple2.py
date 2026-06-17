# # x = (10,20,30)
# # a,b,c=x
# # print(a,b,c)
# # # function  :- len min max sum sort
# # # method := count index
# # print(len(x))
# # print(x.count(10))
# # print(x.index(30))
# # print(x[1:])
# # print(x[1:2])
# # nested tuple
# x = ((10,20),(30,40))
# print(x[1][0])
# for i in x:
#     for j in i:
#      print(j)

# print()
# x = ((10,20),30,(40,50),"hi")
# for i in x:
#     if type(i) == tuple:
#         for j in i:
#           print(j)
#         continue
#     print(i)
      
x = (10,20,30)
print(x,type(x))
y = list(x)
y.append(40)
print(y,type(y))
x = tuple(y)
print(x,type(x))
