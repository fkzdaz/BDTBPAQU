# import urllib
# import urllib2
#
# url="https://mail.qq.com/"
# user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
# values={"username":"1247809987@qq.com","password":"qaz6553328"}
# #
# header={"User_Agent":user_agent,"Referer":"https://mail.qq.com/"}
# data=urllib.urlencode(values)
# request=urllib2.Request(url)
# response=urllib2.urlopen(request)
# print response.read()

#dailifuwuqishezhi
# import urllib2
# enable_proxy=True
# proxy_handler=urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler=urllib2.ProxyHandler({})
# if enable_proxy:
#     opener=urllib2.build_opener(proxy_handler)
# else:
#     opener=urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

# UrlError
# import urllib2
# request=urllib2.Request("http://www.jhdssdsdsd.com")
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError,e:
#     print e.reason

# HttpError
# import urllib2
# req=urllib2.Request("http://blog.csdn.net/cqcre")
# try:
#     resp=urllib2.urlopen(req)
#     print resp.read()
# except urllib2.HTTPError,e:
#     print e.code
#     print e.reason

# UrlError HttpError
# import urllib2
# req=urllib2.Request("http://www.baidu.com")
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError,e:
#     print e.code
#     print e.reason
# except urllib2.URLError,e:
#     print e.reason
# else:
#     print "ok"

# Cookie
# import urllib2
# import cookielib
# cookie=cookielib.CookieJar()
# handler=urllib2.HTTPCookieProcessor(cookie)
# opener=urllib2.build_opener(handler)
# response=opener.open("http://baidu.com")
# for i in cookie:
#     print "Name="+i.name
#     print "Value="+i.valus

# import urllib2
# import cookielib
# import urllib
#
# filename="cook.txt"
# cookie=cookielib.MozillaCookieJar(filename)
# handl=True)er=urllib2.HTTPCookieProcessor(cookie)
# opener=urllib2.build_opener(handler)
# resp=opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True,ignore_expires


# import urllib2
# import cookielib
#
# cooie=cookielib.MozillaCookieJar()
# cooie.load("cook.txt",ignore_expires=True,ignore_discard=True)
# req=urllib2.Request("http://www.baidu.com")
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cooie))
# res=opener.open(req)
# print res.read()


# import urllib
# import urllib2
# import cookielib
# filename="cookie.txt"
# cookie=cookielib.MozillaCookieJar(filename)
# handler=urllib2.HTTPCookieProcessor(cookie)
# opener=urllib2.build_opener(handler)
# postdata=urllib.urlencode({
#             'stuid':'201200131012',
#             'pwd':'23342321'})
# url="http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login"
#
# result=opener.open(urllib,postdata)
# cookie.save(ignore_discard=True,ignore_expires=True)
#
# grUrl="http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre"
# result=opener.open(grUrl)
# print result.read()

