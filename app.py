import requests
from bs4 import BeautifulSoup

url = "https://www.groupon.com/browse/salt-lake-city?address=Vernal%2C+UT+84078&lat=40.455&lng=-109.529&locale=en_US"
HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537/6',
   'origin': url,
   'referer': url
}
page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, "html.parser")

groupons = []

card_content_tags = soup.find_all('div', class_="cui-content")

for tag in card_content_tags:
    deal_name = tag.find('div', class_='cui-udc-title')
    address = tag.find('span', class_='cui-location-name')
    stars = tag.find('div', class_='cui-location-name')
    regular_price = tag.find('div', class_='cui-price-original')
    discount = tag.find('div', class_='cui-price-discount')
    urgency_price = tag.find('div', class_='cui-verbose-urgency-price')
    description = tag.find('div', class_='cui-udc-subtitle')

    if not deal_name:
        continue

    deal_name = deal_name.text.strip()

    if address:
        address = address.text.strip()

    if stars:
        stars = stars.text.strip()

    if regular_price:
        regular_price = regular_price.text.strip()

    if discount:
        discount = discount.text.strip()
    
    if description:
        description = description.text.strip()
    
    if urgency_price:
        urgency_price = urgency_price.text.strip()
        
    groupons.append({
    'name': deal_name,
    'address': address,
    'stars': stars,
    'regular_price': regular_price,
    'discount_price': discount,
    'urgency_price': urgency_price,
    'description': description
        })    

for groupon in groupons:
    print('\n')
    fields = ['name','address','stars','regular_price','discount_price','urgency_price','description']
    for field in fields:
        if groupon[field] != None:
            print(field.title(),':', groupon[field])