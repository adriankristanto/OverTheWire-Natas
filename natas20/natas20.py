import requests
import bs4
import re


# configuration for natas20
USERNAME = 'natas20'
PASSWORD = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
URL = 'http://natas20.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)