
#i 
#defining n so that it can be used in the function
n = int(input('Enter a positive integer n:'))
#defining function for single return value of the given function
def g3n1(n):
    #statement if n is even then divide by 2
    if n %2 == 0:
        n = n//2
    #else statement for if %2 != 0 then do this
    else:
        n = (3*n+1)//2
    #ending function and returning n
    return(n)
#setting the function = to something i can print
ans = g3n1(n)
print(ans)
#got help from students in class to make this work

#ii
#defining n so that it can be used in the function
n = int(input('Enter a positive integer n:'))
#tweaking the function above so that it can do the full sequence
def sequence(n):
    #making a list to put the resulting values in
    result=[n]
    #telling the function to stop at 1
    if n < 1:
        return[]
    #creating a while loop to repeat the function until it hits the if statement (this part is from g3n1)
    while n > 1:
        if n % 2 ==  0:
            n = n//2
        else:
             n = (3*n+1)//2
        #telling the function to put the resulting n's into the result list everytime it runs
        result.append(n)
    #ending the function and returning the list of computed n's
    return(result)
#iii
#what you wanted us to put at the bottom of our code
#didn't know how to use n = int(input('Enter a positive integer n:')) at the bottom and have it defined up top too and running twice
n = int(input('Enter a positive integer n:'))
seq = sequence(n)
print("The resulting sequence is: {0}".format(seq ))
print("It has length {0}".format(len(seq )))

#for this part I got from my cousin who goes to math competitions for fun and is a whiz in math
#i couldn't wrap my head around while loops working (like how the ending statement is on top. with if n < 1) 
#and we have appended results to an empty list before to create the resulting list that we need before in this class
#or in my other computations class MATH 3430
