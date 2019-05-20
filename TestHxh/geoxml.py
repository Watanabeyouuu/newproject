import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_214387.xml'

uh = urllib.request.urlopen(url)
data = uh.read().decode()

tree = ET.fromstring(data)
#print(type(tree)) #<class 'xml.etree.ElementTree.Element'>

counts = tree.findall('.//count')
#print(counts) #counts is a list

res = 0
for count in counts:
    num = count.text
    res = res + int(num)

print(res)
