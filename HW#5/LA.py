
from abc import abstractproperty


def add_vectors(vector_a: list[float],vector_b: list[float]) -> list[float]:
  """Adds the input vectors.

  Creates a zero vector the same size as the input, then overwrites each
  element with the corresponding sum from the input vectors. 

  Args:
    vector_01: A vector stored as a list.
    vector_02: A vector stored as a list. The same size as vector_01.

  Returns:
    The vector sum of the inputs stored as a list.
  """
  result: list[float] = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result


#Problem 01

def scalar_vec_multi(vector: list[float], scalar: float) -> list[float]:
  """Multiplies a vector by a scalar number.

  Creates an empty set whos elements are the appended elements in the given vector scaled up or down by the the scalar number.

  Args:
    vector: A vector stored as a list.
    Scalar: A float number That scales what it's multiplied with

  Returns:
    The vector scaled by Scalar stored as a list.
  """
  result: list[float] = []
  for index in range(len(vector)):
    result.append(vector[index] * scalar)
  return (result)

#Problem 02

def scalar_matrix_multi(matrix: list[float], scalar: float) -> list[float]:
  """Multiplies a matrix by a scalar number.

  Creates an empty set whos elements are the appended elements in the given matrix scaled 
  up or down by the the scalar number.

  Args:
    Matrix: A Matrix stored as a list of column vectors.
    Scalar: A float number That scales what it's multiplied with

  Returns:
    The matrix scaled by scalar stored as a list.
  """

  result: list[list[float]] = []
  for index in range(len(matrix)):
     result.append(scalar_vec_multi(matrix[index],scalar))
  return(result)

#Problem 03 

def matrix_add(matrix_01: list[list[float]],matrix_02: list[list[float]]) -> list[list[float]]:
  """Adds the input matricies.

  Creates an empty set, then overwrites each
  element with the corresponding sum from the input matricies. 

  Args:
    matrix_01: A Matrix stored as a list of column vectors.
    matrix_02: A Matrix stored as a list of column vectors.
               where the number of columns it has is equal to
               the number of rows matrix_01 has.

  Returns:
    The matrix sum of the inputs stored as a list of column vectors.
  """
  #setting a result column full of 0's
  result: list[list[float]] = [] 
  #for loop for rows
  for index in range(len(matrix_01)):
      row = add_vectors(matrix_01[index], matrix_02[index])
      result.append(row)
  return(result)


#Problem 04

def mat_vec_multi(matrix: list[list[float]],vector: list[float]) -> list[float]:
  """Multiplies a matrix and a vector.

  Creates a zero vector the same size as the given vector, then overwrites each
  element with the corresponding product from the input column vector, multiplied in row form, 
  multiplied by its corresponding column in the matrix. Then adding the elements in the rows of the 
  matrix to give us the new element to be put in the zero vector.

  Args:
    matrix: A Matrix stored as a list of column vectors.
    vector: A vector stored as a list.

  Returns:
    The vector whos elements are the products of the vector and matrix by linear
    combination of colums.
  """
  mat_result: list[list[float]] = [0 for elements in matrix]
  for index in range(len(vector)):
    mat_result[index] = scalar_vec_multi(matrix[index],vector[index])
  result: list[float] = add_vectors(mat_result[0],mat_result[1])
  for index in range(2, len(mat_result)):
    result: list[float] = add_vectors(result,mat_result[index])
  return result


#Problem 05

def mat_mat_multi(matrix_0: list[list[float]],matrix_1: list[list[float]]) -> list[list[float]]:
  """Multiplies two matricies where the first matrix's number of rows equal 
      the secondmatrix's number of columns.

  Creates and empty set called result. Then runs mat_vec_multi in a for loop for each
  vector column in matrix_1 to its corresponding row in matrix_0. it then repeats
  mat_vec_multi for every element until it gets to the nth column in matrix_1

  Args:
    matrix_0: A Matrix stored as a list of column vectors.
    matrix_1: A Matrix stored as a list of column vectors where its number of columns
    equal the number of rows in matrix_0.

  Returns:
    The matrix whos elements are the products of matrix_0 and matrix_1 by using the 
    mat_vec_multi function.
  """
  result: list[list[float]] = []
  for index in range(len(matrix_1)):
    result.append(mat_vec_multi(matrix_0,matrix_1[index]))
  return result

#############################################################################################

#HW#04

  
#problem #1

def absolute(S: complex or float) -> float:
    '''Gives absolute value of given scalar.
    
    Takes a scalar sumber, complex or real. For complex numbers
    it takes z = a +jb and multiplies it by z.conjugate() (a - b*1j) and 
    returns the square root of that result. For reals it just squares is
    and square roots it to make it positive. conjugate doesn't effect reals
    because conjugate only deals with +-(b*1j).

    Args:
      Scalar: A scalar number that is in the reals or in complex numbers.

    Returns:
      The real part of the absolute value of your scalar input.

    '''
    z: complex or float = S
    result: float = (z*z.conjugate())**(1/2)
    return result.real
    #returning result.real because I don't think we need the complex 0 in this assignment
#problem #2

def p_norm(vector: list[float], p: float = 2) -> float:
    ''' Gives p-norm of a vector
    
    Takes a list vector, multiplies all its elements to
    the power of your scalar and adds the elements together in 
    a for loop, then returns the scalar(ed) root of that result.

    Args:
      vector: A vector stored as a list
      p: A scalar number which decides which norm to take.
      defaults to 2 if no input is given.

    Returns:
      The p-norm of your vector which is a float number.
    
    '''
    if type(vector[0]) == list:
        print('Incorrect Entry')
        return
    result: complex or float = 0
    for element in vector:
        result += absolute(element)**(absolute(p)) 
    result = result**(1/absolute(p))
    return result
    #need p>=0 so took abs of p to make sure it stays that way
