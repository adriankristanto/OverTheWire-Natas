import requests
import bs4
import re
import html


# configuration for natas10
USERNAME = 'natas10'
PASSWORD = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
URL = 'http://natas10.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
div = bs4.BeautifulSoup(source, 'lxml').body.div
print(f'{div}\n')