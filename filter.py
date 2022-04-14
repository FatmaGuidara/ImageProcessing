from ast import Return
import numpy as np
import random
import math

def noise(matrix):
    matrix = np.matrix(matrix)
    arr = (np.asarray(matrix)).flatten()
    for i in range(len(arr)):
        r = random.randint(0,20)
        if(r==0):
            arr[i] = 0
        elif(r==20):
            arr[i]=255
    matrix = np.matrix(arr.reshape((640, 480)))
    return matrix

def pad(matrix):
    matrix = np.matrix(matrix)
    matrix_padded = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
    return matrix_padded

def filer_moy(matrix):
    padded_matrix = pad(matrix)
    lx,ly = np.shape(padded_matrix)
    new_padded_matrix = np.zeros((lx,ly)).astype(int)
    for x in range(1,lx-1):
        for y in range(1,ly-1):
            new_padded_matrix[x,y] = ( padded_matrix[x-1,y-1] + padded_matrix[x,y-1] + padded_matrix[x+1,y-1] + padded_matrix[x-1,y] + padded_matrix[x,y] + padded_matrix[x+1,y] + padded_matrix[x-1,y+1] + padded_matrix[x,y+1] + padded_matrix[x+1,y+1] )/9          
    new_unpadded_matrix = np.delete(new_padded_matrix, lx-1, 0)
    new_unpadded_matrix = np.delete(new_unpadded_matrix, ly-1, 1)
    new_unpadded_matrix = np.delete(new_unpadded_matrix, 0, 0)
    new_unpadded_matrix = np.delete(new_unpadded_matrix, 0, 1)
    return new_unpadded_matrix

def filer_median(matrix):
    padded_matrix = pad(matrix)
    lx,ly = np.shape(padded_matrix)
    new_padded_matrix = np.zeros((lx,ly)).astype(int)
    for x in range(1,lx-1):
        for y in range(1,ly-1):
            arr = [padded_matrix[x-1,y-1],
                   padded_matrix[x,y-1],
                   padded_matrix[x+1,y-1],
                   padded_matrix[x-1,y],
                   padded_matrix[x,y],
                   padded_matrix[x+1,y],
                   padded_matrix[x-1,y+1],
                   padded_matrix[x,y+1],
                   padded_matrix[x+1,y+1]]
            arr = np.sort(arr)
            new_padded_matrix[x,y] = arr[4]            
    new_unpadded_matrix = np.delete(new_padded_matrix, lx-1, 0)
    new_unpadded_matrix = np.delete(new_unpadded_matrix, ly-1, 1)
    new_unpadded_matrix = np.delete(new_unpadded_matrix, 0, 0)
    new_unpadded_matrix = np.delete(new_unpadded_matrix, 0, 1)
    return new_unpadded_matrix

def signal_to_Noise_Ratio(matrix, filtered_matrix):
    matrix = np.matrix(matrix)
    filtered_matrix = np.matrix(filtered_matrix)
    mean = matrix.mean()
    S = 0
    u = matrix-mean
    B = 0
    v = filtered_matrix - matrix
    lx,ly = np.shape(matrix)
    for x in range(lx):
        for y in range(ly):
            S = S + (u[x,y]*u[x,y])
            B = B + (v[x,y]*v[x,y])
            
    return math.sqrt(S/B)
    

