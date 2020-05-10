from PIL import Image
im = Image.open('kobe.png')
print(dir(im))
#The attribute I chose was the crop attribute. Essentially, the crop attribute is used in python to
#give the python interpreter editing abilities. The Image.crop() method itself is used to crop a rectangular
#portion of any image.
