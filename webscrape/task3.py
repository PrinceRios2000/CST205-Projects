#Authors: Prince Rios and Alex Espinoza
#Last modified: 13 March 2020
#Description: This code uses multiple libraries to import necessary classes. A variable raw is created to hold the text of the code for the website.
#Then, soup is created to hold the html of the website. Finally, the code uses the find_all() function that takes in img as a parameter
#to look for all the cases of img in the html. Finally, a for loop is used to go through the different image url's and breaks after just one 
#url is printed. 

import requests
import numpy as np`
import cv2
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.epicgames.com/"

raw = requests.get(url).text

soup = BeautifulSoup(raw, 'html.parser')

imgs = soup.find_all('img')

for img in imgs:
	link = img.get('src')
	print(link)
	break

r = urlopen(f'{link}')
image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)