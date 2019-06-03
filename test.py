from selenium import webdriver
# -*- coding: utf-8 -*-
#采集SERP搜索结果标题
from bs4 import BeautifulSoup
import time,urllib.request,random,sys,importlib
from urllib.parse import quote
import urllib
import string
#获取Html源码
class Getresult:
    def __init__(self):
        self.user_agents = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8'
            }
    def GetHtml(self,url):
        req = urllib.request.Request(url,None,headers=self.user_agents)
        response = urllib.request.urlopen(req,None,30)#设置超时时间
        try:
            html = response.read().decode('utf-8')
        except Exception as msg:
            print(msg)
            #raise msg
        else:
            #提取搜索结果SERP的标题
            soup = BeautifulSoup(''.join(html))
            for i in soup.findAll("h3"):
                title = i.text
                #print(title)
                if '百度' in title:
                    try:
                        title = title.split('\n')[1]
                    except Exception as msg:
                        #print(msg)
                        pass
                    print(title)
                else:
                    print(title)
if __name__ == "__main__":
    a = Getresult()
    global keyword
    keyword = "测试软件"
    start = time.time()
    for i in range(0,2):
        url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(keyword) + '&pn=' + str(i*100)
        #url1 = quote(url, safe=string.printable)
        html = a.GetHtml(url)
    c = time.time() - start
    print('程序运行耗时:%0.2f 秒'%(c))