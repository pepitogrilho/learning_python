

#list/array of integers.............
ints_01=[0, 1, 2, 3]
print("ints_01:")
print(ints_01)

ints_02=[3, 2, 1, 0]
print("ints_02:")
print(ints_02)

print("ints_01+ints_02:")
print(ints_01+ints_02)

print("ints_01 * 3")
print(ints_01 * 3)

#....................................
print("\n")


#list/array of strings...............
words_01=["spam", "egg", "spam", "sausage"]
print("words_01=[\"spam\", \"egg\", \"spam\", \"sausage\"]")
print("Is \"spam\" in words?:" + str("spam" in words_01))
print("Is NOT \"SPAM\" in words?:" + str("SPAM" not in words_01))


#list/array : methods & functions ...............
print("\"append\" is a method")
ints_01=[0]
print("ints_01:")
print(ints_01)
ints_01.append(1)
print("ints_01:")
print(ints_01)
ints_01.append(2)
print("ints_01:")
print(ints_01)

print("\n")

print("\"len is a normal function\" is a method")
print("len(ints_01):")
print(len(ints_01))

print("\n")

#list/array : methods : "INSERT" ...............
print("\"INSERT\" is a method similar to \"append\"")
ints_02=[1,3]
print("ints_02="+str(ints_02))
ints_02.insert(1,2)
print("ints_02.insert(1,2)..."+str(ints_02))
ints_02.insert(0,0)
print("ints_02.insert(0,0)..."+str(ints_02))

print("\n")

#list/array : methods : "INDEX" ...............
print("\"INDEX\" finds the first occurence of a list item")
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))

#list/array : more methods ....................
print(min(letters))
print(max(letters))
print(letters.count('p'))
print(letters.count('q'))

#list/array : more methods ....................
letters.reverse()
print(letters)
letters.remove('u')
print(letters)
