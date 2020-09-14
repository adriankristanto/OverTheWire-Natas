import requests
import bs4
import re


# configuration for natas25
USERNAME = 'natas25'
PASSWORD = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas25.natas.labs.overthewire.org/'