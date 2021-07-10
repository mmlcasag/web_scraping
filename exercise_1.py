import re
import requests
from bs4 import BeautifulSoup

page = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

html = BeautifulSoup(page.content, "html.parser")

print("Page HTML:")
print(html.prettify())
print("")

# EXERCISE 1:
# Grab all social links from the webpage
# Do it at least in three different ways
# One has to use the find/find_all()
# One has to use the select method()

# Approach #1
print("Approach # 1:")
social_media = []

print("UL tags:")
uls = html.find_all("ul", attrs={"class": "socials"})
print(uls)
print("")

for ul in uls:
    anchors = ul.find_all("a")
    for anchor in anchors:
        social_media.append(anchor["href"])
print("")

print("Social media:")
for url in social_media:
    print(url)
print("")

# Approach #2
print("Approach # 2:")
social_media = []

lis = html.body.find_all("li", attrs={"class": re.compile("social")})
print(lis)
print("")

for li in lis:
    anchors = li.find_all("a")
    for anchor in anchors:
        social_media.append(anchor["href"])
print("")

print("Social media:")
for url in social_media:
    print(url)
print("")

# Approach #3
print("Approach # 3:")
social_media = []

anchors = html.body.select("ul.socials li a")
print(anchors)
for anchor in anchors:
    social_media.append(anchor["href"])
print("")

print("Social media:")
for url in social_media:
    print(url)
print("")