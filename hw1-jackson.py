a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)

x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)

print ('x1={0} and x2={1}'.format(x1,x2))
#i the intended purpose for this program is to calculate the quadratic formula

#ii a=2, b=-5, c=-30 and x1=5, x2=-3 (rounded to nearest integer)
    #a=1, b=6, c=9 and x1=-3 x2=-3   (rounded to nearest integer)

#iii Enter a: 2
    #Enter b: -5
    #Enter c: -30
    #x1=5.3197051490249265 and x2=-2.8197051490249265
#iii Enter a: 1
    #Enter b: 6
    #Enter c: 9
    #x1=-3.0 and x2=-3.0

#iv when you run the program you'll be prompted to "Enter a" where you will enter your a value, then press enter and do the same for b and c
    #the a, b, and c values should be ax**2+bx+c=0 where a, b, and c can be possitive or negative
    #the program will then print out your 2 x values indicated by "x1=(value) and x2=(value)" and that will be your answer!

#v when a = 0 you get a "ZeroDivisionError: float division by zero" meaning you cant divide by 0

## got help from 'https://www.youtube.com/watch?v=Kv2a3f6oWag' for the float(input()) part
## page 27 in the book shows how to do the print part


