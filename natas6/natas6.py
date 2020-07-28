import requests
import bs4
import re
import html


# configuration for natas6
USERNAME = 'natas6'
PASSWORD = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
URL = 'http://natas6.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


