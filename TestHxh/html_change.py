# -*- coding:utf-8 -*-
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1:请求
url = 'http://seputu.com/'
html = urllib.request.urlopen(url, context=ctx)

# soup = BeautifulSoup(html, 'html.parser') # 不用encode decode soup即为html最终结果
# print (soup)

#
data = html.read().decode() #得到数据并解码
js = json.loads(data)
print(data)
