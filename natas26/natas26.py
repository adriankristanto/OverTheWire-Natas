import requests
import bs4
import re


# configuration for natas26
USERNAME = 'natas26'
PASSWORD = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas26.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH