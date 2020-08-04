import requests
import bs4
import re


# configuration for natas12
USERNAME = 'natas12'
PASSWORD = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
URL = 'http://natas12.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(div_content)