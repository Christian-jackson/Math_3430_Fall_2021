#Demo

import LA
import QR
import LS

print('My name is Christian and this is my library of linear algrbra equations' )
print('')

print('''This library has three main files (LA, QR, and LS) starting from basic linear 
algebra (LA) and building on to each other to be able to do more complex calculations (LS)''')
print('')

print('LA (10 linear algebra functions)')
print('')

print('''The first function in LA is add_vectors. This function takes two vectors as its argument and
returns the sums of the inputs stored as a list.''')
test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
print("For example, if a = [1, 2, 4] and b = [3, 1, 2], then add_vectors(a,b) will return")
print('Output for add_vectors: ' + str(LA.add_vectors(test_vector_01,test_vector_02)))
print('')

print('''The second function is scalar_vec_multi. This function takes a scalar number
and a vector as its arguments and returns the vector scaled (vector*scalar) stored as a list''')
test_scalar_01 = 2
print("For example, if s = 2 and b = [1, 2, 4], then scalar_vec_multi(b,s) will return")
print('Output for scalar_vec_multi: ' + str(LA.scalar_vec_multi(test_vector_01,test_scalar_01)))
print('')

print('''The third function is scalar_matrix_multi. This function takes a matrix and a scalar
and returns the scaled matrix (matrix*scalar) stored as a list''')
test_matrix_01 = [[1,2,3],[4,5,6],[7,8,9]]
print("For example, if s = 2 and b = [[1,2,3],[4,5,6],[7,8,9]], then scalar_matrix_multi(b,s) will return")
print('Output for scalar_matrix_multi: ' +str(LA.scalar_matrix_multi(test_matrix_01,test_scalar_01)))
print('')

print('''The fourth function is matrix_add. This function takes two matrices as its arguments
and returns the sum of their elements stored as a list''')
test_matrix_02 = [[2,4,6],[8,10,12],[14,16,18]]
print("For example, if a = [[1,2,3],[4,5,6],[7,8,9]] and b = [[2,4,6],[8,10,12],[14,16,18]], then matrix_add(a,b) return")
print('Output for matrix_add: ' +str(LA.matrix_add(test_matrix_01,test_matrix_02)))
print('')

print('''The fifth function is mat_vec_multi. This function takes a matix and a vector as its
arguments and returns the vector whos elements are the products of the vector and matrix by linear
combination of columns''')
print("For example, if a = [[1,2,3],[4,5,6],[7,8,9]] and b = [3, 1, 2], then mat_vec_multi(a,b) return")
print('Test Output for mat_vec_multi: ' +str(LA.mat_vec_multi(test_matrix_01,test_vector_02)))
print('')

print('''the sixth function is mat_mat_multi. This function takes two matricies as its arguments
and returns the product of their elements stored as a list''')
print("For example, if a = [[1,2,3],[4,5,6],[7,8,9]] and b = [[2,4,6],[8,10,12],[14,16,18]], then mat_mat_multi(a,b) return")
print('Test Output for mat_mat_multi: ' +str(LA.mat_mat_multi(test_matrix_01,test_matrix_02)))
print('')

print('''The seventh function in LA.py is absolute. This function takes a scalar
as its argument and returns its absolute value.''')
print('For example, if scalar = -3j+4, then it will return')
scalar = -3j+4
print(LA.absolute(scalar))
print('')

print('''The eighth function in LA.py is p_norm. This function takes a vector
as its argument and returns its p norm.''')
print('For example, if v = [1, 2, 3], then it will return')
v = [1, 2, 3]
print(LA.p_norm(v))
print('')

print('''The ninth function in LA.py is inf_norm. This function takes a vector
as its argument and returns its infinity norm.''')
print('''For example, if v_2 = [1, 2, 3], then it will return''')
v_2 = [1, 2, 3]
print(LA.inf_norm(v_2))
print('')

print('''The tenth function in LA.py is inf_or_p_norm. This function takes a vector
as its argument and returns its Computes the p-norm, which is the default, or the infinity norm.''')
print('''For example, if v_3 = [3, 2, 1], then it will return''')
v_3 = [3, 2, 1]
print(LA.inf_or_p_norm(v_3, 2, True))
print('')

print('''The eleventh function in LA.py is inner_product. This function takes two vectors
as its arguments and returns their inner product.''')
print('''For example, if vector_1 = [1, 2, 3j] and vector_2 = [2, 3j, 4], then inner_product 
will return''')
vector_e = [1, 2, 3j]
vector_f = [2, 3j, 4]
print(LA.inner_product(vector_e, vector_f))
print('')