# import urllib
# import urllib2
# import re
# page=1
# url="http://www.qiushibaike.com/hot/page/"+str(page)
# user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
# headers={"User-Agent":user_agent}
# try:
#     req=urllib2.Request(url,headers=headers)
#     resp=urllib2.urlopen(req)
#     content= resp.read().decode("utf-8")
#     pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
#                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
#     items = re.findall(pattern, content)
#     for item in items:
#         haveImg = re.search("img", item[3])
#         if not haveImg:
#             print item[0], item[1], item[2], item[4]
# except urllib2.URLError,e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason
# -*- coding:utf-8 -*-
# import urllib2
# import urllib
# import re
#
# class Tool:
#     removeImg=re.compile('<img.*?>| {7}|')
#     removeAddr=re.compile('<a.*?>|</a>')
#     replaceLine=re.compile('<tr>|<div>|</div>|</p>')
#     replaceTD=re.compile('<td>')
#     replacePara=re.compile('<p.*?>')
#     replaceBR=re.compile('<br><br>|<br>')
#     removeExtraTag=re.compile('<.*?>')
#     def replace(self,x):
#         x=re.sub(self.removeImg,"",x)
#         x=re.sub(self.removeAddr,"",x)
#         x=re.sub(self.replaceLine,"/n",x)
#         x=re.sub(self.replaceTD,"\t",x)
#         x=re.sub(self.replacePara,"\n  ",x)
#         x=re.sub(self.replaceBR,"\n",x)
#         x=re.sub(self.removeExtraTag,"",x)
#         return x.strip()
#
# class BDTB:
#
#     def __init__(self,baseurl,seeLZ):
#         self.baseURL=baseurl
#         self.seeLZ="?see_lz="+str(seeLZ)
#
#     def getPage(self,pageNum):
#         try:
#             url=self.baseURL+self.seeLZ+"&pn="+str(pageNum)
#             req=urllib2.Request(url)
#             res=urllib2.urlopen(req)
#             print res.read()
#             return res
#         except urllib2.URLError,e:
#             if hasattr(e,"reason"):
#                 print "Can't do,becase ",e.reason
#                 return None
#
#     def getTitle(self):
#         page=self.getPage(1)
#         pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
#         result=re.search(pattern,page)
#         if result:
#             return result.group(1)
#         else:
#             return None
#
#     def getPageNum(self):
#         page=self.getPage(1)
#         pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
#         result=re.search(pattern,page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     def getContent(self,page):
#         pattern=re.compile('<div class="post_content.*?>(.*?)</div>',re.S)
#         items=re.findall(pattern,page)
#         print self.tool.replace(items[1])
#
# baseURL="http://tieba.baidu.com/p/3138733512"
# bdtb=BDTB(baseURL,1)
# bdtb.getContent(bdtb.getPage(1))
#
# -*- coding:utf-8 -*-
# import urllib
# import urllib2
# import re
#
#
# class Tool:
#
#     removeImg = re.compile('<img.*?>| {7}|')
#
#     removeAddr = re.compile('<a.*?>|</a>')
#
#     replaceLine = re.compile('<tr>|<div>|</div>|</p>')
#
#     replaceTD = re.compile('<td>')
#
#     replacePara = re.compile('<p.*?>')
#
#     replaceBR = re.compile('<br><br>|<br>')
#
#     removeExtraTag = re.compile('<.*?>')
#
#     def replace(self, x):
#         x = re.sub(self.removeImg, "", x)
#         x = re.sub(self.removeAddr, "", x)
#         x = re.sub(self.replaceLine, "\n", x)
#         x = re.sub(self.replaceTD, "\t", x)
#         x = re.sub(self.replacePara, "\n    ", x)
#         x = re.sub(self.replaceBR, "\n", x)
#         x = re.sub(self.removeExtraTag, "", x)
#         return x.strip()
#
# class BDTB:
#
#     def __init__(self, baseUrl, seeLZ):
#         self.baseURL = baseUrl
#         self.seeLZ = '?see_lz=' + str(seeLZ)
#         self.tool = Tool()
#
#     def getPage(self, pageNum):
#         try:
#             url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
#             request = urllib2.Request(url)
#             response = urllib2.urlopen(request)
#             return response.read().decode('utf-8')
#         except urllib2.URLError, e:
#             if hasattr(e, "reason"):
#                 print "error", e.reason
#                 return None
#
#
#     def getTitle(self):
#         page = self.getPage(1)
#         pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
#         result = re.search(pattern, page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     def getPageNum(self):
#         page = self.getPage(1)
#         pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
#         result = re.search(pattern, page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     def getContent(self, page):
#         pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
#         items = re.findall(pattern, page)
#         # for item in items:
#         #  print item
#         print self.tool.replace(items[1])
#
#
# baseURL = 'http://tieba.baidu.com/p/3138733512'
# bdtb = BDTB(baseURL, 1)
# bdtb.getContent(bdtb.getPage(1))

import urllib
import urllib2
import re

