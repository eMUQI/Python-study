from bs4 import BeautifulSoup
from urllib.request import urlopen

#pip3 install beautifulsoup4
#pip3 install lxml

# if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)
print("-"*100)

soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)
