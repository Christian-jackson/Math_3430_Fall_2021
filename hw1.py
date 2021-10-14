# hw1.py
# This program has many problems, and will NOT run as-is. 
# For part of this assignment, you need to correct it.
# Christian Jackson 8/29

import cmath
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
y=(b**2)-(4*a*c)

x1=(-b-cmath.sqrt(y))/(2*a)

x2=(-b+cmath.sqrt(y))/(2*a)

print ('x1={0} and x2={1}'.format(x1,x2))
#i the intended purpose for this program is to calculate the quadratic formula
#ii a=2, b=-5, c=-30 and x1=5, x2=-3
    #a=1, b=6, c=9 and x1=-3 x2=-3
#x1 = (-b + (b**2 - 4*a*c)**1/2)/(2*a)

#x2 = (-b - (b**2 - 4*a*c)**1/2)/(2*a)
