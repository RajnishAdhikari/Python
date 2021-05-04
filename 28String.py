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



