pset = set([1,2,3,3,2,1])
print(pset)

pset.add(4)
print(pset)
pset.add(4)
print(pset)
pset.remove(2)
print(pset)
pset2 = set([1,4,5,6,7])

print(pset & pset2)
print(pset | pset2)

print(set([1,2,[3,4]]))