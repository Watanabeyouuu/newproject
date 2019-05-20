import urllib.request, urllib.parse, urllib.error
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url =https://m.weibo.cn/api/container/getIndex?type=uid&value=1665372775&containerid=1076031665372775&page=2?


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode() #得到数据并解码
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
print(js)
