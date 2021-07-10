import re
import requests
from bs4 import BeautifulSoup

page = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

html = BeautifulSoup(page.content, "html.parser")

print("Page HTML:")
print(html.prettify())
print("")

# EXERCISE 3:
# Grab all the fun facts that have the word "is"

print("Fun Facts")
ul = html.find("ul", attrs={"class": "fun-facts"})
print(ul)
print("")

print("Unfiltered List")
lis = ul.find_all("li")
for li in lis:
    print(li)
print("")

print("Filtered List")
lis = ul.find_all("li")
for li in lis:
    fact = li.find(string=re.compile("is"))
    if fact:
        print(fact)
print("")
