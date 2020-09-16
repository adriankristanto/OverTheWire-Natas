import requests
import bs4
import re
import html


# configuration for natas25
USERNAME = 'natas25'
PASSWORD = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
URL = 'http://natas25.natas.labs.overthewire.org/'


session = requests.Session()
session.auth = AUTH
# get the challenge content
response = session.get(URL)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get the source code
response = session.get(URL + 'index-source.html')
# print(html.unescape(response.text).replace('<br />', ''))


# first part
"""
function setLanguage(){
    /* language setup */
    if(array_key_exists("lang",$_REQUEST))
        if(safeinclude("language/" . $_REQUEST["lang"] ))
            return 1;
    safeinclude("language/en"); 
}

function safeinclude($filename){
    // check for directory traversal
    if(strstr($filename,"../")){
        logRequest("Directory traversal attempt! fixing request.");
        $filename=str_replace("../","",$filename);
    }
    // dont let ppl steal our passwords
    if(strstr($filename,"natas_webpass")){
        logRequest("Illegal file access detected! Aborting!");
        exit(-1);
    }
    // add more checks...

    if (file_exists($filename)) { 
        include($filename);
        return 1;
    }
    return 0;
}
"""
# in the source code, there is a safeinclude()
# which give us a hint of the type of the vulnerability
# which is directory traversal because of insufficient
# user input sanitisation
# for example, in this case, we can perform "unsafe string replacement attack"
# reference: https://nets.ec/Unsafe_string_replacement
# since the server will replace every occurence of ../ with "",
# with the input "....//", we can bypass the input sanitisation
# so, when "../" is removed from "....//", we stilll get "../"
# which still allow for directory traversal


# since we know the location of the log files based on the source code,
# we can try to read the log files with the help of the directory traversal
# attack