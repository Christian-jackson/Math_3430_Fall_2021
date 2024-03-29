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

def add_vectors(vector_a: list[float],vector_b: list[float]) -> list[float]:
  result: list[float] = [0 for element in vector_a]
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
# for and arbitrary number of elements in vector, multiply by scalar
#append the scaled elements into result
#return result

def scalar_vec_multi(vector, scalar):
  result = []
  for index in range(len(vector)):
    result.append(vector[index] * scalar)
  return (result)

#Problem 02

#Q1: What do we have?

#A1: we have a scalar, called scalar, and a matrix stored as a list of lists called matrix. Each list in matrix represents a column vector. 

#Q2: What do we want?

#A2: we want a matrix which is the scaled version of the given martix.

#Q3: How will we get there?

#A3: we will create an empty matrix called result then we will make a for loop for an arbitrary amount of of elements in
# the matrix to run scalar_vec_multi and append it to result.

#-PsuedoCode
# def scalar_matrix_multi(scalar,matrix)
# make empty matrix called result
#create for loop to run scalar_vec_multi for all elements in the matrix
# append the result of scalar_vec_multi of each vector in matrix into result
# return result.

def scalar_matrix_multi(matrix: list[float], scalar: float) -> list[float]:

  result: list[float] = []
  for index in range(len(matrix)):
     result.append(scalar_vec_multi(matrix[index],scalar))
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
# return result
# explicit for loop
# def matrix_add(matrix_01: list[float],matrix_02: list[float]) -> list[float]:
#   #setting a result column full of 0's
#   result: list[float] = [] 
#   #for loop for rows
#   for index:
#     #for loop cor columns
#       for j in range(len(matrix_01[0])):
#         result[i][j] = matrix_01[i][j] + matrix_02[i][j]
#   return(result)


#Problem 04

#Q1: What do we have?

#A1: a matrix thats elements are column vectors. and a column vector stored on the computer

#Q2: What do we want?

#A2: we want to multiply the matrix by the vector using the column method. which multiplies each column in the matrix by the vector then adds them together to get the a new column.
# we will do that for all columns in the matrix.

#Q3: How will we get there?

#A3: we will create an empty matrix called result that we will fill with zeros to give our for loop the correct range it needs later. 
# we will then create a for loop that adds each element in the range of matrix_01 and matrix_02 together and put that into our result. 
# once the for loop is finish then it will return our result

#-PsuedoCode
#make a function mat_vec_multi
# create a matrix full of 0s that is the same size as given matrix.
# create an empty set (result) to append answers to
# create a for loop that runs scalar_vec_multi for all elements in length vector into the rows ih matrix
# define result for next loop
# now run for loop that adds all of those results and puts them into result
# .


def mat_vec_multi(matrix,vector):
  mat_result = [0 for elements in matrix]
  for index in range(len(vector)):
    mat_result[index] = scalar_vec_multi(matrix[index],vector[index])
  result = add_vectors(mat_result[0],mat_result[1])
  for index in range(2, len(mat_result)):
    result = add_vectors(result,mat_result[index])
  return result


#Problem 05

#Q1: What do we have?

#A1: 2 matricies that are the same size

#Q2: What do we want?

#A2: want a new matrix that has the same size as our given matricies whoes elements are the for of the first matrix times the columns of the second function. 
# so result[0] sould equal elements in matrix_01's row 1 times the elements in matrix_02's column 1 and adding all of those together
# to get result[0]

#Q3: How will we get there?

#A3: we will create mat_result that is filled with 0's and is the same size as our given matricies.
# and creat an empty set called result. then we will run a for loop that implements problem #4 on to all elements
# in the matrices and store them in our result.

#-PsuedoCode
# define function called mat_mat_multi
# create an empty set called result
# have a for loop run mat_vec_multi for all elements in the range of given matrix
# in for loop have it append the ans of mat_vec_multi to all elements in our result
# and run it for every element in our given matricies
# return result.

def mat_mat_multi(matrix_0,matrix_1):
  result = []
  for index in range(len(matrix_1)):
    result.append(mat_vec_multi(matrix_0,matrix_1[index]))
  return result

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
print('Test Output for scalar_vec_multi: ' + str(scalar_vec_multi(test_vector_01,test_scalar_01)))
print('Should have been [2,4,8]')

#scalar_vec_multi(test_scalar_02,test_vector_02) should output [9,3,6]
print('Test Output for scalar_vec_multi: ' + str(scalar_vec_multi(test_vector_02,test_scalar_02)))
print('Should have been [9,3,6]')

test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix_02 = [[2,4,6],[8,10,12],[14,16,18]]
test_matrix_03 = [[1,3,5],[7,9,11],[13,15,17]]

#scalar_matrix_multi(test_scalar_01,test_matrix_01) should be [[2,4,6],[8,10,12],[14,16,18]]
print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_matrix_01,test_scalar_01)))
print('Should have been [[2,4,6],[8,10,12],[14,16,18]]')

#scalar_matrix_multi(test_scalar_02,test_matrix_01) should be [[3,6,9],[12,15,18],[21,24,27]]
print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_matrix_02,test_scalar_01)))
print('Should have been [[4, 8, 12], [16, 20, 24], [28, 32, 36]]')

# #_matrix_add(test_matrix_01,test_matrix_02) should be [[3,6,9],[12,15,18],[21,24,27]]
# print('Test Output for scalar_matrix_add: ' +str(matrix_add(test_matrix_01,test_matrix_02)))
# print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

# #_matrix_add(test_matrix_01,test_matrix_02) should be [[2,5,8],[11,14,17],[20,23,26]]
# print('Test Output for scalar_matrix_add: ' +str(matrix_add(test_matrix_01,test_matrix_03)))
# print('Should have been [[2,5,8],[11,14,17],[20,23,26]]')

#mat_vec_multi(test_matrix_01,test_vector_02) should be[{21},{27},{33}]
print('Test Output for mat_vec_multi: ' +str(mat_vec_multi(test_matrix_01,test_vector_02)))
print('Should have been [21, 27, 33]')

#mat_vec_multi(test_matrix_02,test_vector_03) should be[{21},{27},{33}]
print('Test Output for mat_vec_multi: ' +str(mat_vec_multi(test_matrix_02,test_vector_03)))
print('Should have been [84, 108, 132]')

#mat_mat_multi(test_matrix_01,test_matrix_02) should be[[60, 72, 84], [132, 162, 192], [204, 252, 300]]
print('Test Output for mat_mat_multi: ' +str(mat_mat_multi(test_matrix_01,test_matrix_02)))
print('Should have been [[60, 72, 84], [132, 162, 192], [204, 252, 300]]')

#mat_mat_multi(test_matrix_01,test_matrix_03) should be[[48, 57, 66], [120, 147, 174], [192, 237, 282]]
print('Test Output for mat_mat_multi: ' +str(mat_mat_multi(test_matrix_01,test_matrix_03)))
print('Should have been [[48, 57, 66], [120, 147, 174], [192, 237, 282]]')