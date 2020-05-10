from PIL import Image
im = Image.open('image.png')
def negative_image(pixel):
	return tuple(map(lambda pixels: 255 - (pixels//2), pixel))
negative_list = map(negative_image, im.getdata())
im.putdata(list(negative_list))
im.show()