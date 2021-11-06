
import LA

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

def orthonorm(Matrix: list[list]) -> list[list]:
    '''Orthonormalizes a Matrix

    Put in a matrix stored as a list of lists, then will run the stable
    Gram-Schmidt function and will return an orthonormalized Q the same span as the
    input matrix

    Input:
        Matrix: A matrix stored as a list of lists

    Return:
        Returns an orthonormalized matrix the same span as the input matrix
    
    '''
    result: list[list] = SGS(Matrix)
    return result[0]