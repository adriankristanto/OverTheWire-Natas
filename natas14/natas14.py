import requests
import bs4
import re


# configuration for natas14
USERNAME = 'natas14'
PASSWORD = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
URL = 'http://natas14.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find({'div' : 'id'})
print(f'{div_content}\n')