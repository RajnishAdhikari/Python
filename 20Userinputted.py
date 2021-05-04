a = int(input('Enter your first num:'))
b = int(input('Enter your second num:'))
c = int(input('Enter your third num:'))
min = a if a<b and a<c else b if b<c else c
print('Minimun number among a,b,c is:', min)
