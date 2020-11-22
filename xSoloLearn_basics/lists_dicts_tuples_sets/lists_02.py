

#Add and Concatenate ................
ints_01=[0, 1, 2, 3]; print("ints_01:"); print(ints_01)
ints_02=[3, 2, 1, 0]; print("ints_02:"); print(ints_02)

#Operations on list
print("ints_01+ints_02:"); print(ints_01+ints_02)
print("ints_01 * 3");      print(ints_01 * 3)
#....................................
print("\n")

#len = length?
print("len(ints_01):"); print(len(ints_01))

#methods: append(x), pop() ...............
ints_01=[0];        print("ints_01:",end=""); print(ints_01)
ints_01.append(1);  print("ints_01:",end=""); print(ints_01)
ints_01.append(2);  print("ints_01:",end=""); print(ints_01)
ints_01.pop();      print("ints_01:",end=""); print(ints_01)
ints_01.pop();      print("ints_01:",end=""); print(ints_01)

#list/array : methods : "INSERT" ...............
print("\"INSERT\" is a method similar to \"append\"")
ints_02=[1,3];       print("ints_02="+str(ints_02))
ints_02.insert(1,2); print("ints_02.insert(1,2)..."+str(ints_02))
ints_02.insert(0,0); print("ints_02.insert(0,0)..."+str(ints_02))
print("\n")

#method : index(X)
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))

#methods: min, max, count
print(min(letters))
print(max(letters))
print(letters.count('p'))
print(letters.count('q'))


#list/array : more methods ....................
letters.reverse()
print(letters)
letters.remove('u')
print(letters)
