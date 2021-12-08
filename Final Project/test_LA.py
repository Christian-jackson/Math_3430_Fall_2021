
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