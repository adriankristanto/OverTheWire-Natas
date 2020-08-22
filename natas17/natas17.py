import requests
import bs4
import re


# configuration for natas17
USERNAME = 'natas17'
PASSWORD = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
URL = 'http://natas17.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)