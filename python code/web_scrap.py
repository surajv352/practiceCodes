import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/global/in/Gaming-Laptops/Category/ID-363'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'lxml')
res = page_soup.findAll('div',{'class':'item-container'})
c = res[0]
for i in c:
	print(c.)
