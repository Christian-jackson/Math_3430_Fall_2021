#I
#for this part i picked c = 4 and just kept going until i saw the same number twice. i did this so i could tell if the sequence converges.
# x_1=1
# x_2= 1+4= 5
# x_3= 1+ 4/5= 1.8
# x_4= 1+ 4/1.8= 3.22
# x_5= 1+ 4/3.22= 2.24
# x_6= 1+ 4/2.24= 2.78
# x_7= 1+ 4/2.78= 2.43
# x_8= 1+ 4/2.43= 2.64
# x_9= 1+ 4/2.64= 2.51
# x_10= 1+ 4/2.51= 2.59
# x_11= 1+ 4/2.59= 2.54
# x_12= 1+ 4/2.54= 2.57
# x_13= 1+ 4/2.57= 2.55
# x_14= 1+ 4/2.55= 2.57
# x_15= 1+ 4/2.57= 2.56
# so this is going to converge to around 2.55-2.57
# this does the samething for any pos number n.

#II
#to normally solve this you start off with your base of x_1 = 1 as the first input in your list. Then have 'c' be whatever number that you want (like '4' in problem 1).
# then you move to x_n+1 = 1 + (c/x_n).
# since x_1 = 1, to get x_2 you just plug that into the x_n+1 equation n = 1 => (x_1+1 = x_2) = 1 + (c/x_1)
# so, x_2 = 1 + c/1 or 1 + c
# then to get x_3 you plug in x_2 for x_n, getting x_3 = 1 + (c / (1+c))
# then you keep doing that until you can tell if the sequence is converging or diverging
# converging = sequence going to a certain number
# diverging = fluctiating answers that dont converge or shooting off to infinity.

#III
# x_1 = 1 and c = 2
# now put x_1 = 1 in next part of the sequence x_2
# x_2 = 1 + 2/(1) = 3
# now we put the answer from x_2 = 3 into the next x_n and we repeat this for every n
# x_3 = 1 + 2/(3) = 1.666
# x_4 = 1 + 2/(1.666) = 2.2
# x_5 = 1 + 2/(2.2) = 1.909
# x_6 = 1 + 2/(1.909) = 2.048
# x_7 = 1 + 2/(2.048) = 1.98
# x_8 = 1+ 2/(1.98) = 2.01
# and here you can see the sequence getting closer and closer to 2. meaning its converging.

#for Alice and Bobs question
# after running the code on this for a bunch of pos. even and odd integers, irrational numbers, and rational numbers it seems like all positive real numbers converge
# but once you make 'c' negative it fluctuates between even and odd and shows no sign of it getting closer and closer to a single number
# so all pos real numbers converge and all negative numbers diverge.

#IV
def get_terms(c,N):
    result = [1]
    n = 1
    for N in range(1,N):
        n = 1 + (c/n)
        result.append(n)
    return(result)

while True:
    thisc = float(input("Enter c: "))
    thisN = int(input("how many terms? "))
    seq = get_terms(thisc , thisN)
    print(seq)

#V
# i couldn't see anything that would fail in this code unless you didn't put in simplified versions of 'c' like if you put in a fraction instead of a decimal 
# or try to put in sqrt(n1umber) instead of the the simplified verstion of it.