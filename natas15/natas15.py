import requests
import bs4
import re


# configuration for natas15
USERNAME = 'natas15'
PASSWORD = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
URL = 'http://natas15.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')