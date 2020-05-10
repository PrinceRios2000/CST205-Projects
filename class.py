# class Contact(object):
# 	def _init_(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.mobile_phone = ""
# 		self.email = ""
# 	def send_email(self, message):
# 		print("To %s - %s" % (self.email, message))
class Color:
	#A class to define RGB colors
	def __init__(self, name, red, green, blue):
		self.name = name
		self.red = red
		self.green = green
		self.blue = blue
	def luminosity(self):
		return (self.red + self.green + self.blue) / 3
	def breakdown(self):
		string = "Breakdown of " + self.name + ":\n" \
		"Color: (" + str(self.red) + " " + str(self.green) + " " + str(self.blue) + ")\n" \
		"Luminosity: " + str(self.luminosity()) 
		return string
blue = Color("boring blue", 0, 0, 255)
green = Color("normal green", 0, 255, 0)
print("Blue is type: ", type(blue))
print("The breakdown of blue ", blue.name, (blue.red, blue.green, blue.blue))
print("Boring Blue's luminosity is", blue.luminosity())
print(blue.breakdown())
print(green.breakdown())