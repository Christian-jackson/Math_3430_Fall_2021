
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
    V: list = []
    R: list = [[0, 0], [0, 0]]
    
    for element in matrix:
        V.append(element)
    for outer_index in range(len(matrix)):
        R[outer_index][outer_index] = LA.p_norm((V[outer_index]))
        Q.append(LA.scalar_vec_multi((1 / R[outer_index][outer_index]), (V[outer_index])))
        for inner_index in range(outer_index, len(matrix)):
            R[inner_index][outer_index] = LA.inner_product(Q[outer_index], V[inner_index])
            s = LA.scalar_vec_multi(Q[outer_index], -R[inner_index][outer_index])
            V[inner_index] = LA.add_vectors(V[inner_index], s)
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
    result: list[list] = SGS(Matrix)[0]
    return result


#################################################################################

def conjugate(a: float) -> float:
    """Calculates the conjugate

    set an element 'result' equal to the real part plus the
    negative of the imaginary part with the i maginary number
    muliplied to the .imag part.

    Args:
        a: A float scalar

    Returns:
        The conjugated scalar
    
    """
    result: float = a.real + -a.imag*1j
    return result

def con_trans(m: list[list[complex]]) -> list[list[complex]]:
    """ Calculates conjugate transpose of given matrix

    Takes the conjugate of each element in the matrix then 
    transposes it.

    Args:
        m: A matrix stored as a list of lists.

    Returns:
        The conjugate of each element in the given matrix
        transposed.
    
    """
    a: complex = 0
    result: list[list[complex]] = [([0] * (len(m))) for i in range(len(m[0]))]
    for column in range(len(m)):
        for row in range(len(m[0])):
            a = m[column][row]
            a = conjugate(a)
            result[row][column] = a
    return result

def deep_copy(m: list[list]) -> list[list]:
    """ Creates a deep copy of the given matrix

    Creates a zero matrix with the same size as the given
    matrix. Then replaces all the elements with the given matrix
    and returns that matrix.

    Args:
        m: a matrix stored as a list of lists

    Returns:
        The deep copy of the given matrix
    
    """
    i = [[0 for element in range(len(m[0]))] for index in range(len(m))]
    for index in range(len(m)):
        for element in range(len(m[index])):
            i[index][element] = m[index][element]
    return i

def sign(x: float)-> float:
    """Figures if the input float is pos or neg.
    
    if input is greater than or equal to 0 then it returns 1, 
    else (input strictly is less than 0) returns -1.
    
    Args:
        x: A number stored as a float
        
    Returns:
        either 1 if x is pos or -1 if x is negative.
    """
    if x>=0:
        return 1
    else:
        return -1

def V_builder(vec: list) -> list:
    """ Calculates the reflection vector of an input vector.
    
    The sign of vector times the pNorm of the vector times the vector 'a'
    whos first element is 1, but the rest are 0 added with the input vector.

    Args:
        vec: A column vector

    Returns:
        The reflection of the input vector

    """
    a = [0 for element in range(len(vec))]
    a[0] = 1
    V = LA.add_vectors(vec, LA.scalar_vec_multi(a, sign(vec[0])*LA.p_norm(vec)))
    return V

def identity_matrix(x: int) -> list[list]:
    """ Creates an identity matrix the size of the given int

    creates a martix of zeros the size of input int then replaces the diagonal
    elements with 1.

    Args:
        x: An integer that decides the size of the matrix

    Returns:
        The identity matrix
    """
    i: list = [[0 for element in range(x)] for index in range(x)]
    for index in range(x):
        i[index][index] = 1
    return i

def vec_vec_multi(v_1: list, v_2: list) -> list:
    """Multiplies two vectors together

    Creates an empty list called result. Then for 
    every element in the range of length of v_2 it 
    appends the scalar_vec_multi of v_1 and v_2 to 
    the result. Pretty much makes v_2 a row vector
    so that we can multiply them together.

    Args:
        v_1: A vector stored as a list
        v_2: A vector stored as a list the same size as v_1

    Returns:
        The product of v_1 and v_2

    """
    result: list = []
    v_1 == v_2
    for x in range(len(v_2)):
        result.append(LA.scalar_vec_multi(v_1, v_2[x]))
    return result

