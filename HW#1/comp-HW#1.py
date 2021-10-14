'''
For this assignment you will need to plan and write a collection of
algorithms to implement some simple linear algebra operations. For each
algorithm you must write and answer the three questions as the first step. Your answers to the
three questions must match the algorithm you write. You should begin each
algorithm by giving it a function name, see the example for more details.

Your algorithms must match the style used in the example given. Do not copy the
versions of these algorithms written in class. This is intended to be the "next
step" in improving our initial work. You are encouraged to use those versions to help in your
writing of these algorithms.  

Your work must be typed up into this document and uploaded to blackboard. 

This assignment is due by 11:59pm on 09/17/2021. Late work will not be accepted. 


Example:

Problem #0

Write an algorithm to implement vector addition. 


Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 


def add_vectors(vector_a,vector_b):

# Initializing result as an empty list
result = []

# Add an element to result for each element of vector_a. Set that element to 0.
for element in vector_a:
  append 0 to result

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

# Return the desired result.
return result



End Example
'''

#Problem #1

'''
#Write an algorithm to implement scalar-vector multiplication.
'''

#Q1: What do we have?

#A1:  We have a vector stored as a list, denoted by vector_01, and a scalar number stored as an integer
#  denoted by scalar that is being mulitplied to elements in the vector.

#Q2: What do we want?

#A2: We want the product of the scalar number multiplied by the elements in our vector and put it into a new list, vector.no

#Q3: How will we get there?

#A3: We will define a function svmp to give us a*b=c (or in code, vector_01*scalar)
'''
#defining a fucntion that returns multiplication
def scalar_vector_multi(vector_01):
    return vector_01*scalar

# Initializing result as an empty list
vector = []

#instructions for use to put how many elements are in the vector,
elem = int(input("Insert how many elements you want:"))

#for an element i in range from 0 to the given number of elements append an integer to vector from [0,1,2,...,n]
#aka telleing the user to put their elements in
for i in range(0, elem):
    vector.append(int(input("Enter number:")))
	
#defining scalar for the above function
scalar = int(input('enter scalar multiplier: '))

#maping the made list "vector" back into our function to get the scalar * the elements in the made list
#then having it listed and put into a new element 'ans'
ans = list(map(scalar_vector_multi, vector))

#print the answer
print(ans)

#!!! realized that we don't have to actually make a working python code after I finished this, but too happy that it works to not have it in
# got help from https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# and some stack over flow people that had examples that were close
#also got help from 9/15 class with psuedo-code at the end of the class and my other comp class
'''

#Problem #2

'''
Write an algorithm to implement scalar-matrix multiplication.

Write an algorithm to implement scalar-vector multiplication.
'''

#Q1: What do we have?

#A1:  we have a scalar integer, scalar, a matrix stored as a list of columns, matrix, and a vector stored as a list, vector_01

#Q2: What do we want?

#A2: We want to implement our answer from #1 into each of the vectors (columns) of the matrix given to us and then put them back into a new matrix_ans to get
#the new scaled matrix

#Q3: How will we get there?

#A3: for the scalar-vector we will use the same method from number 1. then for scalar-matrix we will implement our scalar-vector method for each column
# in the matrix (vector_a,vector_b,vector_c) and then we will put it into a their own listed elements (colm_1, colm_2,colm_3) and then plug them back 
#into a new matrix_ans

#scalar-vector. Re-use number 1

#defining a fucntion that returns multiplication
def scalar_vector_multi(vector_01):
    return vector_01*scalar

# Initializing result as an empty list
vector = []

#instructions for use to put how many elements are in the vector,
elem = int(input("Insert how many elements you want:"))

#for an element i in range from 0 to the given number of elements append an integer to vector from [0,1,2,...,n]
#aka telleing the user to put their elements in
for i in range(0, elem):
    vector.append(int(input("Enter number:")))
	
#defining scalar for the above function
scalar = int(input('enter scalar multiplier: '))

#maping the made list "vector" back into our function to get the scalar * the elements in the made list
#then having it listed and put into a new element 'ans'
ans = list(map(scalar_vector_multi, vector))



#scalar matrix
def scalar_matrix_multi(matrix_01):
    
    return matrix_01*scalar

vector_a = scalar_vector_multi
vector_b = scalar_vector_multi
vector_c = scalar_vector_multi

# Initializing result (matrix) as a set of vectors
matrix=[vector_a, vector_b, vector_c]

#putting the scaled vectors into columns
colm_1 = list(map(scalar_matrix_multi, vector_a))
colm_2 = list(map(scalar_matrix_multi, vector_b))
colm_3 = list(map(scalar_matrix_multi, vector_c))

#putting those new columns into our new scaled matrix
matrix_ans = [colm_1,colm_2,colm_3]
#print answer
print(matrix_ans)




#Problem #3

'''
Write an algorithm to implement matrix addition.

Write an algorithm to implement scalar-vector multiplication.
'''

#Q1: What do we have?

#A1:  We have a matrix stored as a list of columns, a scalar integer stored as scalar, and a vector stored as a list

