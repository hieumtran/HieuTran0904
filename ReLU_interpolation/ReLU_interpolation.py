import numpy as np
import matplotlib.pyplot as plt
import argparse

# Activation function
def ReLU(input):
    return max(0, input)

def heaviside(input):
    if input >= 0: return 1
    else: return 0

def ReLU_interpolation(v_alpha, train_x):
    assert len(v_alpha) == len(train_x)
    result = np.array([])
    
    for i in range(len(v_alpha)-1):
        relu_array = np.array([])
        y_i = 0    
        for j in range(i, len(train_x)-2):
            relu_array = np.append(relu_array, (train_x[j+2]-train_x[i])/(train_x[j+2]-train_x[j+1]))
        y_i += v_alpha[i] + np.sum(v_alpha[i+1:len(v_alpha)-1]*relu_array) + v_alpha[-1]
        result = np.append(result, y_i)
    result = np.append(result, v_alpha[-1])
    return result
    
def vector_alpha(vector_x, vector_F, n):
    # Construct A matrix Rxn element
    matrix_D = np.zeros((n, n))
    for i in range(n-2):
        basic_row_D = np.array([1])
        basic_row_D = np.append(basic_row_D,-(vector_x[i+2]-vector_x[i])/(vector_x[i+2]-vector_x[i+1]))
        basic_row_D = np.append(basic_row_D,(vector_x[i+2]-vector_x[i])/(vector_x[i+2]-vector_x[i+1])-1)
        if i != 0: basic_row_D = np.concatenate([np.zeros(i), basic_row_D])
        basic_row_D = np.concatenate([basic_row_D, np.zeros(n-len(basic_row_D))])
        matrix_D[i, :] = basic_row_D
    matrix_D[-2, [-1, -2]] = [-1, 1]
    matrix_D[-1, [-1]] = 1
    return np.matmul(matrix_D, vector_F.T)

def runge(x):
    return 1 / (1 + 25*x**2)

def main(n, save_name, save_loc):
    # Interval initation
    start = -1
    stop = 1
    step = (stop-start) / n
    train_x = np.arange(start, stop+step, step)
    train_F = runge(train_x)
    truth_x = np.arange(start, stop+0.01, 0.01)
    truth_F = runge(truth_x)
    v_alpha = vector_alpha(train_x, train_F, len(train_x))
    interpolation_F = ReLU_interpolation(v_alpha, train_x)
    viz(truth_x, truth_F, train_x, interpolation_F, save_loc, save_name)

def viz(truth_x, truth_y, train_x, interpolation_F, save_loc, save_name):
    plt.figure(figsize=(15,7))
    plt.plot(truth_x, truth_y, color='blue', label='Exact function')
    plt.scatter(train_x,interpolation_F, marker='*', color='green')
    plt.plot(train_x, interpolation_F, color='red', label='n={}'.format(len(train_x)-1))
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_loc+save_name, dpi=500)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', help='number of observation', type=int)
    parser.add_argument('--save_name', help='save figure name')
    parser.add_argument('--save_loc', help='save figure location')
    args = parser.parse_args()
    main(args.n, args.save_name, args.save_loc)
