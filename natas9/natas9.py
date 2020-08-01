import requests
import bs4
import re
import html


# configuration for natas9
USERNAME = 'natas9'
PASSWORD = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
URL = 'http://natas9.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
div = bs4.BeautifulSoup(source, 'lxml').body.find('div')
print(div)


"""
$key = "";
if(array_key_exists("needle", $_REQUEST)) {    
    $key = $_REQUEST["needle"];
    }
if($key != "") {    
    passthru("grep -i $key dictionary.txt");
}?&gt;
"""
# one attack that we can try here is OS command injection or shell injection
# this is because there is no user input sanitisation
# the input is passed as is to the 'grep -i command'