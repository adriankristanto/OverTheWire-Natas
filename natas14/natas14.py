import requests
import bs4
import re


# configuration for natas14
USERNAME = 'natas14'
PASSWORD = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
URL = 'http://natas14.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)