def F_builder(vec: list) -> list[list]:
    """Calculates the F_k value
    
    First we set 's' equal to -2 over the p_norm of vector_a squared. 
    Then, we use the scalar_matrix_multi of the scalar, s, and vec_vec_multi
    of 'vec' by itself and set it equal to x. We then use the add_matrix (from LA)
    of the identity matrix with the length of 'vec, and add it to x and set that
    equal to y and return y.

    Args:
        vec: A vector stored as a list

    Returns:
        The F_k matrix
    """
    s: float = -2/(LA.p_norm(vec))**2
    x: list = LA.scalar_matrix_multi(vec_vec_multi(vec, vec), s)
    y: list[list] = LA.matrix_add(identity_matrix(len(vec)), x)
    
    return y

def Q_builder(m: list[list], x: int) -> list[list]:
    """ Builds a iteration of the orthogonal matrix Q.

    Set the elements of the input matrix to 0. Then for every 
    index with the length of 'm', and for every element in 
    the range with the length of the index of 'm', if the 
    scalar plus the index or the scalar plus the element is less 
    than the length of the index of 'm', then overwrite the 
    index and element of 'A' is with the scalar plus index and the 
    scalar plus element of 'm'. Then we make V be 'V_builder'
    of the first element in 'A' and make F be 'F_builder' of
    V. Then it has Q be the identity matrix with the length of the 
    given matrix. For the index in the range of the 'x'
    to the length of 'Q', overwrite the index and element of
    'Q' with the element minus 'x' of F and the index minus 'x'.
    Then it Returns 'Q'

    Args:
        m: A matrix stored as a list of lists
        x: An iteration index stored as an int

    Returns:
        Q: A matrix stored as a list of lists
    
    """
    A: list = [[0 for element in range(x, len(m[index]))] for index in range(x, len(m))]
    for index in range(len(m)):
        for element in range(len(m[index])):
            if x + index < len(m[index]):
                if x + element < len(m[index]):
                    A[index][element] = m[x + index][x+element]

    V = V_builder(A[0])
    F = F_builder(V)

    Q = identity_matrix(len(m))
    for index in range(x, len(Q)):
        for element in range(x, len(Q)):
            Q[index][element] = F[index - x][element - x]

    return Q

def Householder(m: list[list]) -> list[list]:
    """ Does QR decomposition using Householder
    
    Creates a 'deep_copy' of the give matrix 'm' and
    sets it to 'R'. Then makes an empty list 'Q_list'
    Then starts a for loop where for every element
    in range of the length of 'R', set 'Q_list' equal to the
    'Q_builder' of 'R' and 'k', set 'R' equal to the 'mat_mat_multi'
    of 'x' and 'R', and append 'x' to 'Q_list'. After that loop
    it then sets 'Q' to be the 'con_trans' of the first element
    in 'Q_list'. Then it goes into another for loop where from 1
    to 'len(Q_list)' it takes each elements 'con_trans' in 'Q_list'
    then performs 'mat_mat multi' to 'Q' and 'ct' and sets it equal 
    to 'Q'. Then returns [Q, R]

    Args:
        m: a matrix stored as a list of lists
    
    Returns:
        QR decomposition
    """
    R:list = deep_copy(m)
    Q_list: list = []
    for k in range(len(R)):
        x: list = Q_builder(R, k)
        R = LA.mat_mat_multi(x, R)
        Q_list.append(x)
        
    Q: list = con_trans(Q_list[0])
    
    for index in range (1, len(Q_list)):
        ct = con_trans(Q_list[index])
        Q = LA.mat_mat_multi(Q, ct)
    
    return[Q, R]
