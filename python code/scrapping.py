import requests
import bs4
res = requests.get('https://www.newegg.com/global/in/Gaming-Laptops/Category/ID-363')
a = type(res)
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
type(soup)
# soup.select('.mw-headline')
# for i in soup.select('.mw-headline'):
# 	print(i.text)
# for i in soup.select('.item-container'):
# 	print(i.text)
ans = soup.select('.item-container')
r1 = soup.select('.page-title')
print(r1)