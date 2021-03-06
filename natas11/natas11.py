import requests
import bs4
import re
import base64
import html
import json


# configuration for natas11
USERNAME = 'natas11'
PASSWORD = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
URL = 'http://natas11.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
body = bs4.BeautifulSoup(response.text, 'html.parser').body
print(f'{body}\n')


response = session.get(URL  + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
body = bs4.BeautifulSoup(source, 'lxml').body
print(f'{body.prettify()}\n')


# the source code has a default data, which is a PHP array that contains
# showpassword key with value no
# and bgcolor key with value #ffffff
# $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

# next, it loads and save the data, let's see the function implementation
# $data = loadData($defaultdata);
# saveData($data);
"""
# the following is a simple xor function
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    # mydata variable defaults to the aforementioned array
    $mydata = $def;
    # next, we check whether there exists a cookie with key data
    if(array_key_exists("data", $_COOKIE)) {
    # if it doesn, then we decode the data > xor encrypt/decrypt > json decode
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    # if the value of coookie 'data' is an array and it contaisn showpassword and bgcolor keys, then
    # set mydata variable to what was set by the user
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
"""
# therefore, firstly, we would need to create the default data & json encode it
default = {
    'showpassword' : 'no',
    'bgcolor' : '#ffffff'
}
# reference: https://stackoverflow.com/questions/16311562/python-json-without-whitespaces
# when json encode the dictionary, remove the whitespaces added by json.dumps()
# as the whitespaces can affect the xor encryption result
default = json.dumps(default, separators=(',',':'))
# next, get the cookie 'data' from the server & base64 decode it
data_cookie = requests.utils.unquote(session.cookies['data'])
data_cookie = base64.b64decode(data_cookie)
# then, xor the our json encoded data and the base64 decoded data from the server to get the xor encryption key
def xor(plaintext1, plaintext2):
    result = ''
    for index in range(len(plaintext1)):
        result += chr(plaintext1[index] ^ plaintext2[index])
    return result

key = xor(data_cookie, bytearray(default, 'utf-8'))[:4]
# the key is qw8J
print(f'{key}\n')


# finally, we create the data that we want, json encode it, xor encrypt with the recovered key and finally, base64 encode it
data = {
    'showpassword' : 'yes',
    'bgcolor' : '#fffffa'
}
data = json.dumps(data)
# repeat the key len(data) // len(key) times
# then, add the remainder if len(key1) != len(data)
key1 = key * (len(data)//len(key)) + key[:len(data) % len(key)]
data = xor(bytearray(data, 'utf-8'), bytearray(key1, 'utf-8'))
data = base64.b64encode(bytearray(data, 'utf-8'))
data = requests.utils.quote(data)
# and send it as a cookie 'data' to the server
requests.utils.add_dict_to_cookiejar(session.cookies, {'data' : data})
response = session.get(URL)
body = bs4.BeautifulSoup(response.text, 'html.parser').body
print(f'{body}\n')
# this should allow us to get the password of the next level


# natas12 password: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
password = re.search(r'is (\w+)', str(body)).group(1)
print(f'natas12 password: {password}')