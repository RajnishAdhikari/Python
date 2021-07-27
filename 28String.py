#single cotation ''and double cotation "" all string
s = 'a'
print(type(s))

#s = 'This is ' single line string'     invalid string
#s = 'This is \' single line string'     valid string
#print(s)


#invalid s = 'Videos by "ramesh" and 'hari' are awesome. '
s = """Videos by "ramesh" and 'hari' are awesome"""
print(s)


#Accessing String
s = 'Sumana is a good boy.'
#using indexing
print(s[1])
print(s[-6])

"""
s = input('Enter the string :')
i = 0
for x in s:
    print('Character present at positive index{} and at negative index{} is {}'.format(i,i-len(s),x))
    i = i+1
"""


"""
#using slicing
#syntax
#[beginingstring:endstring:stepvalue]
#s[::]
s = 'Learning python is very easy'
print(s[1:5:1])
print(s[1:5:2])
print(s[:5:1])
print(s[::1])
print(s[::])

"""


"""
s = 'abcdefghijklmnop'
print(s[1:6:2])
print(s[::1])
print(s[::-1])
print(s[:1000:1])


print()
print()

#mathematical operations in string
# + string concatination
print('ram' + ' hari')

# * string multiplication
print('ram '*2)


#finding the  length of the string
s = 'Hi man this is rajnish adhikari reporting'
print(len(s))

print()
print()

#Accessing string from forward and backward direction
s = "Learning python is very easy."
n = len(s)
i = 0
print('String in forward direction')
while i<n:
    print(s[i], end='')
    i+=1

print()

print('String in backward direction')
i = -1
while i>= -n:
    print(s[i],end='')
    i = i-1

print()
print()
print('\n')
s = 'Learning python is very easy.'
print('String in normal way')
for i in s:
    print(i,end='')

print('\nstring in Forward direction')
for i in s[::]:
    print(i,end='')

print('\nstring in backward direction')
for i in s[::-1]:
    print(i,end='')

"""

print()
#checking membership in python
s = 'python'
print('p' in s)
print('d' in s)



'''
s = input('Enter the main string:')
subs = input('Enter the sub string:')
if subs in s:
    print(subs,'is available in the string.')
else:
    print(subs,'is not available in the main string.')

'''



#Comparistion between string
# eg.1
"""
s1 = input('Enter the string:')
s2 = input('Enter the next string:')
if s1 == s2:
    print('Both strings are equal.')

else:
    print('Strings are not equal.')
"""
'''
#eg.2
s1 = input('Enter the string:')
s2 = input('Enter the next string:')
if s1 == s2:
    print('Both strings are equal.')

elif s1>s2:
    print('First string is greater than second string.')
elif s2>s1:
    print('Second string is gerater than first string.')
else:
    print('Strings are not equal.')

'''

'''
#example to show if we give space before or after
#the input data then output wont print space

city  = input('Enter your city name:')
scity = city.strip()
if scity == 'ktm':
    print('ktm')
elif scity == 'pokhara':
    print('pokhara')
else:
    print('city is invalid.')
'''

'''
#same as above example without creating variable
city  = input('Enter your city name:').strip()
if city == 'ktm':
    print('ktm')
elif city == 'pokhara':
    print('pokhara')
else:
    print('city is invalid.')
'''

'''
#to find the position or index of the string
s = 'Learning python is very easy'
print(s.find('python'))
print(s.find('e'))
'''

'''
#to find the position or index of the string at a 
#given boundary
s = 'Learning python is very easy'
print(s.find('p', 7,15))
print(s.find('e'))
print(s.find('z'))
print(s.index('z'))
'''

'''
#simple file handling case in string in python
s = input('Enter the main string.')
subs = input('Enter the substring:')
try:
    n = s.index(subs)

except ValueError:
    print('Substring is not found.')

else:
    print('Substring is found.',n)
'''


'''
s = input('Enter the main string:')
subs = input('Enter the substring:')
flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(subs,pos+1,n)
    if pos == -1:
        break 
    print('found at position ', pos)
    flag = True
if flag == False:
    print('String is not found.')
'''


