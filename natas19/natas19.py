import requests
import bs4
import re


# configuration for natas19
USERNAME = 'natas19'
PASSWORD = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
URL = 'http://natas19.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')