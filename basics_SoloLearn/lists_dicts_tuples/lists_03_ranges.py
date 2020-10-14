

#range object
r00= range(0); print(r00, end=''); print(type(r00))
r01= range(1); print(r01)
r02= range(2); print(r02)
r03= range(3); print(r03)
r04= range(4); print(r04)

#list from range
l00=list(r00); print(l00, end=''); print(type(l00))
l01=list(r01); print(l01)
l02=list(r02); print(l02)
l03=list(r03); print(l03)
l04=list(r04); print(l04)                     
print("\n")

#list/array with range from begining to end .............
print(list(range(10)))
print(list(range(0,10)))
print(range(10)==range(0,10))
print(list(range(1,10)))
print(list(range(5,10)))
print("\n")

#list/array with range from begining to end with INTERVAL .............
print(list(range(10)))
print(list(range(0,10)))
print(list(range(0,10,1)))
print(list(range(0,10,2)))
print(list(range(0,10,3)))
print(list(range(0,10,4)))
print(list(range(0,10,5)))
print(list(range(0,10,6)))
print(list(range(0,10,7)))
print(list(range(0,10,8)))
print(list(range(0,10,9)))
print(list(range(0,10,10)))