#counting  the total no. of sub string.
s = 'adjjflkddsfjdfddaaa '
print(s.count('a'))


#replacing in the substring
#s.replace(oldstring, newstring)
s = 'python is easy to learn.'
s1 = s.replace('easy' , 'difficult')
print(s1)




#SPLITTING OF THE STRING
#s = "My name is Rajnish Adhikari"
#syntax
#l = s.split(seperator)
s = 'Python videos by Testa Mesta Vesta are awsome.'
l = s.split()
print(type(l))
for x in l:
    print(x)
print()  
#same eg of above but different method
s = 'Python videos by Testa Mesta Vesta are awsome.'.split()
for x in s:
    print(x)

s ='20-12-2020'
l=s.split('-')
for s in l:
    print(s)

print()
print()



#JOIN IN STRING
#SYNTAX
# A B C D 
#JOINING ABOVE STRING ACCORDING TO - A-B-C-D
#S=SEPERATOR.JOIN(GROUP OF STRING)
t = ('rajnish','ram','shyam')
s = '-'.join(t)
print(s)



#changing the case of the string
#like lower to upper and upper to lower 
'''
upper()
lower()
swap()
title()
capitalize()
'''
#Example
"""
s = 'learning python Is VeRy easY.'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
"""

#Checking string starts with given sub string or not.
#function are startswith() and endswith()
#syntax
#s.startswith(substring)
#s.endswith(substring)
s='Hello hi and Namaste to you all'
print(s.startswith('Hello'))
print(s.endswith('all'))

#to check type of character present in the string
#isalnum()==> a to z A to Z and 0 to 9
#isalpha()==> a to z A to Z 
#isdigit()==> 0 to 9
#islower()==> lowercase a to z 
#isupper()==> uppercase A to Z 
#istitle()==> True if string is title case
#isspace()==> string is made of space
# print('Rajnish123'.isalnum())
# print('Rajnish123@'.isalnum())
# print('Rajnish123'.isalpha())
# print('Rajnish'.isalpha())
# print('Rajnish123'.isdigit())
# print('123'.isdigit())
# print('Rajnish'.islower())
# print('rajnish'.islower())
# print('rajnish'.isupper())
# print('RAJNISH'.isupper())
# print()
# print()
# print('rajnish'.upper().isupper())#first changing lowercase 
# #upper and then checking if uppercase or not
# print()
# print('rajnish'.istitle())
# print('Rajnish'.istitle())
# print('rajnish'.isspace())
# print('aarati is a good girl'.isspace())
# print('  '.isspace())


# for the implementation of nested if statement
# s = input('Enter any string:')
# if s.isalnum():
#     print('String is alphanumeric.')
#     if s.isalpha():
#         print('Alphabet Character') 
#         if s.islower():
#             print('Lowercase string')
#         else:
#             print('String is not lowercase.')
#     else:
#         print('String is not alphabet characte.')
# else:
#     print('String is not alphanumeric.')
print()
print()
# formatting of the string
# two types 
# 1. format() with replacement operator
# 2. f string
# name =  'Hari'
# age = 25
# print('My name is {0} and my age is {1}.'.format(name,age))
# print(f'My name is {name} and my age is {age}.')
# print('My name is {x} and my age is {y}.'.format(x = name,y = age))

#example of the binary formatting
print('Binary formatting:{0:b}'.format(153))


print()

#reversed function in  string
#i.e. reversing the giving string 
# s = input('Enter any string :')
# r = reversed(s)
# output = ''.join(r)
# print(output)


#to print no of words that is available in the string
# s = input('Enter any string:')
# v = ['a', 'e', 'i' , 'o', 'u','A','E','I','O','U']
# d = {}
# for ch in s:
#     if ch in v:
#         d[ch] = d.get(ch,0) + 1 
# for k,v in sorted(d.item()):
#     print('{} occurs {} times'.format(k,v))












