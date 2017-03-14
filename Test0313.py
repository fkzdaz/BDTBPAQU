# from urllib2 import Request,URLError,HTTPError,urlopen
#
# old_url='http://www.baidu.com'
# req=Request(old_url)
# response=urlopen(req)
# print "old_url"+old_url
# print "new_url"+response.geturl()
# import urllib2
# request=urllib2.Request("http://www.baidu.com")
# response=urllib2.urlopen(request)
# print response.read()
# import urllib2
# import urllib
#
# values={"username":"1247809987@qq.com","password":"qaz6553328"}
# data=urllib.urlencode(values)
# url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request=urllib2.Request(url)
# response=urllib2.urlopen(request)
# print response.read()
# import urllib2
# import urllib
# values={}
# values["username"]="1247809987@qq.com"
# values["password"]="qaz6553328"
# data=urllib.urlencode(values)
# url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request=urllib2.Request(url)
# response=urllib2.urlopen(request)
# print response.read()

import urllib2
import urllib
values={}
values["username"]="1247809987@qq.com"
values["password"]="qaz655328"
data=urllib.urlencode(values)
url="http://passport.csdn.net/account/login"
geturl=url+"?"+data
request=urllib2.Request(geturl)
response=urllib2.urlopen(request)
print response.read()