#problem #3

def inf_norm(vector: list[float]) -> float:
    '''Gives greatest absolute valued element of the 
      scalar

    Creates an empty set called result and appends 
    the absolute value, not python abs(), of the elements 
    in the given function to each element in result. Then
    returns the max element in result

    Args:
      vector: A vector stored as a list

    Returns:
      The greatest absolute(element) in the vector.
    '''
    result: list[float] = []
    for element in range(len(vector)):
        result.append(absolute(vector[element]))
    result = max(result)
    return result

#problem #4

def inf_or_p_norm(vector: list[float], boolean: bool = False, p: float = 2) -> float:
    '''Gives infinity-norm or p-norm based on user input

    Runs a Boolean function that calls p-norm (default p = 2) 
    if user only puts the vector into the function. If user wants 
    something there than the 2-norm they must enter all ({0}, (1}, {2})) 
    If user puts in the vector and a True boolean then it returns
    the inf-norm.

    Args:
      vector: A vector stored as a list
      boolean: a boolean value (True or False) decides which
      function to return
      p: A scalar number which decides which norm to take.
      defaults to 2 if no input is given.
    
    Returns:
      Either infinity-norm or p-norm of the vector
    '''
    if boolean:
        return inf_norm(vector)
    else:
        return p_norm(vector, p)

#problem #5

def inner_product(vector_0: list[float], vector_1: list[float]) -> float:
  '''Gives inner product, also known as cross product

  Runs a for loop that gives the summation of the elements in 
  vector_0 times the elements in vector_1. It runs until vector_0
  is out of elements

  Args:
    vector_0: A vector stored as a list
    vector_1: a vector stored as a list the same size
              as vector_0.
        
  Returns:
    the summations of element_0*element_1 for vector_0
    and vector_1
  '''
  result = 0
  for index in range (len(vector_0)):
      result += vector_0[index]*vector_1[index]
  return result
test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
#Test Inputs

# test_vector_01 = [1, 2, 4]
# test_vector_02 = [3, 1, 2]
# test_vector_03 = [4 ,6 ,2]

#  # add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
# print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
# print('Should have been [4,3,6]')

#  # add_vectors(test_vector_01,test_vector_03) should output [5,8,6]
# print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_03)))
# print('Should have been [5,8,6]')

# test_scalar_01 = 2
# test_scalar_02 = 3

#  #scalar_vec_multi(test_scalar_01,test_vector_01) should output [2,4,8]
# print('Test Output for scalar_vec_multi: ' + str(scalar_vec_multi(test_vector_01,test_scalar_01)))
# print('Should have been [2,4,8]')

#  #scalar_vec_multi(test_scalar_02,test_vector_02) should output [9,3,6]
# print('Test Output for scalar_vec_multi: ' + str(scalar_vec_multi(test_vector_02,test_scalar_02)))
# print('Should have been [9,3,6]')

# test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
# test_matrix_02 = [[2,4,6],[8,10,12],[14,16,18]]
# test_matrix_03 = [[1,3,5],[7,9,11],[13,15,17]]

# # #scalar_matrix_multi(test_scalar_01,test_matrix_01) should be [[2,4,6],[8,10,12],[14,16,18]]
# print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_matrix_01,test_scalar_01)))
# print('Should have been [[2,4,6],[8,10,12],[14,16,18]]')

#  #scalar_matrix_multi(test_scalar_02,test_matrix_01) should be [[3,6,9],[12,15,18],[21,24,27]]
# print('Test Output for scalar_matrix_multi: ' +str(scalar_matrix_multi(test_matrix_02,test_scalar_01)))
# print('Should have been [[4, 8, 12], [16, 20, 24], [28, 32, 36]]')

#  #matrix_add(test_matrix_01,test_matrix_02) should be [[3,6,9],[12,15,18],[21,24,27]]
# print('Test Output for matrix_add: ' +str(matrix_add(test_matrix_01,test_matrix_02)))
# print('Should have been [[3,6,9],[12,15,18],[21,24,27]]')

#  #_matrix_add(test_matrix_01,test_matrix_02) should be [[2,5,8],[11,14,17],[20,23,26]]
# print('Test Output for matrix_add: ' +str(matrix_add(test_matrix_01,test_matrix_03)))
# print('Should have been [[2, 5, 8],[11, 14, 17],[20, 23, 26]]')

#  #mat_vec_multi(test_matrix_01,test_vector_02) should be[{21},{27},{33}]
# print('Test Output for mat_vec_multi: ' +str(mat_vec_multi(test_matrix_01,test_vector_02)))
# print('Should have been [21, 27, 33]')

#  #mat_vec_multi(test_matrix_02,test_vector_03) should be[{21},{27},{33}]
# print('Test Output for mat_vec_multi: ' +str(mat_vec_multi(test_matrix_02,test_vector_03)))
# print('Should have been [84, 108, 132]')

#  #mat_mat_multi(test_matrix_01,test_matrix_02) should be[[60, 72, 84], [132, 162, 192], [204, 252, 300]]
# print('Test Output for mat_mat_multi: ' +str(mat_mat_multi(test_matrix_01,test_matrix_02)))
# print('Should have been [[60, 72, 84], [132, 162, 192], [204, 252, 300]]')

#  #mat_mat_multi(test_matrix_01,test_matrix_03) should be[[48, 57, 66], [120, 147, 174], [192, 237, 282]]
# print('Test Output for mat_mat_multi: ' +str(mat_mat_multi(test_matrix_01,test_matrix_03)))
# print('Should have been [[48, 57, 66], [120, 147, 174], [192, 237, 282]]')