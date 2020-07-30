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