import requests
import re
import bs4


# configuration for natas0
USERNAME = "natas0"
PASSWORD = "natas0"
URL = 'http://natas0.natas.labs.overthewire.org'
# for simple http authentication
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


# get the page source
response = requests.get(url=URL, auth=AUTH)
# pass the page source to BeautifulSoup
soup = bs4.BeautifulSoup(response.text, 'html.parser')


# the header doesn't seem relevant to the challenge as stated by the following comment
# <!-- This stuff in the header has nothing to do with the level -->
body = soup.find('body')
# the comment is contained within the div with id=content
div_content = body.find('div', {'id': 'content'})
# create a lambda function to get the comment containing the password
# within the body element
# reference: https://stackoverflow.com/questions/33138937/how-to-find-all-comments-with-beautiful-soup
comment = div_content.find(text=lambda line: isinstance(line, bs4.Comment))


# natas1 password: gtVrDuiDfck831PqWsLEZy5gyDz1clto
password = re.findall(r'is (.*) ', comment)[0]
print(f"natas1 password: {password}")