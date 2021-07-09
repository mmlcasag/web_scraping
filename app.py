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

# Start using BeautifulSoup to scrape
first_header = soup.find("h2")
print('find("h2") example:')
print(first_header)
print("")
# Notice that we have 2 <h2> tags in the page
# The find function returns only the first occurrence

# If you want all the occurrences you should use the find_all function
print('find_all("h2") example:')
headers = soup.find_all("h2")
print(headers)
print("")

# Now you can loop through all of them
print('Looping through the headers:')
for header in headers:
    print(header)
print("")

# You can also pass in a list of elements to look for
print('find(["h1","h2"]) example:')
first_header = soup.find(["h1","h2"])
print(first_header)
print("")

print('find_all(["h1","h2"]) example:')
all_headers = soup.find_all(["h1","h2"])
print(all_headers)
print("")

# Let's say you want to find all paragraphs within the web page
print('find_all("p") example:')
paragraphs = soup.find_all("p")
print(paragraphs)
print("")

# You can pass in attributes to the find/find_all function
# Let's say you now want only the paragraph with the id from the previous example
print('find_all("p", attrs={"id": "paragraph-id"}) example:')
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)
print("")

# You can nest find/find_all calls
print('find("body") example:')
body = soup.find("body")
print(body)
print("")
# Here you have the entire body element
# But now let's say you want only the first div tag inside the body
# You can do this
print('find("div") inside the body example:')
div = body.find("div")
print(div)
print("")
# Now let's extract the header from the div
print('find("h1") inside the div example:')
header = div.find("h1")
print(header)
print("")

# We can search specific strings in our find/find_all calls
# Let's say we want to search for the word "Some bold text" inside our paragraphs
print('find_all("p", string="Some bold text") example:')
string_search = soup.find_all("p", string="Some bold text")
print(string_search)
print("")

# If you want to search for just a part of the string (like a LIKE '%%' clause)
# You can use regex, for example:
import re

print('find_all("p", string=re.compile("Some")) example:')
string_search = soup.find_all("p", string=re.compile("Some"))
print(string_search)
print("")

# if you want to ignore case you can use regex like this
print('find_all("h2", string=re.compile("(H|h)eader")) example:')
string_search = soup.find_all("h2", string=re.compile("(H|h)eader"))
print(string_search)
print("")

# the SELECT() method (CSS selector)
print('select("p") example:')
paragraph = soup.select("p")
print(paragraph)
print("")

# Now let's say we only want to print paragraphs that are immediately inside divs
# We need to use selectors like this
print('select("div p") example:')
paragraph = soup.select("div p")
print(paragraph)
print("")

# This page might be useful to learn how to best use selectors:
# https://www.w3schools.com/cssref/css_selectors.asp

# Now let's say we only want the paragraph right after the h2 tag
# We need to use selectors like this
print('select("h2 ~ p") example:')
paragraph = soup.select("h2 ~ p")
print(paragraph)
print("")

# Let's say we want to grab the <b> tag inside the <p> tag with the "paragraph-id" id
# We need to use selectors like this
print('select("p#paragraph-id b") example:')
bold_text = soup.select("p#paragraph-id b")
print(bold_text)
print("")

# Let's say we want to grab the <p> tags inside the <body> tag but only those who are direct descendents
# We need to use selectors like this
print('select("body > p") example:')
paragraphs = soup.select("body > p")
print(paragraphs)
print("")

# You can also loop through them
for paragraph in paragraphs:
    print(paragraph.select("i"))
print("")

# Let's say we want to grab an element by a specific property
# We need to use selectors like this
print('select("[align=middle]") example:')
elements = soup.select("[align=middle]")
print(elements)
print("")
