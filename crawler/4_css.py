from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen(
    "https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)

print("\n\n找所有 class=month 的信息. 并打印出它们的 tag 内文字.")
soup = BeautifulSoup(html, features="lxml")
month = soup.find_all('li', {"class": "month"})
for m in month:
    print(m.get_text())

print("\n\n找到 class=jan 的信息. 然后在 <ul> 下面继续找 <ul> 内部的 <li> 信息.")
jan = soup.find('ul', {"class": "jan"})
jan_s = jan.find_all('li')
for j in jan_s:
    print(j.get_text())
