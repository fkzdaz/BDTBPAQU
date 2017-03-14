# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 23:28:25 2017

@author: fkz
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import cookielib
import os

class GdcpSpider:
    def __init__(self):
        self.baseURL = ""
        self.enable = True
        self.charaterset = "gb2312"
        string = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        self.headers = {'User-Agent' : string}
        self.cookie = cookielib.CookieJar()
        self.hander = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.hander)


    def getCheckCode(self):

        checkcode_url = "http://jw2012.gdcp.cn/CheckCode.aspx"
        request = urllib2.Request(checkcode_url, headers=self.headers)
        picture = self.opener.open(request).read()

        local = open("checkcode.jpg", "wb")
        local.write(picture)
        local.close()

        os.system("checkcode.jpg")

        TextBox3 = raw_input(str("Please input checkcode ").encode(self.charaterset))
        return TextBox3


    def login(self, TextBox1, TextBox2):
        TextBox3 = self.getCheckCode()
        postData = {"TextBox1":TextBox1, "TextBox2":TextBox2, "TextBox3":TextBox3}
        data = urllib.urlencode(postData)
        request_url = "http://jw2012.gdcp.cn/default2.aspx"
        request_new = urllib2.Request(request_url, headers=self.headers)
        response = self.opener.open(request_new, data)


# # 抓取网页
#     def getHtml(self, url):
#         try:
#             request_score = urllib2.Request(url, headers=self.headers)
#             response_score = self.opener.open(request_score)
#             return response_score.read().decode("gb2312", 'ignore').encode("utf8")
#         except urllib2.URLError, e:
#             if hasattr(e, "reason"):
#                 string = "lose" + str(e.reason)
#                 print string.encode(self.charaterset)
#                 return None


if "__main__" == __name__:
    TextBox1 = "1213157213"
    TextBox2 = "445224199408052410"
    gdcp = GdcpSpider()
    gdcp.login(TextBox1, TextBox2)
    print "login success！！！"



