import requests
import bs4
import re


# configuration for natas15
USERNAME = 'natas15'
PASSWORD = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
URL = 'http://natas15.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)