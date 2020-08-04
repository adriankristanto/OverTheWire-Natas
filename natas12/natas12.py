import requests
import bs4
import re


# configuration for natas12
USERNAME = 'natas12'
PASSWORD = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
URL = 'http://natas12.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)