import requests
import bs4
import re


# configuration for natas2
USERNAME = 'natas2'
PASSWORD = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
URL = 'http://natas2.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


response = requests.get(url=URL, auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')