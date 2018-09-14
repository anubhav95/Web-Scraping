from  urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

file = "Details.csv"
f = open(file, "w")
Headers = "Brand,Product_url\n"
f.write(Headers)
for i in range(1,13):
	my_url = 'https://www.stihlusa.com/products/stihl-top-rated-products/?page={}&viewAll=False'.format(i)
	uClient = uReq(my_url) 
	page_html = uClient.read()
	page_soup = soup(page_html, "html.parser")
	containers = page_soup.find_all("div", {"class":"top-product-image"})

	for container in containers:
		brand= container.img["title"]
		url_name=container.a["href"]

		print("Brand: "+ brand)
		print("url_name: "+ url_name)

		f.write(brand + "," + url_name+ "\n")

f.close()		

			





