import requests
import bs4
import re
import html
import base64


# configuration for natas8
USERNAME = 'natas8'
PASSWORD = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
URL = 'http://natas8.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
# </div> has an id element, which is invalid, thus, we can't find it with html.parser
soup = bs4.BeautifulSoup(source, 'lxml')
div_content = soup.body.find('div')
print(f'{div_content.prettify()}\n')


# in the source code, we found the following
"""
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
function encodeSecret($secret) {    
    return bin2hex(strrev(base64_encode($secret)));
}
"""
# the encodeSecret() function will be used on our input & the output will be compared
# with the variable encodedSecret
# therefore, firstly, reverse from hex to binary
# next, we should reverse the binary
# finally, we should decode the reversed binary
