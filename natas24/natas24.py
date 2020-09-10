import requests
import bs4
import re


# configuration for natas24
USERNAME = 'natas24'
PASSWORD = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas24.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH