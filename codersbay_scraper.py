import requests
from bs4 import BeautifulSoup

url = 'https://codersbay.wien'

response = requests.get(url)

# Parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.h2.text)
print(soup.select("h2"))
print(soup.find(class_="text-embraced fw-bold"))
soup.find(class_="text-embraced fw-bold").get(class_)
header = soup.find('h2', class_="text-embraced fw-bold")

#print(soup.div)
cont = soup.find('div', class_="wysiwyg-content")

print(header.text)
print(cont.text)