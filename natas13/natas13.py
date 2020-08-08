import requests
import re
import bs4


# configuration for natas13
USERNAME = 'natas13'
PASSWORD = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas13.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(div_content)