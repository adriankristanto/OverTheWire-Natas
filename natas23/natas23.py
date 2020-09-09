import requests
import bs4
import re


# configuration for natas23
USERNAME = 'natas23'
PASSWORD = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas23.natas.labs.overthewire.org/'