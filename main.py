import struct
import numpy as np
import random
e = 2.71828

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

def relu(in_vec):
    out_vec = []
    for i in range(len(in_vec)):
        if in_vec[i][0] <= 0:
            out_vec.append([0])
        else:
            out_vec.append([in_vec[i][0]])
    return out_vec

def soft_max(in_vec):
    out_vec = []
    vec_e = []
    vec_sum = 0
    vec_len = len(in_vec)

    max_val = max(in_vec[i][0] for i in range(vec_len))

    for i in range(vec_len):
        shifted_val = in_vec[i][0] - max_val
        vec_e_cal = e**shifted_val
        vec_e.append(vec_e_cal)
        vec_sum += vec_e_cal

    for i in range(vec_len):
        out_vec.append([vec_e[i] / vec_sum])

    return out_vec

def mat_mul(mat_a, mat_b):

    if not isinstance(mat_a[0], list):
        a_row = 1
        a_col = len(mat_a)
        mat_a = [mat_a]
    else:
        a_row = len(mat_a)
        a_col = len(mat_a[0])

    if not isinstance(mat_b[0], list):
        b_row = len(mat_b)
        b_col = 1
        mat_b = [[item] for item in mat_b]
    else:
        b_row = len(mat_b)
        b_col = len(mat_b[0])

    if a_col != b_row:
        print(f"Error: Incompatible dimensions! Ax:{a_col} != By:{a_row}")

    out_mat = [[0 for _ in range(b_col)] for _ in range(a_row)]

    for i in range(a_row):
        for j in range(b_col):
            for k in range(a_col):
                out_mat[i][j] += mat_a[i][k] * mat_b[k][j]

    return out_mat

def mat_add(mat_a, mat_b):

    out_b = []
    for i in range(len(mat_a)):
        weighted_sum = mat_a[i][0]
        bias = mat_b[i][0]
        out_b.append([weighted_sum + bias])

    return out_b

def wb_init(in_num, w_num):

    w = [[random.uniform(-1, 1) for x in range(in_num)] for y in range(w_num)]
    b = [[random.uniform(-1, 1)] for y in range(w_num)]

    return w, b

def mse(front_out, label):

    return None

def one_hot(Y):

    one_hot_Y = [[0] for _ in range(10)]
    one_hot_Y[Y][0] = 1

    return one_hot_Y

def front_prop(data, w0, b0, w1, b1):

    # Note how the w0 is first matrix, not the data
    lay0 = mat_mul(w0, data)
    lay0 = mat_add(lay0, b0)
    lay0 = relu(lay0)

    lay1 = mat_mul(w1, lay0)
    lay1 = mat_add(lay1, b1)
    print(lay1)
    lay1 = soft_max(lay1)
    print(lay1)

    return lay1

def back_prop():

    return None

def main():

    w0, b0 = wb_init(784, 10)
    w1, b1 = wb_init(10, 10)
    data = [[random.randint(0, 255)] for x in range(784)]

    front_prop(data, w0, b0, w1, b1)

    return 0

main()
