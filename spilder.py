#pip install requests
import requests
from bs4 import BeautifulSoup
import lxml

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
print("############爬取央企名单#############")
url ="http://www.gov.cn/banshi/2012-08/14/content_13001.htm";
doc=requests.get(url)
doc.encoding='utf-8'

print(doc.text)
namePath='//*[@id="Zoom"]/div/table/tbody/tr/td[2]/p/span/a/span/span'




