# coding:utf8
import urllib2
import cookielib
url = "https://www.baidu.com"

print '第1种方法'
res1  = urllib2.urlopen(url)
print res1.getcode()
print len(res1.read())

print '第2种方法'
req = urllib2.Request(url)
# 伪装成Mozilla浏览器
req.add_header("user-agent", "Mozilla/5.0")
res2  = urllib2.urlopen(req)
print res2.getcode()
print len(res2.read())

print '第3种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
res3 = urllib2.urlopen(url)
print res3.getcode()
print cj
print res3.read()