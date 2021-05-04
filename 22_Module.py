#Module is a collection of function and class
#using math module
import math
print(math.sqrt(49))
print(math.pi)

import math as m 
print(m.pi)

print('\n')
print(m.ceil(1.30))
print(m.floor(1.30))




#finding area of circle 
from math import pi
r = int(input('Enter the radius of circle:'))
print('Area of the circle is:', pi*r**2)