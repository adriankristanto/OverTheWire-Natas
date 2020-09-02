import requests
import bs4
import re


# configuration for natas18
USERNAME = 'natas18'
PASSWORD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
URL = 'http://natas18.natas.labs.overthewire.org/'
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