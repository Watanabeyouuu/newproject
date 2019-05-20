import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_214387.xml'
html = urllib.request.urlopen(url, context=ctx).read()

temp = list()
commentinfo = ET.fromstring(html)
lst = commentinfo.findall('comments/comment')


for item in lst:
    num = item.find('count').text
    num = int(num)
#    sum = sum + num
    temp.append(num)
#print(temp)
a = sum(temp)

print(a)
