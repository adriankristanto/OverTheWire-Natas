import requests
import bs4
import re


# configuration for natas18
USERNAME = 'natas18'
PASSWORD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
URL = 'http://natas18.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)


"""
In the source code, there's a global variable called $maxid=640.
Also, each user is assigned a numerical id between 1 and 640 (inclusive)
(reference: https://www.php.net/manual/en/function.rand.php)
using the createID() function.
This user id is then assigned to the cookie PHPSESSID.
It seems that the admin has one of the ids, but we don't know which one yet.
For example,
"""
data = {
    'username' : 'randomusername',
    'password' : 'randompassword',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
# prints out any number between 1 and 640 for PHPSESSID
print(f'Cookies: {response.cookies}\n')