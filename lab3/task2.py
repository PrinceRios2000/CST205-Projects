color_dictionary = {
	"Red":(250, 50, 7), 
	"Green":(0, 255, 0), 
	"Blue":(0, 0, 250), 
	"Magenta":(250, 0, 250), 
	"Cyan":(0, 250, 250), 
	"Yellow":(250, 250, 0)
}

print(f'The Blue channel of Magenta has a value of {color_dictionary["Magenta"][2]}.')
print(f'The Green channel of Yellow has a value of {color_dictionary["Yellow"][1]}.')
print(f'The Red channel of Cyan has a value of {color_dictionary["Cyan"][0]}.')
for key, value in color_dictionary.items():
	if key[1] == 'e':
		print(value)