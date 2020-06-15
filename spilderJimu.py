import sys
import json
from bs4 import BeautifulSoup
import requests

url='https://box.jimu.com/Venus/List'
html=requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
context=html.text
#print(context)
title_tag = soup.title
print(title_tag)
print(title_tag.text)
listp=soup.find('project-list')
print(listp)


