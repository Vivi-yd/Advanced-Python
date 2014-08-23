from random import sample
#creating a set -: direct elements
x = set(["Python", "Java", "Pearl", "Python"])
print(x)
#creating a set -: using iterable
y = set("python")
print(y)
#inserting elements -: no duplicates allowed
x.add("Lisp") 
x.add("Haskell") 
x.add("Java")
print(x)

#creating random list for using in set -: elements between 1 and 99
#and lists of size 20
lst1 = sample(range(1, 100), 20)
lst2 = sample(range(1, 100), 20)

print("First list:", lst1)
print("Second list:" , lst2)

set1 = set(lst1)
set2 = set(lst2)

#general operations on sets
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

print "--------------------frozensets -------------------"

#create frozenset
frozen1 = frozenset("veronica")
frozen2 = frozenset("ashu")

#some operations on frozensets
print(frozen1.difference(frozen2))
print(frozen1.union(frozen2))
print(frozen1.isdisjoint(frozen2))
