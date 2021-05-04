#Input and Output Statement in Python
'''
a = int(input('Enter any number:'))
b = int(input('Enter another number:'))
print(a+b)
'''
'''
#print('\n')
#read data fom user and display the info
employee_number = int(input('Enter the employee no:'))
employee_name = input('Enter then employee name:')
employee_salary = float(input('Enter the employee salary:'))
employee_address = input('Enter the employee address:')
employee_married = bool(input('Is empl married ?[y/n]'))
print('Employee number:',employee_number)
print('Employee name:', employee_name)
print('Employee address:', employee_address)
print('Employee salary:', employee_salary)
print('Employee Married or not?:', employee_married)

'''
'''
a,b = [int(x) for x in input('Enter two numbers:').split()]
print('product is:', a*b)'''



'''
from sys import argv
argv = [ 10,20,30,40]
print('The number of command line argrments:',len(argv))
print('List of the command line argumetns:',argv)
print('command line argument one by one:')
for x in argv:
    print(x)

    '''

from sys import argv
argv = [10,20,30]
sum = 0 
args = argv[0:]
for x in args:
    n=int(x)
    sum = sum+n
print('Sum is ', sum)


#output Statement
print('Rajnish')
print()
print('Aarati')

print()

print('My name is rajnish\nadhikari')

print()

print('rajnish '*5)
print('Rajnish' + ' Adhikari')
print('Rajnish is goo\td boy.')


print()

a= 10
b= 20 
c= 30
print(a,b,c)
print(a,b,c,sep=',')
print(a,b,c,sep=':')


print('Rajnish')
print('Adhikari')
print()

print('Rajnish ', end = '')
print('Adhikari')


print()
a = 20
print('My name is Rajnish and my age is',a)



print()

#Replacement operator
name = 'Rajnsih'
age = 21
print('My name is {0} and my age is {1}'.format(name,age))



name = 'Rajnsih'
age = 21
print(f'My name is {name} and my age is {age}')






