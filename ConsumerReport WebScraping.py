import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

url = 'http://www.consumerreports.org/cro/a-to-z-index/products/index.htm'                    # input your url here
file_name = 'consumer_reports.txt'              # output file name

user_agent = UserAgent()

page = requests.get(url,headers={'user-agent':user_agent.chrome})
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)

def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

all_divs = soup.find_all('div', attrs={'class':"crux-body-copy"})

products = {product.a.string.strip('\n\t\t').strip(): product.a['href'] for product in all_divs}

for key, value in products.items():
    print(key,'     ', value)
