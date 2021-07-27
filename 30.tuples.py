#Tuple
#tuple is exactly same as list but tuple is
# immutable

# if out data is fixed we should go for tuple
# instertion order is preserved
# duplicates are allowed
# heterogenous object are allowed in tuple
# supports both positive and negative index
# made by using parenthesis -()

# for eg 
# t = 10,20,30,40,50 #if we dont use () its ok but recommended
# print(t)
# print(type(t))

# t = ()
# print(type(t))  #empty is also tuple

# t = (10)
# print(type(t))  #intger
# for single value tuple we should seperate by comma

# t = (10,)
# print(type(t))
# print(t)

# tuple creation

# t = ()   #empty tuple
# t =(10,)    #single valued tuple
# t = (10,20,30,40,50) #normal tuple
#  # by using tuple() function
# list = [10,20,30,40,50,60]
# t = tuple(list )
# print(t)

# t = tuple(range(10,20,2))
# print(t)


# Accessing elements of tuples
# 1. Index
# 2. slicing
  
# 1, Index
# t = (10,20,30,40,50)
# print(t[5])

# 2. slice operator
# t = (10,20,30,40,50)
# print(t[2:5]) #form index 2 to 5
# print(t[:5]) #from 0 to index 5
# print(t[:])  #form 1st to end
# print(t[::])  # default increment value 1
# print(t[::2]) #default increment value 2, 1st ko include hunxa



#Tuples vs immutability
#once made tuple cannot be changed means immutable
# t = (10,20,30,40)
# t[1] = 1000
# print(t)   #invalid because we cannot add element in tuple



#mathematical operator in tuple
# 1, concatination operator
# t1 = (10,20,30,40)
# t2 = (50,60)
# t3 = t1+ t2
# print(t3)


#multiplecation operator or repitition operator
# t1 = (10,20,30,40)
# t2 = t1*3
# print(t2)


##Important function in tuple
#1 len()  #total no of items in list
# t = (10,20,30,40)
# print(len(t))

#2 count() #prints how many times a particular element is 
# repitated
# t1 = (10,20,30,40,20,20,20)
# print(t1.count(20))

#3 index() #shows the index of the element
# t1 = (10,20,30,40)
# print(t1.index(30))
# print(t1.index(2000)) #error because the element isn't in the index


#4  sorted()  #arranging in ascending order
# t1 = (10,20,30,15,5,40)
# t2 = sorted(t1)
# print(t2)
# print(t1)


#5 minimum and maximum function
#returns minimum and maximum function
# t1 = (10,20,30,15,5,40)
# print(max(t1))
# print(min(t1))


#cmp() 
# it compares items of different tuple
# if both are equal it returns 0
# if first tuple is less than the other then it returns -1
# if first tuple is greater than the second then it return +1

# t1 = (10,20,30)
# t2 = (10,20,30)
# print(cmp(t1,t2))  #cmp is only in python 2 

# 6  tuples packing and unpacking
# a = 10
# b = 20
# c = 30
# d = 40
# t = a,b,c,d  #packing
# print(t)

# t = (10,20,30,40)
# a,b,c,d = t    #we have to assing item == variables number
# print(a,b,c,d) #unpacking

# 7  tuple comprehension
# t = (x*x for x in range(1,16))
# for x in t:
#     print(x)

# print(type(x))



#program to find sum and average form user inputted tuples
# t = eval(input('Enter the number:'))
# l = len(t)
# sum = 0
# for x in t:
#     sum = sum + x
# print ('The sum of the given tuple is:',sum)
# print('Average of the given tuple is:',sum/l)



