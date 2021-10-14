

"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""
import LA
import pytest

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [4 ,6 ,2]

test_scalar_01 = 2
test_scalar_02 = 3

test_matrix_01 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
test_matrix_02 = [[2, 4, 6],[8, 10, 12],[14, 16, 18]]
test_matrix_03 = [[1, 3, 5],[7, 9, 11],[13, 15, 17]]


# Begin Example
# Problem #0

def add_vectorss(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!



def test_add_vecs():
    #[1+3, 2+1, 4+2] = [4, 3, 6]
    assert LA.add_vectors(test_vector_01, test_vector_02) == [4, 3, 6]
    #[1+4, 2+6, 4+2] = [5, 8, 6]
    assert LA.add_vectors(test_vector_01, test_vector_03) == [5, 8, 6]

def test_scalar_vec_multi():
    #[1*2, 2*2, 4*2] = [2, 4, 8]
    assert LA.scalar_vec_multi(test_vector_01, test_scalar_01) == [2, 4, 8]
    #[3*3, 1*3, 2*3] = [9, 3, 6]
    assert LA.scalar_vec_multi(test_vector_02, test_scalar_02) == [9, 3, 6]

def test_scalar_matrix_multi():
    #[[1*2, 2*2, 3*2],[4*2, 5*2, 6*2],[7*2, 8*2, 9*2]] = [[2, 4, 6],[8, 10, 12],[14, 16, 18]]
    assert LA.scalar_matrix_multi(test_matrix_01, test_scalar_01) == [[2, 4, 6],[8, 10, 12],[14, 16, 18]]
    #[[2*2, 4*2, 6*2],[8*2, 10*2, 12*2],[14*2, 16*2, 18*2]] = [[4, 8, 12], [16, 20, 24], [28, 32, 36]]
    assert LA.scalar_matrix_multi(test_matrix_02, test_scalar_01) == [[4, 8, 12], [16, 20, 24], [28, 32, 36]]

def test_matrix_add():
    #[[1+1, 2+4, 3+6],[4+8, 5+10, 6+12],[7+14, 8+16, 9+18]] = [[3, 6, 9],[12, 15, 18],[21, 24, 27]]
    assert LA.matrix_add(test_matrix_01, test_matrix_02) == [[3, 6, 9],[12, 15, 18],[21, 24, 27]]
    #[[1+1, 2+3, 3+5],[4+7, 5+9, 6+11],[7+13, 8+15, 9+17]] = [[2, 5, 8],[11, 14, 17],[20, 23, 26]]
    assert LA.matrix_add(test_matrix_01, test_matrix_03) == [[2, 5, 8],[11, 14, 17],[20, 23, 26]]

def test_mat_vec_multi():
    #
    assert LA.mat_vec_multi(test_matrix_01, test_vector_02) == [21, 27, 33]
    #
    assert LA.mat_vec_multi(test_matrix_02, test_vector_03) == [84, 108, 132]

def test_mat_mat_multi():
    #
    assert LA.mat_mat_multi(test_matrix_01, test_matrix_02) == [[60, 72, 84], [132, 162, 192], [204, 252, 300]]
    #
    assert LA.mat_mat_multi(test_matrix_01, test_matrix_03) == [[48, 57, 66], [120, 147, 174], [192, 237, 282]]