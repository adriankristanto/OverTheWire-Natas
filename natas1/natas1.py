import requests
import bs4
import re


# configuration for natas1
USERNAME = "natas1"
PASSWORD = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"
URL = "http://natas1.natas.labs.overthewire.org"
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


response = requests.get(url=URL, auth=AUTH)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
body = soup.find('body')
div_content = body.find('div', {'id': 'content'})
print(f'{div_content}\n')
comment = div_content.find(text=lambda line: isinstance(line, bs4.Comment))


# natas2 password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
password = re.search(r'is (\w+) ', comment).group(1)
print(f"natas2 password: {password}")