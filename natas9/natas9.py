import requests
import bs4
import re


# configuration for natas9
USERNAME = 'natas9'
PASSWORD = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
URL = 'http://natas9.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
print(response.text)