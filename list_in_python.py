#features
# 1 Insertion order is preserved
# 2  Heterogenous objects are allowed
#  3 Duplicate values are allowed
# 4 Growable are allowed 

list = [ 100, 105.44, 'rajnish', True, 100]
"""print(list)
print(list[0])
print(list[-5])
print(list[-2])
print(list[-3])
print(list[0:3])
print(list[1:4])"""

#printing list element one by one
for i in list:
    print(i)

#Adding element in the list -- we use append
list.append("Aarati")
print(list)


# creating the empty list and appending item on it
a = []
a.append("Rajnish")
a.append('ai')
a.append(98)
print(a)

#using loop and printing one by one
for i in a:
    print(i)