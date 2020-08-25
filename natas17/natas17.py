import requests
import bs4
import re


# configuration for natas17
USERNAME = 'natas17'
PASSWORD = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
URL = 'http://natas17.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')