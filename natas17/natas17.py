import requests
import bs4
import re


# configuration for natas17
USERNAME = 'natas17'
PASSWORD = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
URL = 'http://natas17.natas.labs.overthewire.org/'
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


# as we can see in the source, the feedback to the user is now commented out
"""
if(mysql_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }
"""
# one attack that we can try is time-based SQL injection attack
# the idea is that if the user exists, then the website will return its response 
# after X seconds
# otherwise, the website will response immediately