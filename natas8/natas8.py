import requests
import bs4
import re


# configuration for natas8
USERNAME = 'natas8'
PASSWORD = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
URL = 'http://natas8.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.body.find('div', {'id' : 'content'})
print(div_content)