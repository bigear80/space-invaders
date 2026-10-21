
# a=set()
# a.add(1)
# a.add(1)
# print(a)
# a={1,2,3,4,5,1}
# b={2,8,9,0,2,7}
# b.remove(7)
# # b.remove(6)
# b.discard(0)
# b.discard(6)
# b.add(7)
# print(b)

# for i in a:
#     print(i)
# #opperations on set
# #addition/union
# print(a,b)
# print(a.union(b))
# print(a|b)
# #subtraction/intersection
# print(a.intersection(b))
# print(a&b)
# #symetric diffrence = union-intersection
# print(a.symmetric_difference(b))
# print(a^b)
# #diffrence
# print(a-b)
# print(a.difference(b))
# print(b.difference(a))
b=set( )
a=set( )
c=set( )
for i in range (3):
    a.add(input('what is the number'))
    b.add(input('whats the next number'))
    c.add(input('whats the final number'))
print(a,b,c)
print(a.union(b).union(c))
print(a|b|c)