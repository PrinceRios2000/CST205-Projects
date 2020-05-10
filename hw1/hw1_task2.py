# # authors: prince rios and aundre labrador
# last modified: 16 February 2020
# course name: csr205
# Description:This code reads a file in binary and creates a function that takes in a list as a parameter.
# A function called task1 is created. This function initializes three lists and are each given a length of 255 with each value being 0.
# A nested for loop is created to through the height and width of the pixel list and going through the different tuples in the list. At the end
# of the function, three lists will be returned, each containing the number of occurences in the 256 bins. 
import pickle as pkl
from PIL import Image
import numpy as np
file = open('image_matrix.dat', 'rb')
pixel_list = pkl.load(file)
def task2(pixel_list):
	red_list = []
	green_list = []
	blue_list = []
	img = Image.fromarray(np.uint8(pixel_list), 'RGB')
	width, height = img.size
	for i in range(0, 256):
		red_list.append(0)
		green_list.append(0)
		blue_list.append(0)
	for i in range(height):
		for j in range(width):
			for z in range(0, 256):
				if pixel_list[i][j][0] == z:
					red_list[z] += 1
				elif pixel_list[i][j][1] == z:
					green_list[z] += 1
				elif pixel_list[i][j][2] == z:
					blue_list[z] += 1
	return red_list, green_list, blue_list
print(task2(pixel_list))