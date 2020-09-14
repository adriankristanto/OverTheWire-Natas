import requests
import bs4
import re
import html


# configuration for natas25
USERNAME = 'natas25'
PASSWORD = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas25.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(html.unescape(response.text).replace('<br />', ''))