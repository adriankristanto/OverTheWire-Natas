import requests
import bs4
import re


# configuration for natas16
USERNAME = 'natas16'
PASSWORD = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
URL = 'http://natas16.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# according to the source code, there are few symbols that are not filtered out by the regex expression
# which includes $, (, ), {, }
# one way we can execute a command is through the use of $()
# for example, $(grep a /etc/natas_webpass/natas17)