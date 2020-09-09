import requests
import bs4
import re
import html


# configuration for natas23
USERNAME = 'natas23'
PASSWORD = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas23.natas.labs.overthewire.org/'


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
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
"""
# firstly, once we made a requests with passwd as one of the params,
# we need to include "iloveyou" string in the passwd as 
# the strstr() function will return everything up to the needle
# if the string doesn't exist, it will return False
# reference: https://www.php.net/manual/en/function.strstr.php
# next, it will compare the string that we submitted with the integer 10
# if the string is greater than 10, it will return True and we will get the admin page