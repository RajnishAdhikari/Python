#set is defined by {}
# sets are mutable as we can add and remove
#indexing is not defined in set
s = { 100,200,100.25,'Ram'}
print(type(s))
print(s)
#for printing set one by one
for i in s:
    print(i)

#for removing any element
s.remove('Ram')
print(s)
#for adding element we use add function
s.add(201)
print(s)



"""
making set immutable
we can use function frozenset
"""

s = { 100,200,100.25,'Ram'}
fs = frozenset(s)
fs.add(50)
print(fs)