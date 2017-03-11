import requests
from bs4 import BeautifulSoup

url = 'http://liebide.com'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
# print soup.body.text
for link in soup.find_all('a'):
	print link.get('href')