#Q2: What do we want?

#A2: We want to get two matrices added to one another to form a new add_matrix_ans and we want the same thing as #1

#Q3: How will we get there?

#A3: We will create an empty matrix of approprite size to the other given matricies and then we will write a for statement that will iterate the matrix addition through rows and columns.
#we will then store that into our new matrix.

#scalar vector multi. Re-use number 1

#matrix addition
def matrix_addition():
    return matrix_1+matrix_2

#setting the colmumns of the second vector equal to new defined elements
vector_1,vector_2,vector_3 = scalar_vector_multi,scalar_vector_multi,scalar_vector_multi

matrix_1 = [vector_a,vector_b,vector_c]
matrix_2 = [vector_1,vector_2,vector_3]

# setting result (add_matrix_ans) as an empty list
add_matrix_ans = [[0,0,0],[0,0,0],[0,0,0]]

#iterating matrix addition through columns(i) and then through rows(j)
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        add_matrix_ans[i][j] = matrix_1[i][j] + matrix_2[i][j]

#setting result as a perfect subset of add_matrix_ans to be able to print answer
for result in add_matrix_ans:
    print(result)

#Problem #4
'''
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.  
'''

#Write an algorithm to implement scalar-vector multiplication.

#Q1: What do we have?

#A1:  We have a matrix whos elements are stored as column vectors and a vector stored in column form. we also have the functions stored from #0 and #1

#Q2: What do we want?

#A2: we want a new matrix with the same number of rows as the given matrix and same number of columns as the vector. We also want to store the elements of a1b1+a2b2+...+anbn 
# (a1 being the first column in the matrix and b1 being the first elements in the vector, a2 being the second column and b2 being the second element in the vector)
#into columns in the new matrix

#Q3: How will we get there?

#A3: We will make an empty matrix to put the new elements into. Then we will use a given matrix[[a,b,c][e,f,g][h,i,j]] where a1-3 are column vectors and then multiply it by vector[[1,2,3] ]. 
# We will then multiply each vector in the matrix with the corresponding element in the vector
#Then we will store those elements into our empty matrix 

def column_method(matrix,vector):

#setting up empty matrix
result = []

#redefining function from 1 to fit problem
def scalar_vector_multi(vector_01):
    return colm*vector

# Initializing result as an empty list
colm = []

#instructions for use to put how many elements are in the vector,
elem = int(input("Insert how many elements you want in the colm of your matrix:"))

#for an element i in range from 0 to the given number of elements append an integer to vector from [0,1,2,...,n]
#aka telleing the user to put their elements in
for i in range(0, elem):
    colm.append(int(input("Enter number:")))

vector =[]	
#defining scalar for the above function
vector = list(input('Insert how many elements you want in your vector: '))
for j in range(0, vector):
    vector.append(int(input("Enter number:")))

#pretty sure you would have to run this 3 total times to get each a1_2,a2_2,a3_2, but this is assigning the result into new vectors
a1_2 = list(map(scalar_vector_multi, colm*vector))
a2_2 = list(map(scalar_vector_multi, colm*vector))
a3_2 = list(map(scalar_vector_multi, colm*vector))

#giving elements definition
a,b,c,e,f,g,h,j = int

# defining the vectors in the matrix to be able to do vector mulitplication (combination of columns)
a1 = [a,b,c]
a2 = [e,f,g]
a3 = [h,i,j]

#multiplying the vectors in the matrix by the elements in the vector

#defining add_vectors for this problem. didn't post the whole thing to save space
def add_vectors(vector_a,vector_b):
#implement #0 function twice since it only adds 2 vectors and we have 3. Stored first part in first_half and then added the last vector to it.
first_half = add_vectors(a1_2,a2_2)
total = add_vectors(first_half,a3_2)

matrix  = [[a,b,c][e,f,g][h,i,j]]
vector = [[1,2,3]]

#defining the matrix and vector that we are using
matrix  = [[a,b,c][e,f,g][h,i,j]]
vector = [[1,2,3]]

#putting the added up products into the result
for elem in total:
    result.append(total)
return(result)


#Problem #5
'''
Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.  
'''

#Write an algorithm to implement scalar-vector multiplication.

#Q1: What do we have?

#A1:  We have 2 matricies stored on the computer and our code from #4

#Q2: What do we want?

#A2: We want a matrix that returns the product of the 2 stored matricies

#Q3: How will we get there?

#A3: we will use the code from #4 but instead of a vector we will turn it into a matrix to do matrix-matrix multi

#defining new function to be equal to #4
def matrix_matrix_multi(matrix_01,matrix_02) = column_method(matrix,vector):
    return matrix_01*matrix_02

#initializing result
result = []

#defining our new elements as elements in the function in #4 to reuse it and keep it understandable
matrix_01 = colm[index]
matrix_02 = vector[index]
#putting the matricies into our function
ans = list(map(matrix_matrix_multi,matrix_01*matrix_02))
#printing answer
print(ans)
