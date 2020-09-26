import requests
import bs4
import re


# configuration for natas27
USERNAME = 'natas27'
PASSWORD = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas27.natas.labs.overthewire.org/'

session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')