import requests
import bs4
import re
import html


# configuration for natas6
USERNAME = 'natas6'
PASSWORD = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
URL = 'http://natas6.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get source code
response = session.get(URL + 'index-source.html')
# the response contains the source code as encoded html file, e.g. &lt; which should've been <br
# therefore, we can use html.unescape() to decoded the html file
source = html.unescape(response.text).replace('<br />', '')
soup = bs4.BeautifulSoup(source, 'lxml')
print(soup.find('div').prettify())