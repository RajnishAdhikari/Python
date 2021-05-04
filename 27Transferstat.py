#types
#break
#continue
#pass
'''
#Break Statement
for i in range(10):
    if i==7:
        print('Processing is finished.')
        break
    print(i)


'''

"""
cart = [10,50,30,550,600,40,400]
for item in cart:
    if item > 500:
        print('You cannot process items more than 500Rs.')
        break
    print(item)

"""


'''


#Continue Statement
#to print odd number between 0-9
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

print()
#to print even number between 0-9
for i in range(10):
    if i%2 != 0:
        continue
    print(i)

print()
print()

cart = [10,50,30,550,600,40,400,80,90,900]
for item in cart:
    if item>500:
        print('You cannot process the items more than 500Rs.', item)
        continue
    print(item)
'''

"""
#loop with else block
cart = [10,20,30,40,500,510]
for item in cart:
    if item>=500:
        print('We cannot process your item.',item)
        break
    print(item)
else:
    print('All item procssed successfully.')
"""

#pass statement
def m1():
    pass

#Example
for i in range(100):
    if i%9 ==0:
        print(i)
    else:
        pass

#using delete keyword
x = 10
print(x)
del x     #firstly x is defined and then its value is deleted.
print(x)
