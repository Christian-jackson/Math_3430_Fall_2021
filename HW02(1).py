"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



#Problem 01

#Q1: What do we have?

#A1: A scalar, called scalar, and a vector stored as a list of elements, vector. 

#Q2: What do we want?

#A2: the scaled vector in a new vector, result, from multiplying by scalar and vector.

#Q3: How will we get there?

#A3: we will create an empty vector, called result. we will then multiply each element in vector by scalar and append it into our result. 

#-PsuedoCode
# def scalar_vec_multi(scalar, vector):
# make and empty set called result
# for each element in vector, multiply by scalar
#append the scaled elements into result
#return result

def scalar_vec_multi(scalar, vector):
  result = []
  for element in vector:
    result.append(element * scalar)
  return (result)

#Problem 02

#Q1: What do we have?

#A1: we have a scalar, called scalar, and a matrix stored as a list of lists called matrix. Each list in matrix represents a row vector. 

#Q2: What do we want?

#A2: we want a matrix which is the scaled version of the given martix.

#Q3: How will we get there?

#A3: we will create an empty matrix called result then we will multiply each vector in our given matrix by scalar and append it into our empty matrix, result. 

#-PsuedoCode
# def scalar_matrix_multi(scalar,matrix)
# make empty matrix called result
# append the result of scalar_vec_multi of each vector in matrix into result
# return result.

def scalar_matrix_multi(scalar,matrix):
  result = []
  for vector in matrix:
    result.append(scalar_vec_multi(scalar,vector))
  return(result)

#Problem 03 

#Q1: What do we have?

#A1: we have 2 matricies that are lists of lists, called matrix_01 and matrix_02. each list in the matricies represent a row vector 

#Q2: What do we want?

#A2: we want a matrix which is the the product of adding matrix_01 and matrix_02 together.

#Q3: How will we get there?

#A3: we will create an empty matrix called result that we will fill with zeros to give our for loop the correct range it needs later. 
# we will then create a for loop that adds each element in the range of matrix_01 and matrix_02 together and put that into our result. 
# once the for loop is finish then it will return our result
  
#-PsuedoCode
# def matrix_add(matrix_01,matrix_02):
# make an result matrix filled with zeros
# run a for loop for each element in the rows
# run a for loop that will iterate the row loop above for each column of the matrix
# tell program what to do for each element in the for loop
# return result.

# explicit for loops
def matrix_add(matrix_01,matrix_02):
  #setting a result column full of 0's
  result = [[0 for x in range(3)] for y in range(3)] 
  for i in range(len(matrix_01)):
      for j in range(len(matrix_01[0])):
        result[i][j] = matrix_01[i][j] + matrix_02[i][j]
  return(result)


#Problem 04


#Problem 05



#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [4 ,6 ,2]

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')

# add_vectors(test_vector_01,test_vector_03) should output [5,8,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_03)))
print('Should have been [5,8,6]')

test_scalar_01 = 2
test_scalar_02 = 3

#scalar_vec_multi(test_scalar_01,test_vector_01) should output [2,4,8]
print('Test Output for scalar_vec_multi: ' + str(scalar_vec_multi(test_scalar_01,test_vector_01)))
print('Should have been [2,4,8]')

#scalar_vec_multi(test_scalar_02,test_vector_02) should output [9,3,6]
print('Test Output for scalar_vec_multi: ' + str(scalar_vec_multi(test_scalar_02,test_vector_02)))
print('Should have been [9,3,6]')

test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_02 = [[2,4,6],[8,10,12],[14,16,18]]
test_matrix_03 = [[1,3,5],[7,9,11],[13,15,17]]

#scalar_matrix_multi(test_scalar_01,test_matrix_01) should be [[2,4,6],[8,10,12],[14,16,18]]
print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_scalar_01,test_matrix_01)))
print('Should have been [[2,4,6],[8,10,12],[14,16,18]]')

#scalar_matrix_multi(test_scalar_02,test_matrix_01) should be [[3,6,9],[12,15,18],[21,24,27]]
print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_scalar_02,test_matrix_01)))
print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

#_matrix_add(test_matrix_01,test_matrix_02) should be [[3,6,9],[12,15,18],[21,24,27]]
print('Test Output for scalar_matrix_multi: ' +str(matrix_add(test_matrix_01,test_matrix_02)))
print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

#_matrix_add(test_matrix_01,test_matrix_02) should be [[2,5,8],[11,14,17],[20,23,26]]
print('Test Output for scalar_matrix_multi: ' +str(matrix_add(test_matrix_01,test_matrix_03)))
print('Should have been [[2,5,8],[11,14,17],[20,23,26]]')