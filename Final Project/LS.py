#LS
import LA 
import QR 

def backsub(m: list[list], v:list) -> list:
    """
    """
    result: list = [v[-1]*(1/(m[-1][-1]))]
    for e in range(len(m) -2, -1, -1):
        s: float = v[e]
        for i in range(len(result)):
            s -= m[len(m)-1-i][e] * result[i]
        s *= 1/(m[e][e])
        result.append(s)
    return result[:: -1]

def least_squares(m: list[list], v: list) -> list:
    """
    """
    Q, R = QR.SGS(m)
    Q_x = QR.con_trans(Q)
    Q_y = LA.mat_vec_multi(v, Q_x)
    result = backsub(R, Q_y)
    return result

test_matrix_01 = [[1, 2], [3, 4]]
test_matrix_02 = [[2, 4, 6], [6, 8, 10]]
test_matrix_03 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
v_1 = [2, 3]
v_2 = [7, 8, 9] 
v_3 = [5, 3, 10]
