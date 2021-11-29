#test_LS

import LS
import pytest

test_matrix_01 = [[1, 2], [3, 4]]
test_matrix_02 = [[2, 4, 6], [6, 8, 10]]
test_matrix_03 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
v_1 = [2, 3, 4]
v_2 = [7, 8, 9] 
v_3 = [5, 3, 10]

def test_least_squares():
    assert LS.least_squares(test_matrix_03, v_2) == [[2, 8, 0]]