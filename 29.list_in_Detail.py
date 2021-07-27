# if you want to represent group of data as a single entity
# then we use list where insertion order is preserved.
#features

# 1.insertion order is preserved
# 2.duplicates are allowed
# 3.heterogenous objects are allowed i.e. different data 
# types like string, int,floating point number, boolean, etc
# 4. list is dynamic in nature
# 5. in square braket ['rajnish',2, 2.5, true , 2]
# 6.list object are mutable ie we can change items

 #creation of the list
# a = []
# print(type(a))
# print(a)
# l = [34,34.3,True,'harish']
# print(l)
# print(type(l))


#taking input with user
# l = eval(input('Enter list:'))
# print(l)
# print(type(l))


#By using dynamic casting
# l = list(range(0,12,2))
# print(l)
# print(type(l))

# s = 'Ram'
# l = list(s)
# print(l)
# print(type(l))


#using function
# s = 'My name is rajnish adhikari'
# l = s.split()
# print(l)
# print(type(l))

#another way -- this is good practice
# s = 'My name is rajnish adhikari'.split()
# print(l)
# print(type(l))


#creating list within another list
# l = [35,53,53,21,[34,64],53]
# print(l)
# print(type(l))


#accessing the value or of the list 
#we can do it by two types 1.indexing 2.slicing
#1. by using indexing
# list support both positive and negative indexing
# + means left to right == starts with 0 indexing
# - means right to left == starts with -1 indexing

# l = ['Rajnish',1,2.23,True]
# print(l[3])


# 2.by using slicing
# Syntax
# list2 = list1[start:stop:step]
# start= form where slice starts 
#         Default value 0
# end = where slice ends 
#         length of the list
# step = increment Value
#         default 1

# n = [1,2,3,43,53,56,75,74,33.4]
# print(n[3:8:2])     
# print(n[3:8])   #go from 3rd to 8th no increase value
# print(n[3:])    #go from 3rd to last 
# print(n[:8])    #go from 1st to 8th element
# print(n[::3])  #go from 1st to last with increment value 3


# l = [0,1,2,3,4,5]
# print(l)
# l[3] = 1000   #using mutable property to replace value
# print(l)

#traversing the elements of the list or 
# sequential access of elements of list
# by using while Loop

# n = [1,2,3,4,5,6,7,True,'Ram']
# i = 0
# while i <len(n):
#     print(n[i])
#     i = i+1

#by using for loop
# n = [1,2,3,4,5,6,7,True,'Ram']
# for x in n:
#     print(x)

#printing odd and even elements in the list
# n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,22,33,44,55,66]
# for x in n:
#     if x%2==0:
#         print(x)


# n = [0,1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66]
# for x in n:
#     if x%2 != 0:
#         print(x)


#printing elements according to indexing
# l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,22,33,44,55,66]
# x = len(l)
# for i in range(x):
#     print(l[i],'is available at positive index',i,'and negative index at',i-x)


# important functions of the list

# To get information of list
# len()
# n = [1,2,3,4,4]
# print(len(n))


# #count
# n = [1,1,2,2,3,4,3,2,2,1,1,1,1,1,2,2,3]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))

#index
# n = [1,2,1,3,4,5,6,7]
# print(n.index(1))     #shows what is the index of 1 at 1st
# print(n.index(2))


#functions of list for changing elements of list
# 1. append()- to  add element in the last
# eg.
# list= []
# print(type(list))
# list.append(9)
# list.append(10.255)
# list.append('A')
# list.append(True)
# list.append(10)
# print(list)

#program to implement the number divisible by from 1-100
# list = []
# for i in range(101):
#     if i%10 == 0:
#         list.append(i)
# print(list)    


# 2. insert()
# n = [1,2,3,4,5]
# n.insert(2,10000)
# n.insert(23,4000)
# n.insert(-12,4555)
# print(n)



# 3. extend()
# used to merge two or more than two list
# syntax is 
# l1.extends(l2) -- all elements in l2 are shifted to l1
#list2 item will not be deleted , it is as it is.
# list1 = ['kathmandu', 'pokr', 'syan', 'dang']
# list2 = ['Janakpur','jhapa', 'palpa']
# list1.extend(list2)
# print(list1)
# print(list2)



# 4. remove()
# removes the item from the list
# n = [10, 20, 30 ,40 ,50 ,10]
# n.remove(20)
# n.remove(10) #1st item will removed not all same item
# print(n)


# 5. pop()
# removes the last element of the list
# n = [10, 20, 30, 40, 50,60]
# print(n.pop())  #returns the removed value as well
# print(n.pop())
# print(n)


# ordering the items in the list
# 1.reverse()
# n = [10,20,30,40]
# n.reverse()
# print(n)
 
# 2. sort()
# default ascending to descending
# if we need to sort string then -- ascending order
# n = [10,20,30,40,1,2,3]
# n.sort()
# print(n)



# n = ['ram','rajnish','asmita','elon','bill','warren']
# n.sort()
# print(n)



# n = ['Ram','rajnish','asmita','Elon','bill','Warren']
# n.sort()  #upper and this might not be same because of 
#           # capital letter ascii value start at 65(A)
# print(n)



# n = ['ram','rajnish','asmita',1,'bill',5]
# n.sort()
# print(n) #output is error because at same time, string 
         # and integer value isn't supported


#Another process to sort i.e.
# in descending order
# n = [20,50,5,20,60,95,10,70555]
# n.sort(reverse = True)
# print(n)



# Aliasing vs Cloning
# Aliasing - process of giving another name for the list
# x = [10,20,30,40,50,60]
# y = x
# print(id(x))
# print(id(y))
# print(y)
# y[1] = 500
#disadvantage of aliasing it that when we change the value
# of y in list then x value is also changed


# Cloning -- process of duplicating the list

#using slice operator
# x = [10,20,30,40,50,60]
# y = x[:]  #same element but different id value
# y[1] = 100000
# print(id(x))
# print(id(y))
# print(x)
# print(y)


#using copy function
x = [10, 20, 30, 40,50]
# y = x.copy()
# y[1] = 999
# print(x)
# print(y)


#mathematical operations in list
# 1. concatination  or + operator
# n = [10, 20, 30]
# m = [40, 50, 60]
# print(n+m)

# # 2. multiplication/ repetition  operator
# n = [10, 20, 30]
# m = n*3
# print(m)


#comparing list 
# x = ["Cat","Dog","Monkey"]
# y = ["Cat","Dog","Monkey"]
# z = ["cat","dog","Monkey"]
# print(x == y)
# print(y == z)
# print(x != z)

#comparing by using comparision operator : <> >= <=
# x = [10,20,30,40,50]
# y = [10,20,700,800,1000,10000,100000]
# print ( x < y )
# print(x > y)
# print(x >= y)
# print(x <= y)


#membership operator in list
#in 
#not in
# n= [10,20,30,40]
# print(10 in n)
# print(100 in n)
# print(10 not in n)
# print(500 not in n)


#clear operatior in list
# n= [10,20,30,40]
# print(n)
# n.clear()
# print(n)


#using nested list 
# n= [10,20,30,[100,200]]
# print(n)
# print(n[0])
# print(n[3])
# print(n[3][0])



#list comprehension
# Syntax
# list = [expressioin for item in list if condtion]
# eg:
s = [x*x for x in range(1,10)]
print(s)



v = [2*x for x in range (1,5)]
print(v)

