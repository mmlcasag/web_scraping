import re
import requests
from bs4 import BeautifulSoup

outer_page = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
outer_html = BeautifulSoup(outer_page.content, "html.parser")

print("Outer Page HTML:")
print(outer_html.prettify())
print("")

# EXERCISE 5:
# Mystery challenge!

base_path = "https://keithgalli.github.io/web-scraping/"

print("Mystery Challenge")
anchor_tags = outer_html.body.select("div.block a")
links_url = [ base_path + anchor_tag["href"] for anchor_tag in anchor_tags ]
print(links_url)
print("")

all_paragraphs = []
for link_url in links_url:
    inner_page = requests.get(link_url)
    inner_html = BeautifulSoup(inner_page.content, "html.parser")

    print("Page HTML for {}:".format(link_url))
    print(inner_html.prettify())
    print("")

    paragraphs = inner_html.find_all("p", attrs={"id": "secret-word"})
    all_paragraphs.append(paragraphs)

for paragraph in all_paragraphs:
    print(paragraph[0].string)
