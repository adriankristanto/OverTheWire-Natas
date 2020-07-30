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
