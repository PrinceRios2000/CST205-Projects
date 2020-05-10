# #Authors: Prince Rios and Alex Espinoza
# #Last modified: 13 March 2020
# #Description: This code uses multiple libraries to import necessary classes. A variable raw is created to hold the text of the code for the website.
# #Then, soup is created to hold the html of the website. Finally, the code uses the find_all() function that takes in img as a parameter
# #to look for all the cases of img in the html. Finally, a for loop is used to go through the different image url's and breaks after just one 
# #url is printed. 

# import requests
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# from PIL import Image
# url = "https://epicgames.com/"

# raw = requests.get(url).text

# soup = BeautifulSoup(raw, 'html.parser')

# imgs = soup.find_all('img')

# for img in imgs:
# 	link = img.get('src')
# 	img = Image.open(f'{link}')
# 	print(link)
# 	break
# img.show()
from PIL import Image

img = Image.open('https://cdn2.unrealengine.com/Diesel%2Fstore%2Ffeatured-carousel-d2wony-br%2FWLK_Expansion_Store_Landscape_2560x1440-2560x1440-32ae96dcaf5732bf0c0046e79d8745ce49828b7b.jpg?h=1080&resize=1&w=1920')
img.show()