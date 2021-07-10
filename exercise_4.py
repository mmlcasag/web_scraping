import re
import requests
from bs4 import BeautifulSoup

page = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

html = BeautifulSoup(page.content, "html.parser")

print("Page HTML:")
print(html.prettify())
print("")

# EXERCISE 4:
# Grab all the images in the page

base_path = "https://keithgalli.github.io/web-scraping/"

images_tag = html.body.select("div.column img")
print(images_tag)
print("")

images_names = [ image["alt"].replace(",","") for image in images_tag ]
print(images_names)
print("")

images_urls = [ base_path + image["src"] for image in images_tag ]
print(images_urls)
print("")

count = 0
for image_url in images_urls:
    print(images_names[count])
    print(image_url)

    image_data = requests.get(image_url).content
    with open("images/" + images_names[count] + ".jpg", "wb") as handler:
        handler.write(image_data)
    
    count = count + 1
    