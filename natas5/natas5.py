import requests
import bs4
import re


# configuration for natas5
USERNAME = 'natas5'
PASSWORD = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
URL = 'http://natas5.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)