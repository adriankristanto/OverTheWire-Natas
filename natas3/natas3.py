import requests
import bs4
import re


# configuration for natas3
USERNAME = 'natas3'
PASSWORD = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
URL = 'http://natas3.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)