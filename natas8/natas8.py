import requests
import bs4
import re
import html


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
print(f'{div_content}\n')


response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
# </div> has an id element, which is invalid, thus, we can't find it with html.parser
soup = bs4.BeautifulSoup(source, 'lxml')
div_content = soup.body.find('div')
print(f'{div_content.prettify()}\n')