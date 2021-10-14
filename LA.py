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

def scalar_vec_multi(vector: list[float], scalar: float) -> list[float]:
  result: list[float] = []
  for index in range(len(vector)):
    result.append(vector[index] * scalar)
  return (result)

#Problem 02

def scalar_matrix_multi(matrix: list[float], scalar: float) -> list[float]:

  result: list[float] = []
  for index in range(len(matrix)):
     result.append(scalar_vec_multi(matrix[index],scalar))
  return(result)

#Problem 03 

def matrix_add(matrix_01: list[float],matrix_02: list[float]) -> list[float]:
  #setting a result column full of 0's
  result: list[float] = [] 
  #for loop for rows
  for index in range(len(matrix_01)):
      row = add_vectors(matrix_01[index], matrix_02[index])
      result.append(row)
  return(result)


#Problem 04

def mat_vec_multi(matrix: list[float],vector: list[float]) -> list[float]:
  mat_result: list[float] = [0 for elements in matrix]
  for index in range(len(vector)):
    mat_result[index] = scalar_vec_multi(matrix[index],vector[index])
  result: list[float] = add_vectors(mat_result[0],mat_result[1])
  for index in range(2, len(mat_result)):
    result = add_vectors(result,mat_result[index])
  return result


#Problem 05

def mat_mat_multi(matrix_0: list[float],matrix_1: list[float]) -> list[float]:
  result: list[float] = []
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

# #scalar_matrix_multi(test_scalar_01,test_matrix_01) should be [[2,4,6],[8,10,12],[14,16,18]]
print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_matrix_01,test_scalar_01)))
print('Should have been [[2,4,6],[8,10,12],[14,16,18]]')

 #scalar_matrix_multi(test_scalar_02,test_matrix_01) should be [[3,6,9],[12,15,18],[21,24,27]]
print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_matrix_02,test_scalar_01)))
print('Should have been [[4, 8, 12], [16, 20, 24], [28, 32, 36]]')

 #matrix_add(test_matrix_01,test_matrix_02) should be [[3,6,9],[12,15,18],[21,24,27]]
print('Test Output for matrix_add: ' +str(matrix_add(test_matrix_01,test_matrix_02)))
print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

 #_matrix_add(test_matrix_01,test_matrix_02) should be [[2,5,8],[11,14,17],[20,23,26]]
print('Test Output for matrix_add: ' +str(matrix_add(test_matrix_01,test_matrix_03)))
print('Should have been [[2, 5, 8],[11, 14, 17],[20, 23, 26]]')

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