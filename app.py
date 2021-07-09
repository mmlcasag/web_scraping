import requests
from bs4 import BeautifulSoup

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a BeautifulSoup object
soup = BeautifulSoup(r.content, "html.parser")
# the second argument is to avoid the BeautifulSoup warning message
# https://stackoverflow.com/questions/33511544/how-to-get-rid-of-beautifulsoup-user-warning

# Print out our HTML
print(soup)

# Print out our HTML formatted in a more readable way
print(soup.prettify())