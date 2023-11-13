
import requests
from bs4 import BeautifulSoup
import re

def get(url, raw=False):
    try:
        result = requests.get(url)
        return result.content if raw else result.text
    except:
        return False
    

html = get('https://habr.com/ru/companies/ruvds/articles/433408/')
if html:
    root = BeautifulSoup(html,'html.parser')
    links = root.find_all('a')
    for link in links:
        addr = str(link.get('href'))
        if re.match("^(https://|http://)", addr):
            print(addr)
