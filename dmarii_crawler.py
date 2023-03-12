import requests
from bs4 import BeautifulSoup

import time

class Product:
    def __init__(self, name, price, description): 
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return str(self.name) + ", " + str(self.price) + ", " + str(self.description)

subpages =[ '106',
           '107']
        #    '108',
        #    '109',
        #    '110',
        #    '111',
        #    'alice-2mm',
        #    'alice-3mm',
        #    'alice-bundle',
        #    'aria-emerald',
        #    'aria-pink',
        #    'avery-earrings',
        #    'bold-chain-aria-bundle',
        #    'bold-chain-adjustable-ring',
        #    'dual-pearl-necklace',
        #    'gold-beaded-cuffs',
        #    'gold-bean-earrings',
        #    'gold-bold-chain-necklace',
        #    'gold-crescent-large-hoops',
        #    'medium-gold-hoops-202']

headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }

product_list = []
for i in subpages:
    response = requests.get("https://dmaari.com/products/{}".format(i), headers=headers)
    
    content = BeautifulSoup(response.content, 'html.parser')
    
    name_containers = content.find('div', {'class': 'product__title'})
    price_containers = content.find('span', {'class': 'price-item price-item--regular'})
    desc_containers = content.find('div', {'class': 'product__description rte quick-add-hidden'})

    temp_name = name_containers.text
    print(name_containers.text)
    # homework: post-processing: cut temp_name unnecessary parts
    temp_price = price_containers.text
    print(price_containers.text)
    # homework: post-processing : text (temp_price) >integer
    temp_desc = desc_containers.text
    
    print(desc_containers.text)

    time.sleep(1)

    temp_product = Product(temp_name, temp_price, temp_desc)
    product_list.append(temp_product)

#HeRE!!!!
# product_list : the list of all instances containing product information
print("RESULTS:!!!!!")
for product_sample in product_list:
    print(product_sample)


