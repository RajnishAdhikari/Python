# Function
# a = 20
# b = 10
# print("the sum is :",a+b)
# print("the difference is :",a-b)
# print("the product is :",a*b)
# print("the quotient is :",a/b)
# #again if we need to find same calculation of another two
# # number then ,,,,,,,,,,,
# a = 200
# b = 100
# print("the sum is :",a+b)
# print("the difference is :",a-b)
# print("the product is :",a*b)
# print("the quotient is :",a/b)
# Here to print the same thing we have printed two times 
# and in near future we may need many more time so to 
# overcome this we use Function




# def calculate(a,b):
#     print('The sum is:',a+b)
#     print("the difference is :",a-b)
#     print("the product is :",a*b)
#     print("the quotient is :",a/b)
# calculate(10, 20)
# calculate(100, 200)
# calculate(1000, 2000)

# defination of Function
# If a group of statement is repeatidealy required then we
# will write that repetedily used code as a single 
# entity and call that separate code whenever we need.
# This phenomenon is known as function

# The main advantage of function is code reusability.


# TYPES OF Function  2 TYPES
# 1) BUILT IN Function
# 2) USER DEFINED FUNCTION

# 1) BUILT IN Function
# The function which are available as soon as python is 
# installed on your machines are called built in function
# eg:: 
# id()
# type()
# eval()
# input()

# 2)USER DEFINED FUNCTION
# The functions which are developed by the programmer to 
# fulfill business logic is called user defined function
# for all user defined function we have to use def infront
# def means define 
# and then name of the function 
# if there is parameter then we have to give parameter(here)
# else there () will be empty
# way to define function
# def function_name(parameters):
    # '''Doc String'''
    # ..............
    # ..function_body..
    # ..............
    # return value (can be or cannot be)

    # eg
# def wish():
#     print("Hello world I am from Nepal.")

# wish()
# wish()
# wish()


# what is parameter/??????
# parameters are input to the function.
# if the function contain any parameter them compulsary 
# arguments should be given at the time of calling
# example:
# def wish(name):
#     print('Hello',name,'good morning')
# wish("aarati")
# wish('Rajnish')
# wish('samrat')


# wap to take any number and print its squre value using function
# def square(number):
#     print('The square of',number,'is',number*number)
# square(9)
# square(7)
# square(5)



# wap to accept two numbers and print it's sum
# def add(x,y):
#     return x + y
# result = add( 8,6)   #every time we need to make sure that
# a = add(500, 100)     #return value is hold else we will get error
# print('The result is',result)
# print('The result is',a)


# def f1():
#     print('Hello')
# f1()


# wap to check whether the given number is even or odd using function
# def even_odd(num):
#     if num%2 == 0:
#         print(num,'is a even number') 
#     else:
#         print(num,'is a odd number')
# even_odd(25)
# even_odd(466)



# WAP TO FIND FACTORIAL
# def factorial(num):
#     result = 1
#     while num >=1:
#         result = result * num
#         num = num -1
#     return result
# print(factorial(5))


# same question printing one by one
# def factorial(num):
#      result = 1
#      while num >=1:
#          result = result * num
#          num = num -1
#      return result
# for i in range(1,5):
#     print('Factorial of ', i , 'is :',factorial(i))






#returning of multiple value function
# def sum_sub(a,b):
#     sum = a+b
#     sub = a-b
#     return sum, sub
# x,y = sum_sub(100, 50)
# print("The sum is ",x)
# print("The difference is ",y)


# def calc(a,b):
#     sum = a+b
#     sub = a-b
#     product = a*b
#     div = a/b
#     return sum,sub,product,div  
# t = calc(100,50) #this is argument
# # print(t)
# # print(type(t))
# for i in t:
#     print(i)



# Types of Arguments in python
# def f1(a,b): #a,b are the formal argument
#     ..........
#     .........

# f1(10,20)  #actual argument


# generally there are four types of argument
# 1) Positional Arguments
# 2) Keyword Arguments
# 3) Default Arguments
# 4) Variable Length Arguments


# 1) Positional Arguments
# These are the arguments passed to the function in the
# correct order. we cannot interchange position
# for eg:
# def sub(a,b):
#     print(a-b)
# sub(20, 10)
# sub(10,20)
# if we change the order of argumet then the order
# is different


# 2) Keyword Argument
# def sub(a,b):
#     print(a-b)
# sub(10, 20)  #if we want to make b = 10 and a = 20 then 
# we use keyword arguments
# we can pass argument values by keyword That is by parameter name

# def wish(name,msg):
#     print('hello', name,msg)
# wish(name = 'ram', msg = 'goodmorning')
# wish( msg = 'goodmorning',name = 'hari')

# using positional and keyword argumnt at the same time
# def wish(age,name,msg):
#     print('hello', name,msg,'and your age is',age)
# wish(22,name = 'ram', msg = 'goodmorning')

# def wish(name,msg):
#     print('hello',name,msg)
# wish('rajnish',msg = 'good morning') #at first we use positional 
# argument and keyword argument so this is valid argument

# wish('rajnish','good morning') only implementing positional argument
# wish(msg = 'how are you', rajnish) #invalid argument as positional
# argument isn't in the well positioned


# 2) Default Arguments
# def wish(name = 'Guest'):
#     print('hello', name, 'Good morning')
# # wish('Ram') #if in case argument is passed then we will get 
# # that as output else Default argument is passed as given
# wish()

# def wish(name = 'Guest',age):
#      print('hello', name, 'Good morning and your age is',age)
# wish('ram',25)  #this is not possible because while passing
# default argument we should pass it at last

# def wish(age,name = 'Guest'):
#       print('hello', name, 'Good morning and your age is',age)
# wish(25,'ram')
# wish(24)


# def wish(name = 'Guest',mes = 'Good morning')       valid


# def wish(name = 'guest', msg)     invalid because positional 
# argument is after the default argument
# default argument always need to come at last








