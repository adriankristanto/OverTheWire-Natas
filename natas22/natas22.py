import requests
import bs4
import re


# configuration for natas22
USERNAME = 'natas22'
PASSWORD = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas22.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')