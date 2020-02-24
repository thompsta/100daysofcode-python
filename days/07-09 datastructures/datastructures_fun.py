numlist = [1, 2, 3, 4, 5]
#print(numlist)
numlist.reverse()
numlist.sort()
for num in numlist:
    print(str(num))

mystring = 'stan'
l = list(mystring)
print(l)
print(l[0])
#pop will remove and return the item, can reference an index
l.pop()
print(l)
l.insert(3, 'n')
print(l)
l[0] = 'c'
print(l)
del l[0]
l.insert(0, 'b')
print(l)
l.append('s')
print(l)

#mutability = can be changed
#immutability = cannot be changed

l = list(mystring)
t = tuple(mystring)

l[0] = 'p'
#t[0] = 'b' #throws error because tuple is immutable

#can still iterate over tuple like list
for letter in t:
    print(letter)


pybites = {'stan' : 30, 'bob': 33, 'mike': 33}
print(pybites)

people = {}
#assigning a key a value in the dictionary
people['stan'] = 27
people['trudy'] = 102
print(people)

print(pybites.keys())
print(pybites.values())
for k,v in pybites.items():
    #print(k, 'is', v, 'years old')
    print('%s is %d years of age' % (k,v))

