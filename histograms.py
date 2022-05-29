#%%
import numpy as np
import matplotlib.pyplot as plt

def mean_stdev(matrix):
    matrix = np.matrix(matrix)
    mean = matrix.mean()
    stdev = np.std(matrix)
    return mean, stdev

def histogram (matrix):
    matrix = np.matrix(matrix)
    histogram = np.zeros(256).astype(int)
    for i in range (256):
        pixels_value_i = np.sum (matrix == i )
        histogram[i] = pixels_value_i
    return histogram

def histogram_cummulated(histogram):
    histogram_c = np.zeros(256).astype(int)
    histogram_c[0] = histogram[0]
    for i in range(1,256):
      histogram_c[i] = histogram_c[i-1]+histogram[i]
    return histogram_c

def show_histogram(hist):
    plt.bar(range(256), hist)
    plt.xlabel('Graylevel / intensity')
    plt.ylabel('Frequency')

def histogram_equalization(matrix):
    hist = histogram(matrix)
    histC = histogram_cummulated (hist)
    hist_transform = np.zeros(256).astype(np.uint8)
    N, M = matrix.shape
    # create the image to store the equalised version
    matrix_eq = np.zeros([N,M]).astype(np.uint8)
    for z in range(256):
        s = ((255)/float(M*N))*histC[z]
        matrix_eq[ np.where(matrix == z) ] = s
        hist_transform[z] = s
    return (matrix_eq)




# %%
