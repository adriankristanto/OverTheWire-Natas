import requests
import bs4
import re


# configuration for natas28
USERNAME = "natas28"
PASSWORD = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = "http://natas28.natas.labs.overthewire.org/"


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')