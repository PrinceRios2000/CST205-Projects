import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from urllib.request import urlopen
from bs4 import BeautifulSoup
# Use the web page you chose here:
my_site = "https://epicgames.com/"
# req = Request(my_site, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(my_site)
# Print out a portion of the HTML
soup = BeautifulSoup(html.read(), 'html.parser')

# print(html.read()[50_000:50_100])
print(soup.prettify()) 