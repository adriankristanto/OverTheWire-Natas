import requests
import bs4
import re


# configuration for natas11
USERNAME = 'natas11'
PASSWORD = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
URL = 'http://natas10.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)