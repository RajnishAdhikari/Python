'''
1 if 
2 if- elif
3 if- elif else

'''

# if statement

'''
 #syntax 
 if condition:
     statement
if condition:
    statement1
    statement2
    statement3 
    and so on
'''
"""
Example
name = input('Enter your name:')
if name == "Rajnish":
    print("My name is Rajnish")
"""



#if-else Condition
#Syntax  
'''
if condition:
    statement
else:
    another statement
'''
"""
sample Example
name = input('Enter your name:')
if name == "Rajnish":
    print("My name is Rajnish")
else:
    print("Sorry man the username is invalid")
"""
'''
3> if elif else
Syntax::
if condtion 1:
    statement1
elif condtion2:
    statement2
elif condition3:
    statement3
else:
    default statement
'''

#Example
"""
brand = input('Enter your favourite brand(mobile):')
if brand == 'nokia':
    print('You have a durable cell phone.')
elif brand == 'sony':
    print('Your cell phone is best for camera.')
elif brand == 'samusang':
    print('Your cell phone has good battery life.')
else:
    print("This is unknown mobile phone for me.")
"""
#note that there is no switch statement in python
"""
n1 = int(input('Enter the first number:'))
n2 = int(input("Enter the second number:"))
if n1 > n2:
    print('First number is greater than second number that is',n1)
else:
    print('Second number is greater than first number that is',n2)
"""




"""
checking which number is greater in 3 user inputted number using if-elif else
n1 = int(input('Enter the first number:'))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
if n1 > n2 and n1 > n3:
    print('First number is greatest  than second number and third that is',n1)
elif n2 > n3 :
    print('Second number is greater than first number that is',n2)
else:
    print('Third number is the greatest one i.e.',n3)
    """





#checking whether a particular number lies in between 1 and 100
n = int(input('Enter any number you want:'))
if n >=1 and n<= 100:
    print('The number',n,' lies in between 1 and 100')
else:
    print('The number is out of range')


#printing 0 to 9
n = int(input('Enter your number between 1 to 9'))
if n==0:
    print('The inputted number is 0')
elif n == 1:
    print('One')
elif n == 2:
    print('Two')
elif n == 3:
    print('Three')
elif n == 4:
    print('Four')
elif n == 5:
    print('Five')
elif n == 6:
    print('six')
elif n == 7:
    print('Seven')
elif n == 8:
    print('eight')
elif n == 9:
    print('nine')
else:
    print('Number is out of the range')