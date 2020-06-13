#pip install requests
import requests

url='https://www.runoob.com/python/python-mysql.html'
html=requests.get(url)
linkUrl=html.url;
print(linkUrl)
content=html.content;
print(content)
cookies=html.cookies
print(cookies)
headers=html.headers
print(headers)
#print(html.text)