# class Tool:
#     removeImg=re.compile('<img.*?>| {7} |')
#     removeAddr=re.compile('<a.*?>|</a>')
#     replaceLine=re.compile('<tr>|<div>|</div><p>')
#     replaceTD=re.compile('<td>')
#     replacePara=re.compile('<p.*?>')
#     replaceBR=re.compile('<br><br>|<br>')
#     removeExtraTaf=re.compile('<.*?>')
#     def replace(self,x):
#         x=re.sub(self.removeImg,"",x)
#         x=re.sub(self.removeAddr,"",x)
#         x=re.sub(self.removeExtraTaf,"",x)
#         x=re.sub(self.replaceLine,"\n",x)
#         x=re.sub(self.replaceBR,"\n",x)
#         x=re.sub(self.replaceTD,"\n",x)
#         x=re.sub(self.replacePara,"\n  ",x)
#         return x.strip()
#
# class BDTB:
#
#     def __init__(self,baseUrl,seeLZ,floorTag):
#         self.baseURL=baseUrl
#         self.seeLZ='?see_lz='+str(seeLZ)
#         self.tool=Tool()
#         self.file=None
#         self.floor=1
#         self.defaultTitle="BDTB"
#         self.floorTag=floorTag
#
#     def getPage(self,pageNum):
#         try:
#             url=self.baseURL+self.seeLZ+"&pn="+str(pageNum)
#             req=urllib2.Request(url)
#             res=urllib2.urlopen(req)
#             return res.read().decode('utf-8')
#         except urllib2.URLError,e:
#             if hasattr(e,"reason"):
#                 print "Error",e.reason
#                 return None
#
#     def getTitle(self,page):
#         pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h1>',re.S)
#         result=re.search(pattern,page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     def getPageNum(self,page):
#         pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
#         result=re.search(pattern,page)
#         if result:
#             return result.group(1).strip()
#         else:
#             return None
#
#     def getContent(self,page):
#         pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
#         items=re.findall(pattern,page)
#         contents=[]
#         for item in items:
#             content="\n"+self.tool.replace(item)+"\n"
#             contents.append(content.encode("utf-8"))
#         return contents
#
#     def setFileTitle(self,title):
#         if title is not None:
#             self.title=open(title+".txt"+"w+")
#         else:
#             self.file=open(self.defaultTitle+".txt"+"w+")
#
#     def writeData(self,contents):
#         for item in contents:
#             if self.floorTag=="1":
#                 foolLine="\n"+str(self.tool)+"--------------------------------------------------\n"
#                 self.file.write(foolLine)
#             self.file.write(item)
#             self.floor+=1
#
#     def start(self):
#         indexPage=self.getPage(1)
#         pageNum=self.getPageNum(indexPage)
#         title=self.getTitle(indexPage)
#         self.setFileTitle(title)
#         if pageNum==None:
#             print "URL is not use"
#             return
#         try:
#             print "The tiezi have"+str(pageNum)+"page"
#             for i in range(1,int(pageNum)+1):
#                 print "aready write No"+str(i)+"page"
#                 page=self.getPage(1)
#                 content=self.getContent(page)
#                 self.writeData(content)
#
#         except IOError,e:
#             print "write is Error"+e.message
#         finally:
#             print "writing is success"
#
# print "please input the tiezi NO:"
# baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
# seeLZ=raw_input("if you only want to seeLZ please input 1,if not,input 0\n")
# foolrTag=raw_input("if you want to write foolrtag,please input 1,if not,input 0\n")
# bdtb=BDTB(baseURL,seeLZ,foolrTag)
# bdtb.start()



__author__ = 'FKZ'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


class Tool:

    removeImg = re.compile('<img.*?>| {7}|')

    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()



class BDTB:

    def __init__(self, baseUrl, seeLZ, floorTag):

        self.baseURL = baseUrl

        self.seeLZ = '?see_lz=' + str(seeLZ)

        self.tool = Tool()

        self.file = None

        self.floor = 1

        self.defaultTitle = "bdtb"

        self.floorTag = floorTag


    def getPage(self, pageNum):
        try:

            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)

            return response.read().decode('utf-8')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "Error", e.reason
                return None


    def getTitle(self, page):

        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern, page)
        if result:

            return result.group(1).strip()
        else:
            return None


    def getPageNum(self, page):

        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None


    def getContent(self, page):

        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:

            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):

        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeData(self, contents):

        for item in contents:
            if self.floorTag == '1':

                floorLine = "\n" + str(
                    self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL not user"
            return
        try:
            print "have" + str(pageNum) + "page"
            for i in range(1, int(pageNum) + 1):
                print "write" + str(i) + "page"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)

        except IOError, e:
            print "Error reason" + e.message
        finally:
            print "Success"


print "no"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("if you only want to seeLZ please input 1,if not,input 0\n")
floorTag = raw_input("if you want to write foolrtag,please input 1,if not,input 0\n")
bdtb = BDTB(baseURL, seeLZ, floorTag)
bdtb.start()