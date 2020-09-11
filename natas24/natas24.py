import requests
import bs4
import re
import html


# configuration for natas24
USERNAME = 'natas24'
PASSWORD = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas24.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
source = bs4.BeautifulSoup(source, 'lxml')
# print(source.prettify())