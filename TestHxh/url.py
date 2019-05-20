import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://detail.zol.com.cn/notebook_index/subcate16_list_s857_1.html')
for line in fhand:
    print(line.decode().strip())
