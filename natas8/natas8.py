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
# therefore, firstly, we need decode the secret from its hex representation
# next, we should reverse the secret
# finally, we should base64 decode the reversed binary
encodedSecret = "3d3d516343746d4d6d6c315669563362"
ascii_encodedSecret = bytes.fromhex(encodedSecret).decode()[::-1]
decodedSecret = base64.b64decode(ascii_encodedSecret).decode()
print(f'{decodedSecret}\n')


# submit the secret
data = {
    'secret' : decodedSecret,
    'submit' : 'submit'
}
response = session.post(URL, data=data) 
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# natas9 password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
password = re.search(r'is (\w+)\n', str(div_content)).group(1)
print(f'natas9 password: {password}')
