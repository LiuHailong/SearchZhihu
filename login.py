#coding=utf-8
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
  
hosturl = "http://www.zhihu.com/question/34852948"
posturl = "http://www.zhihu.com/login/email"

cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
h = urllib2.urlopen(hosturl)  
  
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
        'Referer': 'http://www.zhihu.com/',
    }
postData = {
        'email': "787346616@qq.com", 
        'password': "ds931026",
        'rememberme': 'true',
    }
  
postData = urllib.urlencode(postData)  
  
request = urllib2.Request(posturl, postData, headers)  
# print request
response = urllib2.urlopen(request)  
text = response.read()  
print text