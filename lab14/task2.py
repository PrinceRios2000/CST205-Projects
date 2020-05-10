import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import cv2
# https://photobucket.com/
url = 'https://epicgames.com'
raw = requests.get(url).text
soup = BeautifulSoup(raw, 'html.parser')
link = ''
imgs = soup.findAll('img')
for img in imgs:
	link = img.get('src')
	# print(link)
	break
r = urlopen(link)
image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow("window", image)