import requests
import bs4
import re


# configuration for natas21
USERNAME = 'natas21'
PASSWORD = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
URL = 'http://natas21.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
# response = session.get(URL + 'index-source.html')
# print(response.text)


# get the second site
response = session.get(re.search(r'href="(.+)"', str(div_content))[1])
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')