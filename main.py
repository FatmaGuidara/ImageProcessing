#%%
from read_write_file import *
from histograms import *
import matplotlib.pyplot as plt

matrix = readImagePgm('pic1.pgm')

# print(np.shape(readImagePgm('pic1.pgm')))
    
# writeImagePgm(matrix, 640, 480, 255, 'output.pgm')

# print(mean_stdev(readImagePgm('pic1.pgm')))


# hist = histogram(matrix)
# show_histogram(hist)
# hist_c = histogram_cummulated(hist)
# show_histogram(hist_c)

# matrix_eq, hist_transform = histogram_equalization(matrix)
# writeImagePgm(matrix_eq, 640, 480, 255, "pic1_equalized.pgm")

# %%
