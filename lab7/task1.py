#authors: Prince Rios and Alex Espinoza
#Date: 17 February 2020
#Description: This code opens an image and finds the index with the larget red value and uses a for loop
#to go through all the pixels in the image to continuously save the largest red value.
from PIL import Image
im = Image.open('lab7_task1.jpg')
width, height = im.size
max_red = 0
coordinates = 0
for x in range(width):
	for y in range(height):
		target_red = im.getpixel((x,y))
		if target_red[0] > max_red:
			max_red = target_red[0]
			coordinates = (x, y)
print(coordinates)