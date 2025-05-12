import struct
import numpy as np
import random

def load_images(filename):

    with open(filename, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        images = np.frombuffer(f.read(), dtype=np.uint8).reshape(num, rows, cols)
    return images

def load_labels(filename):
    with open(filename, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    return labels

#images = load_images('data/train-images.idx3-ubyte')
#labels = load_labels('data/train-labels.idx1-ubyte')

in_arr = [random.randint(0, 255) for x in range(0, 10)]
print(in_arr)

def relu(input):
    if input <= 0:
        return 0
    else:
        return input

def mat_mul(mat_a, mat_b):

    if not isinstance(mat_a[0], list):
        a_row = 1
        a_col = len(mat_a)
    else:
        a_row = len(mat_a)
        a_col = len(mat_a[0])

    b_row = len(mat_b)
    b_col = len(mat_b[0])

    if a_col != b_row:
        print(f"Error: Incompatible dimensions! Ax:{a_col} != By:{a_row}")

    out_mat = [[0 for _ in range(a_col)] for _ in range(a_row)]

    if a_row == 1:
        for i in range(a_row):
            for j in range(b_col):
                for k in range(a_col):
                    out_mat[i][j] += mat_a[k] * mat_b[k][j]
    else:
        for i in range(a_row):
            for j in range(b_col):
                for k in range(a_col):
                    out_mat[i][j] += mat_a[i][k] * mat_b[k][j]

    return out_mat

def linear_regression():

    return None

def front_propagation(f_weights, f_bias, input_data):
    in_len = len(input_data)

    for i in range(0, in_len):
        input_data[i] = relu(input_data[i])

def main():
    return 0
main()
