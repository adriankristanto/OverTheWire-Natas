import requests
import bs4
import re


# configuration for natas19
USERNAME = 'natas19'
PASSWORD = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
URL = 'http://natas19.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# as the webpage said, the code used is the same as the previous level
# however, the session ids are not sequential
# let's see what this means
data = {
    'username' : 'randomusername',
    'password' : 'randompassword',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
# example id: PHPSESSID=3433302d72616e646f6d757365726e616d65
print(f'{response.cookies}\n')