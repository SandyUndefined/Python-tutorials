import numpy as np


def matrix_sum(matrix1,matrix2):
    a = np.array(matrix1)
    b = np.array(matrix2)
    return a+b


if __name__ == '__main__':
    r=4
    c=3
    matrix1 = []
    for i in range(r):
        a=[ ]
        for j in range(c):
            a.append(int(input()))
        matrix1.append(a)
    matrix2 = []
    for i in range(r):
        a = []
        for j in range(c):
            a.append(int(input()))
        matrix2.append(a)
    print(matrix_sum(matrix1,matrix2))