print('QR (Gram-schmidt, Orthonormal lists, and the Householder method)')
print('')

print("The first function is SGS which calculates the Q and R for QR factorization.")
print("Ex : if m_1 = [[1, 0, 1], [2, 1, 0]] and m_2 = [[4, 3], [5, 6]] then it will return")
matrix1 = [[1, 0, 1], [2, 1, 0]]
matrix2 = [[4, 3], [5, 6]]
print(QR.SGS(matrix1))
print('')

print('''The second function is orthonorm which takes a matrix as its argument and
returns the orthonormal list of vectors from our input matrix.''')
print("For example, if m_1 = [[5, 12], [15, 25]] then it will return")
matrix1 = [[5, 12], [15, 25]]
print(QR.orthonorm(matrix1))
print('')

print('''The third function is conjugate. This function takes a scalar
as its argument and returns its conjugate.''')
print('''For example, if scalar = 2 + 3j, then it will return''')
scalar_01 = 2 + 3j
print(QR.conjugate(scalar_01))
print('') 

print('''The fourth function is con_trans. This function takes a matrix
as its argument and returns its conjugate transpose.''')
print('''For example, if matrix = [[1, 0], [-5, -5]], then it will return''')
matrix_02 = [[1, 0], [-5, -5]]
print(QR.con_trans(matrix_02))
print('') 

print('''The fifth function is deep_copy. This function takes a matrix
as its argument and returns its deep copy.''')
print('''For example, if matrix = [[1, 0], [-5, -5]], then it will return''')
matrix_02 = [[1, 0], [-5, -5]]
print(QR.deep_copy(matrix_02))
print('') 

print('''The sixth function is sign. This function takes a scalar
as its argument and returns its sign.''')
print('''For example, if scalar = 2, then it will return''')
test_scalar_01 = 2
print(QR.sign(test_scalar_01))
print('') 

print('''The seventh function is V_builder. This function takes a vector
as its argument and returns its V_builder.''')
print('''For example, if vector = [1, 2, 4], then it will return''')
test_vector_01 = [1, 2, 4]
print(QR.V_builder(test_vector_01))
print('') 

print('''The eighth function is identity_matrix. This function takes a scalar
as its argument and returns its the square identity matrix.''')
print('''For example, if scalar = 2, then it will return''')
print(QR.identity_matrix(test_scalar_01))
print('') 

print('''The ninth function is vec_vec_multi. This function takes two vectors
as its arguments and returns its their product.''')
print('''For example, if vector_1 = [2, 3, 4] and vector_2 = [7, 8, 9], then it will return''')
v_1 = [2, 3, 4]
v_2 = [7, 8, 9] 
print(QR.vec_vec_multi(v_1, v_2))
print('') 

print('''The tenth function is F_builder. This function takes a vector
as its argument and returns F.''')
print('''For example, if vector_01 = [1, 0], then it will return''')
vector_01 = [1, 0]
print(QR.F_builder(vector_01))
print('') 
##
print('''The eleventh function is Q_builder. This function takes a matrix
and a scalar as its arguments and returns Q.''')
print('''For example, if matrix = [[1,2,3],[4,5,6],[7,8,9]] and scalar = 1, then it will return''')
print(QR.Q_builder(test_matrix_01, 1))
print('') 

print('''The twelth function is Householder which takes a matrix as its argument and
implements Householder orthogonalization to return calculate QR factorization''')
print("For example, if matrix = [[2,2,1],[-2,1,2],[1,3,1]] then it will return")
matrix7 = [[2, 2, 1], [-2, 1, 2], [1, 3, 1]]
print(QR.Householder(matrix7))
print('')

print('LS (least squares)')
print('')

print("""The first function is backsub. this takes a matrix followed by a vector as its arguments 
and returns x via the back substitution method.""")
print("For example, if matrix = [[1,2,3],[4,5,6],[7,8,9]] and vector = [3, 1, 2], then it will return")
print(LS.backsub(test_matrix_01, test_vector_02))
print('')

print('''the second function is least_squares. This takes a vector and a matrix as its arguments and 
returns the least squares solution via QR decomposition''')
print("For example, if matrix = [[1, 2], [1, 3]] and vector = [5, 7], then it will return")
matrix = [[1, 2], [1, 3]]
vector = [5, 7]
print(LS.least_squares(matrix,vector))
print('')

print('''This is the end of my library for computational mathematics. I didn't get all of the fuctions to work
exactly how id like, especially Gram-Schmidt, but I hope this is usefull''')