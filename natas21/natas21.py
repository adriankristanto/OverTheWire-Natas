import requests
import bs4
import re


# configuration for natas21
USERNAME = 'natas21'
PASSWORD = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
URL = 'http://natas21.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
# response = session.get(URL + 'index-source.html')
# print(response.text)


# get the second site
SECOND_URL = re.search(r'href="(.+)"', str(div_content))[1] + '/'
response = session.get(SECOND_URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code for the second site
# response = session.get(SECOND_URL + 'index-source.html')
# print(response.text)


# since there is nothing interesting in the source code of the first webpage,
# we can safely skip it and go to the second website immediately
# in the second website, there is the following lines of code
"""

// if update was submitted, store it
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}
"""
# which will store any parameters that we submit to the webpage, including the admin parameter
# this is the main vulnerability.
# therefore, we can ignore the rest of the code that performs the validation