# set
# if we want to represent a group of unique data as a 
# single entity then we should go for list

# s = {10,20,30,40,10}
# repitition are not allowed in set

# insertion order isn't preserved 
# eg, s={70,80,90,40,50}
# suppose we want to find the element of index 1 but there
# is no gurantee that we will obtain 80 ,,
# position isn't defined, means that 
# insertion order isn't preserved

#indexing and slicing are not allowed
# if we cannot define the position particularly then we 
# aren't able to perform indexing and slicing

# heterogenous objects are allowed
# we can have integer float boolean string 

#set is  mutable
# once we insert element in set then the position isn't 
# defined 

# we can perform mathematical operations like union,
# intersection, difference and so on

#creation of set
# s = {10,20,30,40,70}
# print(type(s))      #set

# s = {10}        #single element is also set
# print(type(s))

# s = {}
# print(type(s))      #this is dictonary

# we can make set by function set()
# l = [10,20,30,40]
# print(type(l))     this is list

# now converting into set
# l = [10,20,30,40]
# s = set(l)
#print(s)
# print(type(s))

# s = set(range(10))
# print(s)



# important function of set
# add(x): here x is any element
# s = {10,20,30}
# s.add(40)
# print(s)
# print(type(s))


#to add multiple item we use update () function
# s = {10,20,30}
# l = [40,50,60]
# s.update(l)
# print(s)

# to find copy of a set using copy()  function
# copy means cloned object
# s = {10,20,30,40}
# s1 = s.copy()
# print(s1)


# to remove and return randon element form the set
# we use pop() function

# s = {10,20, 30,40,50}
# print(s.pop())
# print(s)
# print(s.pop())
# print(s)


#remove() function removes special element
# s = {10,20,30,40,50,60}
# s.remove(20)
# print(s)
# s.remove(200)
# print(s)


# discard() function in set
# works same as the discard while it doesn't show 
# error value
# s = {10,20,30,40,50}
# s.discard(20)
# s.discard(60)
# print(s)

#what is difference between remove and discard
# remove throw error if the element is not available in
# the set while discard jus print that are available in
# the set and do not show error


# clear() function removes all element in the set
# s = {10,20,30,40,50}
# print(s)
# s.clear()
# print(s)

# mathematical operations in set
#  1.union
# implementing 
# x.union(y)
# x|y
# x = {10,20,30,40,50,60}
# y = {60,70,80,40,50}
# print(x.union(y))
# print(x|y)


#  2. intersection
# implementing 
# x.intersection(y)
# x|y
# x = {10,20,30,40,50,60}
# y = {60,70,80,40,50}
# print(x.intersection(y))
# print(x&y)


# 3. Difference
# implementing 
# x.difference(y)
# x-y
# x = {10,20,30,40,50,60}
# y = {60,70,80,40,50}
# print(x.difference(y))
# print(x-y)



#4. symmetric difference
# implementing 
# x.symmetric_difference (y)
# x y
# x = {10,20,30,40,50,60}
# y = {60,70,80,40,50}
# print(x.symmetric_difference (y))
# print(x ^ y)



# Membership operator in set
# 1. in and 2. not in
# s = set('rajnish')
# print(s)
# print('r' in s)
# print('z' in s)
# print('i' not in s)


# set comprehension
# s = {x*x for x in range(10)}
# print(s)


# if we need to remove duplicates from the list then
# we can convert list to set and example is shown
#  list =[10,20,30,40,50,60,10,70,80,90]
#  s = set(list)
#  print(s)


# w = input('Enter any string you love:')
# s = set(w)
# v = {'a','e','i','o','u'}
# d =s.intersection(v)
# print('The diffferent vowels present in', w, "are",d)



