#I
#g(21)
#=>g(32)
# =>g(16)
# =>g(8)
# =>g(4)
# =>g(2)
# =>g(1) done
# 
# II
# to solve this by hand you would just look at the g(n) function at the top of the HW paper and plug in your n
# so if its positive you would divide it by 2 and if its odd then put it in (3n+1)/2 then you would set that answer as your new n and keep 
# plugging it in into the fomula given (repeating if possitive divide by 2 and if odd put it in (3n+1)/2)
# you'd keep doing that until you get 1 and then stop, unless you get insanely lucky and find the one number no one has found where
# this problem doesn't converege to 1
# 
# III
# 
# g(33)         (3n+1)/2
# =>g(50)       //2
# =>g(25)       (3n+1)/2
# =>g(38)       //2
# =>g(19)       (3n+1)/2
# =>g(29)       (3n+1)/2
# =>g(44)       //2
# =>g(22)       //2
# =>g(11)       (3n+1)/2
# =>g(17)       (3n+1)/2
# =>g(26)       //2
# =>g(13)       (3n+1)/2
# =>g(20)       //2
# =>g(10)       //2
# =>g(5)        (3n+1)/2
# =>g(8)        //2
# =>g(4)        //2
# =>g(2)        //2
# =>g(1)
# done and it will fluctuate between 1 and 2 from here)))


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

#for this part I got from my cousin who goes to math competitions for fun and is a whiz in math
#i couldn't wrap my head around while loops working (like how the ending statement is on top. with if n < 1) 
#and we have appended results to an empty list before to create the resulting list that we need before in this class
#or in my other computations class MATH 3430

#iii
#what you wanted us to put at the bottom of our code
n = int(input('Enter a positive integer n:'))
seq = sequence(n)
print("The resulting sequence is: {0}".format(seq ))
print("It has length {0}".format(len(seq )))