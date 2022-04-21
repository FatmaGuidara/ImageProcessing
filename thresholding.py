import math
import numpy as np
from histograms import *

def thresholding(matrix, thres):
    matrix = np.matrix(matrix)
     # create a new image with zeros
    f_tr = np.zeros(matrix.shape).astype(int)
    # setting to 0 the pixels below the threshold
    f_tr[np.where(matrix > thres)] = 255
    return f_tr

def otsu(matrix):
    lx,ly = np.shape(matrix)
    matrix = np.matrix(matrix)
    histogramme = histogram(matrix)

    max = -math.inf
    maxSeuil = -1
    
    for seuil in range(1,len(histogramme)-1):
        w1 = (np.sum(histogramme[:seuil]))
        w2 = (np.sum(histogramme[seuil:]))
        # mub = np.array(histogramme[:seuil]).
        # # for i in range(seuil):
        # #     mub = mub + histogramme[i] * i
        # # mub = mub / np.sum(histogram[:seuil])
        # muf = 0
        # # for i in range(seuil,len(histogramme)):
        # #     muf = muf + histogramme[i] * i
        # # muf = muf / np.sum(histogram[seuil:])
        # variance = wb * wf * (mub-muf) * (mub-muf)
        variance1 = np.var(histogramme[:seuil])
        variance2 = np.var(histogramme[seuil:])
        variance = w1 * variance1 + w2 * variance2
        
        if(variance>max):
            max = variance
            maxSeuil = seuil

            
    print(maxSeuil)
    return(thresholding(matrix, maxSeuil))
