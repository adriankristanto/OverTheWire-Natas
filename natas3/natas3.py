import requests
import bs4
import re


# configuration for natas3
USERNAME = 'natas3'
PASSWORD = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
URL = 'http://natas3.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


response = requests.get(url=URL, auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
body = soup.find('body')
div_content = body.find('div', {'id' : 'content'})
print(div_content)