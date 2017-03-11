#coding: utf-8
from bs4 import BeautifulSoup
import urllib
import requests

html = requests.get('http://www.moko.cc/mtb/model/1612478/space.html')
soup = BeautifulSoup(html.text, 'html.parser')
# img_url = []
i = 1
for img in soup.find_all('img'): #, class_='BDE_Image'
	urllib.urlretrieve(str(img['src']),'%s.jpg' % i)
	i += 1
