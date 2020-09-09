import requests
import bs4
import re


# configuration for natas23
USERNAME = 'natas23'
PASSWORD = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas23.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')