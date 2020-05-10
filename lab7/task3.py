from PIL import Image
im = Image.open('lab7_task3.jpg')
width, height = im.size
for x in range(width):
	for y in range(height):
		