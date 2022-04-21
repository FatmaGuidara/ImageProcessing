#%%
from read_write_file import *
from histograms import *
from contrast import *
from filter import *
from thresholding import *
from binary_images_filters import *
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


# writeImagePgm(linear_transformation(matrix), 640, 480, 255, 'linear_transformed_contrast_pic1.pgm')

# writeImagePgm(saturated_transformation(matrix, 150, 220), 640, 480, 255, 'saturated_transformed_contrast_pic1.pgm')

noise = noise(matrix)

# writeImagePgm(filer_moy(noise), 640, 480, 255, 'moy_filtered_pic1.pgm')
# writeImagePgm(filer_median(noise), 640, 480, 255, 'median_filtered_pic1.pgm')

# writeImagePgm(filer_moy(matrix), 640, 480, 255, 'moy_filtered_pic1_without_noise.pgm')
# writeImagePgm(filer_median(matrix), 640, 480, 255, 'median_filtered_pic1_without_noise.pgm')

# print(signal_to_Noise_Ratio(matrix,filer_median(noise)))
# print(signal_to_Noise_Ratio(matrix,filer_moy(noise)))


# writeImagePgm(thresholding(matrix, 100), 640, 480, 255, 'images/pic1_manual_thresholding.pgm')
# writeImagePgm(otsu(matrix), 640, 480, 255, 'images/pic1_otsu.pgm')
binary_image = otsu(matrix)

# writeImagePgm(erosion(matrix=binary_image), 640, 480, 255, 'images/pic1_erosion.pgm')
writeImagePgm(dilatation(matrix=binary_image), 640, 480, 255, 'images/pic1_dilatation.pgm')


# %%
