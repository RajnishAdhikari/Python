# Dictonary
# if we want to represent a group of individual object
# as a single entity then  we will go for list,set,tupels

#if we want to represent a group of data as a key 
# value pair then we should go for dictonary

# eg:
# roll_number = Name
# phone_number = address
# ip_address = domain_name
#   (key)          (value)


# features of dictonary
# 1) Duplicates value 
# key cannot be Duplicate while value can be Duplicate

# 2) Heterogenous 
# Heterogenous object are allowed for both key and values
# eg           100: 'ram'   'ram' ='1.25'

# 3) Insertion order isn't preserved
# while printing the elements of the dictonary at many time  we can
# can get that those elements in any position

# 4) Dictonary is mutable as we can insert and delete elements from 
# the dictonary

# 5) Dictonary is dynamic as we can increase and decrease the 
# size of dictonary


# 6) Concept of indexing and slicing and not applicable



# How to create a dictonary? 
# d = {}
# print(type(d))



# d = dict()
# print(type(d))


# value associated dictonary 
# d = {}            ###first making empty dictonary
# d[100] = 'rajnish'  #here 100 is key and rajnish is value
# d[101] = 'raj'
# d[102] = 'raju'
# d[103] = 'ram'
# print(d)
# print(type(d))


# accessing certain key value 
# d = {100:'ram',200:'hari',300:'rajnish',400:'python'}
# # print(d[300])
# if 200 in d:
#     print(d[200])
# else:
#     print('value not available')


# d = {100:'ram',2000:'hari',300:'rajnish',400:'python'}
# if 200 in d:
#     print(d[200])
# else:
#     print('value not available')


# wap to enter name and percentage of students and display on the screen
# record ={}
# n = int(input('Enter  the number of student:'))
# i = 1
# while i<=n:
#     name = input('Enter the name of student: ')
#     marks = int(input('Enter the mark of student:'))
#     record[name] = marks
#     i = i+1
# print('##################################################')
# print('\t''Name of student','\t\t', 'Student mark')
# for x in record:
#     print('\t',x,'\t\t',record[x])


# updating the dictonary
# d[key] = Value
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'}
# d[100] = 'social'
# d[500] = 'design and analysis of algorithm'   #//new element
# print(d)



# how to delete the key value from dictonary
# 1) del d[key] -- d is dictonary
# eg
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# del d[100]
# print(d)

# 2) clear() -- it delets all the item from dictonary
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(d)
# d.clear()
# print(d)



#how to delete a dictonary
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# del d 
# print(d) --this will show error because delete is already deleted


# important function in dictonary
 
# 1)dict()
# To create a dictonary
# d = dict()
# print(type(d))

# d = [(100,'rajnish'),(200,'ram'),(300,'hari')]
# print(type(d))     ###this is list 


# d = dict([(100,'rajnish'),(200,'ram'),(300,'hari')])
# print(type(d))   ##this is dictonary
# print(d[200])

# 2) len()
# returns the number of item in the dictonary 
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(len(d))

# 3) clear()
# clears every item  from the dictonary 

# 4) get()
#if there is some value then it returns else returns null
# d.get(key)
# d.get(key,defaultvalue)
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(d.get(300))
# print(d.get(600))   #prints null value
# print(d.get(600,'The key you searched is no in the dict'))

#5)  pop()
# removes the mentioned item from the list and returns
# the remaining item
# if key isn't available we will get key error
# d.pop(key)
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# d.pop(300)
# print(d)
# d.pop(700)  ##prints key error

# 6) popitem()
# this function removes random item from the dictonary
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(d)
# print(d.popitem())
# print(d)


# 7) keys()
# it returns all the keys associated with the dictonary
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(d.keys())
# for k in d.keys():
#     print(k)

# 8) values()
# it returns all the values associated with the dictonary
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(d.values())
# for k in d.values():
#     print(k)

# 9) items()
# it returns the tuples values representing key value pair
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# for k,v in d.items():
#     print(k,'......',v)

#10) copy()
# to create copy of the dictonary
# d1 = d.copy()
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# d1 = d.copy()
# print(d)
# print(d1)

# 11)  setdefault():
# if the key is already available then returns corresponding 
# values else that value is added in the dict as a new items
# d = {100:'science', 200:'health', 300:'maths',400:'nepali'} 
# print(d.setdefault(500,'php'))
# print(d)
# print(d.setdefault(100,'c programming'))

# 12) update()
# adding new item in the dictonary


# dictonary comprehension
# square = {x:x*x for x in range(1,6)}
# print(square)

# wap to take dictonary from the user and print the sum of the values 
# d = eval(input('Enter your dictonary:'))
# s = sum(d.values())
# print('The sum is',s)

# wap to find number of occurence of each letter 
# present in the string
# word = input('Enput any word you love:')
# d = {}
# for x in word:
#     d[x] = d.get(x,0)+1
# for k,v in d.items():
#     print(k,'occured',v,'times')

# wap to input key and value with user and print the value with it's
# associated key
n = int(input('Enter the number of student: '))
d = {}
for i in range(n):
    name = input('Enter the name of student: ')
    marks = input('Enter the marks:')
    d[name] = marks
while True:
    name = input('Enter the student names to get marks: ')
    marks = d.get(name, -1)
    if marks == -1:
        print('Student not found')
    else:
        print('marks of', name , 'is', marks)
    option = input('Do you want to search again?  [YesNo]')
    if option == 'No':
        break
print('thanks for using our app.')
