"""
This assignment is due by 11:59pm on 10/29/2021. 

For this assignment you will be writing a python script named QR.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to add are

1) A function which implements the unstable version of Gram-Schmidt for reduced QR
factorization. It will
take as it's argument a matrix and will return a list of two matrices. The first
will be Q and the second will be R from the QR factorization described in the
algorithm.

2) A function which implements the stable version of Gram-Schmidt for reduced QR
factorization.It will take as it's argument a matrix and will return a list of 
two matrices. The first will be Q and the second will be R from the QR factorization 
described in the algorithm.

"""

import LA

def UGS(matrix: list[list]) -> list[list]:

    Q: list = []
    V: list = [element for element in matrix]
    R: list = [([0] * (len(matrix[0]))) for i in range(len(matrix))]

    for outer in range(len(matrix)):
        V[outer] = matrix[outer]
        for inner in range(0, outer):
            R[outer][inner] = LA.inner_product(Q[inner], V[outer])
            s = LA.scalar_vec_multi(Q[inner], -R[outer][inner])
            V[outer] = LA.add_vectors(V[outer], s)
        R[outer][outer] = LA.p_norm((V[outer]))
        Q.append(LA.scalar_vec_multi((V[outer]), (1/R[outer][outer])))
    return [Q, R]
test_matrix_01 = [[1,2,3], [4,5,6]]
print(UGS(test_matrix_01))



def SGS(matrix: list[list]) -> list[list]:
    """Computes QR factorization using the stable Gram-Schmidt process.

    Create an empty list for Q and V and a matrix of zeros for V and R.
    For each element in matrix a, append V. For each outer index, overwrite 
    the outer indexes of R with the p_norm function of the outer index of V.
    This will be the same length of the matrix. Then, we append Q to the scalar 
    vector multiplication function of the the outer index of V and the quotient 
    of 1 over the outer indexes of R. For every inner index we have going from 
    the outer index to the length of the matrix, we will overwrite the inner
    and outer indexes of R with inner product function of the outer index of 
    Q and the inner index of V. Then, we will overwrite a variable, A, with
    the scalar vector multiplication function of outer index of Q, and the
    negative inner and outer indexes of R. Next, we will overwrite the inner 
    index of V with the add vectors function of the inner index of V and s.
    Return the result.

    Args:
        matrix_a: A matrix stored as a list of lists.
    Returns:
        A list producing the matrices Q and R.
    """
    Q: list = []
    V: list = [element for element in matrix]
    R: list = [([0] * (len(matrix[0]))) for i in range(len(matrix))]
    
    for outer in range(len(matrix)):
        R[outer][outer] = LA.p_norm((V[outer]))
        Q.append(LA.scalar_vec_multi((V[outer]), (1 / R[outer][outer])))
        print()
        for inner in range(outer, len(matrix)):
            R[inner][outer] = LA.inner_product(Q[outer], V[inner])
            A = LA.scalar_vec_multi(Q[outer], -R[inner][outer])
            V[inner] = LA.add_vectors(V[inner], A)
    return [Q, R]



test_matrix_01 = [[1,2], [3,4]]
print(UGS(test_matrix_01))
