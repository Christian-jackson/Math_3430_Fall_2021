#I)
# gcd is on other file worked out by hand and that shows that gcd = 4 and gcd_divops = 5
# 
# II)
# have 2 numbers a and b where a > b
# see how many times b goes into a and then subtract the two
# a - nb = x where n is how many times b goes in a and x is the remainder.
# then replace a with b and replace b with x
# you keep doing that until you get x = 0
# with gcd the b of the equation that gave you 0 is the gcd
# and gcd_divops would be how many iterations it took to get to 0
# .
# 
# III).
# test done on paper

#IV)
def gcd(a, b):
    if b==0:
        return a
    return(gcd(b, a%b))



def gcd_divops(a,b):
    if b==0:
        return 0
    return (1 + gcd_divops(b, a%b))

c = 34802
d = 8490
print((gcd_divops(c,d)))
print((gcd(c,d)))

