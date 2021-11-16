import pytest
import LA 

def householder(mtx:list):
    """Performs Householder triangularization
    Parameters
    ----------
    mtx : list
        A input matrix of floats
    Returns
    -------
    a list where first index is an orthogonal matrix Q and the second element 
    is an upper triangular matrix R
    """

def EmptyMat(mat:list[list])->list[list]:
    '''
    creates an empty matrix full of 0's same size as mat
    Args:
    mat: A matrix stored as a list of lists.
    Returns: Matrix the same size as m filled with 0.
    '''
    returnMatrix = []
    for index in range(len(mat)):
        returnMatrix.append(list())
        for j in range(len(mat[index])):
            returnMatrix[index].append(0)
    return returnMatrix

def copyMatrix(m:list[list])->list[list]:
    '''
    This function takes in a matrix m, and iterates entry
    by entry, copying it without reference to a new matrix
    which it then returns.
    Args:
        m: A matrix of vectors stored as list of lists
    Returns:
        Returns a matrix with the same entries as m without
        reference to them.
    '''
    temp = EmptyMat(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            temp[i][j] = m[i][j]
    return temp



def makeColumn(vec:list,n:int)->list:
    '''
    Creates a column vector of size vec filled with 0's with n denoting
    the location of a 1. Then returns this vector.
    Args:
        v: A vector v stored as list
        n: An integer denoting where a 1 will be inserted into the new vector
    
    Returns
        Returns a vector composed of a 1 at position n and 0s everywhere else
    '''
    temp = []
    for i in vec:
        temp.append(0)
    temp[n] = 1
    return temp

def reconstructMatrix(matrixToReconstruct:list[list],BaseMatrix:list[list])->list[list]:
    '''
    Reconstructs matrixToReconstruct to the same size as BaseMatrix
    with an "identity shell" as outlined below.
    1 2     1 0 0    1 0 0 0
    3 4 ->  0 1 2 -> 0 1 0 0
            0 3 4    0 0 1 2
                     0 0 3 4
    Args:
        matrixToReconstruct: A matrix stored as a list of lists
        BaseMatrix: A matrix stored as a list of lists
    Returns:
        Returns a matrix with an inner part as matrixToReconstruct and 
        the size BaseMatrix with an "identity shell" to make up the size
        difference.
    '''
    copyMatrixToReconstruct = copyMatrix(matrixToReconstruct)
    while len(BaseMatrix) > len(copyMatrixToReconstruct):
        for i in copyMatrixToReconstruct:
            i.insert(0,0)
        tempCol = makeColumn(copyMatrixToReconstruct[0],0)
        copyMatrixToReconstruct.insert(0,tempCol)
    return copyMatrixToReconstruct
    

def makeIdentMatrix(m:list[list])-> list[list]:
    '''
    Creates an identity matrix the same size as m.
    Args:
        m: A matrix stored as a list of lists
    Returns:
        Returns an identity matrix of the same size a m.
    '''
    tempMatrix = EmptyMat(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i==j):
                tempMatrix[i][j] = 1
            else:
                tempMatrix[i][j] = 0
    return tempMatrix

def makeSubMatrix(m:list[list])->list[list]:
    '''
    Creates a submatrix out of m that slices off the first row
    and column of m. As outlined as below.
    1 4 7    5 8
    2 5 8 -> 6 9 -> 9
    3 6 9
    Args:
        m: A matrix stored as a list of lists.
    Returns:
        Returns the sliced matrix.
    '''
    temp = copyMatrix(m)
    temp.pop(0)
    for i in temp:
        i.pop(0)
    return temp

def houseHolderCalc(m:list[list], n:int)->list[list]:
    '''
    Calculates the householder transformation matrix for m, Matrix.
    Is created by the formula outlined in class.
    Args:
        m: A matrix stored as a list of lists.
        n: An integer n (Should be set to 0 always)
    Returns:
        Returns the householder transformation matrix for m.
    '''
    x = m[n] # First column of m
    normX = LA.p_norm(x)
    inverseX = LA.scalar_vec_multi(x,-1)
    e = makeColumn(x,n)
    v = LA.add_vectors((LA.scalar_vec_multi(e,normX)),inverseX)
    # Now we calculate F
    numerator = []
    for entry in v:
        column = LA.scalar_vec_multi(v,entry)
        numerator.append(column)
    deno = 2/(LA.inner_product(v,v))
    temp = LA.scalar_matrix_multi(numerator,deno)
    ident = makeIdentMatrix(m)
    temp = LA.scalar_matrix_multi(temp,-1)
    F = LA.add_vectors(temp,ident)
    return F

