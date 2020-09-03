import requests
import bs4
import re


# configuration for natas19
USERNAME = 'natas19'
PASSWORD = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
URL = 'http://natas19.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)