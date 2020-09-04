import requests
import bs4
import re


# configuration for natas20
USERNAME = 'natas20'
PASSWORD = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
URL = 'http://natas20.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)