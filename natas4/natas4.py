import requests
import bs4
import re


# configuration for natas4
USERNAME = 'natas4'
PASSWORD = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
URL = 'http://natas4.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


response = requests.get(url=URL, auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(div_content)