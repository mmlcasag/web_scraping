import re
import requests
import pandas
from bs4 import BeautifulSoup

page = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

html = BeautifulSoup(page.content, "html.parser")

print("Page HTML:")
print(html.prettify())
print("")

# EXERCISE 2:
# Grab the table and read it on pandas

print("Table:")
table = html.find("table")
print(table)
print("")

print("Columns:")
columns = table.find("thead").find_all("th")
column_names = [ column.string for column in columns ]
print(column_names)
print("")

print("Rows:")
rows = table.find("tbody").find_all("tr")
table_rows = []
for tr in rows:
    tds = tr.find_all("td")
    row = [ str(cell.get_text()).strip() for cell in tds ]
    print(row)
    table_rows.append(row)
print("")

dataframe = pandas.DataFrame(table_rows, columns=column_names)
print(dataframe)