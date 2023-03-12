# crawling
# computer science - crawling
# Website
# website contents - collecting
# parsing
#jqoiwj

import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    # https://kr.investing.com/currencies/usd-krw
    # response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    response = requests.get("https://dmaari.com/products/{}".format(target1), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    # print(content.text)

    containers = content.find('span', {'class': 'price-item price-item--regular'})
    print(containers.text)


for i in range(4):
    id = i + 106
    get_exchange_rate(str(id))


# DDoS - (Distributed) Denial of Service -> Cloudflare -> block bot
# Netflix.com = B pepple
# Servers = computer 
# Users 
# Dmarii.com - 200 
# Bots - adversarial crawling
# 1 bot - 200 requests -> block