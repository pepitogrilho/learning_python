
#list of CHARS ...................................
chars=["0", "1", "2", "3"]; 
print("chars:"); print(chars)
print("len(chars) = " + str(len(chars)))

for i in chars:
   print(i)

i=0
while i < len(chars):
   print("chars[" + str(i) + "]=" + chars[i] )
   i += 1

#...................................... list of CHARS


#list of INTS .......................................
ints=[0, 1, 2, 3]

print("ints:"); print(ints)

for i in ints:
    print(i)

i=0
while i < len(ints):
   print("ints[" + str(i) + "]=" + str(ints[i]) )
   i += 1

#....................................... list of INTS


#empty list .......................................
empty_list = []; print(empty_list)
empty_list.append(0); empty_list.append(1)
print(empty_list)
#....................................... empty list





#mixed list/array...................
mixed=[0, 1, [2,"2"], [3,"3"]]
print("mixed:")
print(mixed)

i=0
while i < len(mixed):
   print(mixed[i])
   i += 1
print("Finished!")
#mixed list/array...................


#multidimensional list/array........
multidim=[[0,"0"], [1,"1"], [2,"2"], [3,"3"]]
print("multidim:")
print(multidim)
i=0
while i < len(multidim):
   j=0
   while j < len(multidim[i]):
      print(multidim[i][j])
      j += 1
   i += 1
print("Finished!")
#multidimensional list/array........


#matrix.............................
m = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
    ]

print(m[0][0])
print(m[1][1])
print(m[2][2])
