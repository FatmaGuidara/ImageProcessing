import numpy as np
import random
import math

def thresholding(matrix, thres):
    matrix = np.matrix(matrix)
     # create a new image with zeros
    f_tr = np.zeros(matrix.shape).astype(int)
    # setting to 0 the pixels below the threshold
    f_tr[np.where(matrix > thres)] = 255
    return f_tr
