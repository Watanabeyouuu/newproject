import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
count = 0
ass = list()
tags = soup('span')
for tag in tags:
    # ass = tag.contents[0]

    ass.append(tag.contents[0])

for num in ass:
    num = int(num)
    sum = sum + num
    count = count + 1
print('Count', count)
print('Sum', sum)
