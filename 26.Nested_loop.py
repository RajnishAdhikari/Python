"""
#nested loop - loop  inside another loop
for i in range(4):
    for j in range(4):
        print('i = ',i, 'j = ',j)
"""


"""
#right angle triangle pattern
n = int(input('Enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end = "")
    print()
"""


#
n = int(input('Enter the number of rows you want to print:'))
for i in range(1,n+1):
    print(''*(n-i),end='')
    print('*'*i)