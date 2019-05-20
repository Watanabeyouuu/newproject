import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_214388.json'
sum = 0
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print(data[:600])
info = json.loads(data)

info = info['comments']
print(info)
for item in info:
    num = item['count']
    sum = sum + num
print(sum)
#print(res)
