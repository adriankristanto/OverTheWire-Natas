import requests
import bs4
import re
import html


# configuration for natas11
USERNAME = 'natas11'
PASSWORD = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
URL = 'http://natas11.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
body = bs4.BeautifulSoup(response.text, 'html.parser').body
print(f'{body}\n')


response = session.get(URL  + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
body = bs4.BeautifulSoup(source, 'lxml').body
print(body)