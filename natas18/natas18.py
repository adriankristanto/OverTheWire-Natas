import requests
import bs4
import re


# configuration for natas18
USERNAME = 'natas18'
PASSWORD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
URL = 'http://natas18.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)