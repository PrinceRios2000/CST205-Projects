# # authors: prince rios and aundre labrador
# last modified: 16 February 2020
# course name: cst205
# Description:This code reads a file in binary and creates a function that takes in a list as a parameter.
# A function called task1 is created. This function initializes three lists with all values initialized to 0 and uses nested for loops to iterate
# through the list of pixels and returns a dictionary with three keys. The corresponding values of the keys are lists containing the 
# number of occurences for each bin. 
import pickle as pkl
from PIL import Image
import numpy as np
file = open('image_matrix.dat', 'rb')
pixel_list = pkl.load(file)
def task1(pixel_list):
	red_list = [0, 0, 0, 0]
	green_list = [0, 0, 0, 0]
	blue_list = [0, 0, 0, 0]
	bin1 = range(0,64)
	bin2 = range(64,128)
	bin3 = range(128,192)
	bin4 = range(192,256)
	img = Image.fromarray(np.uint8(pixel_list), 'RGB')
	width, height = img.size  
	for i in range(height):
		for j in range(width):
			if pixel_list[i][j][0] in bin1:
				red_list[0] += 1
			elif pixel_list[i][j][0] in bin2:
				red_list[1] += 1
			elif pixel_list[i][j][0] in bin3:
				red_list[2] += 1
			elif pixel_list[i][j][0] in bin4:
				red_list[3] += 1
	for i in range(height):
		for j in range(width):
			if pixel_list[i][j][1] in bin1:
				green_list[0] += 1
			elif pixel_list[i][j][1] in bin2:
				green_list[1] += 1
			elif pixel_list[i][j][1] in bin3:
				green_list[2] += 1
			elif pixel_list[i][j][1] in bin4:
				green_list[3] += 1
	for i in range(height):
		for j in range(width):
			if pixel_list[i][j][2] in bin1:
				blue_list[0] += 1
			elif pixel_list[i][j][2] in bin2:
				blue_list[1] += 1
			elif pixel_list[i][j][2] in bin3:
				blue_list[2] += 1
			elif pixel_list[i][j][2] in bin4:
				blue_list[3] += 1

	bin_count = {
	"Red": red_list,
	"Green": green_list,
	"Blue": blue_list
	}
	return bin_count
print(task1(pixel_list))
file.close()
