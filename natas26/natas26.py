import requests
import bs4
import re


# configuration for natas26
USERNAME = 'natas26'
PASSWORD = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas26.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)