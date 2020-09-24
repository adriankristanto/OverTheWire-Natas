import requests
import bs4
import re


# configuration for natas26
USERNAME = 'natas26'
PASSWORD = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas26.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)


# firstly, let's try to use the feature provided by the web server, 
# which is drawing a straight line
params = {
    'x1' : 50,
    'y1' : 50,
    'x2' : 100,
    'y2' : 100
}
response = session.get(URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# next, we can find the image we requested in the following link
# img/natas26_<PHPSESSID>.png, which we can try and access
img_link = re.search(r'img src="(img/natas26_\w+\.png)"', str(div_content))[1]
response = session.get(URL + '/' + img_link)
print(response)
# therefore, we can assume that we have the permission to access the content of the img directory