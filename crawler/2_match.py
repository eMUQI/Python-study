from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)

print("-"*100)

res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res1 = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res1[0])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
