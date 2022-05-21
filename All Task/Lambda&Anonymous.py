# result = lambda n1, n2, n3: n1+n2+n3 #, n1-n2-n3--throws error because it only accept one expression
# print("sum of three values : ", result(10, 20, 25))

# result = lambda n1, n2, n3: n1 * n2 * n3
# print("Multiplication of three values : ", result(10, 20, 25))

# add_sub = lambda x,y : (x+y, x-y)
# a,b  = add_sub(2,5)
# print(a)
# print(b)
#map
# li = [5, 7, 8,9,10,11,12,13,14,15]
# square_list = list(map(lambda x: x**2, li))#tuple(map(lambda x:x**2, li))
# print(square_list)

# a = [1,2,3,4]
# b = [2,4,6,7]
# ab = list(map(lambda x, y : x+y,a,b))
# print(ab)

# Filter function
# data = [1,2,3,4,5,6,7,8,9,10,11,12,13,]
# a = list(filter(lambda x: x%2==0, data))
# print(a)
# Reduce function
from functools import reduce
li = [5,6,7,9,0,8,13]
sum = reduce((lambda x, y: x+y), li)
print(sum)
 