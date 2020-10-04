import requests
import bs4
import re
import urllib
import base64


# configuration for natas28
USERNAME = "natas28"
PASSWORD = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = "http://natas28.natas.labs.overthewire.org/"


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# demonstrate the usage of the site
data = {
    "query" : "a",
    "submit" : "submit"
}
response = session.post(URL, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# see the url
print(response.url)
# as we can see, the query parameter seems to be url encoded and base64 decoded
query_param = re.search(r'query=(.+)', response.url)[1]
# unquote the query parameter
query_param = urllib.parse.unquote(query_param)
# base64 decode it and display it as hex
query_param = base64.b64decode(query_param)
print(query_param.hex())