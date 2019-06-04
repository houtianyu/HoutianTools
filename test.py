# coding: utf-8
from selenium import webdriver
# -*- coding: utf-8 -*-
#采集SERP搜索结果标题
from bs4 import BeautifulSoup
from OtherJobs.otherJob import OtherJobs
import time,urllib.request,random,sys,importlib
from urllib.parse import quote
import urllib,os,win32api,win32process,inspect
import string
#获取Html源码
class Getresult:
    def __init__(self):
        self.ss = OtherJobs()
    def search_file(self):
        self.ss.Init_Exe_Path()

if __name__ == "__main__":
    a = Getresult()
    start = time.time()
    a.search_file()
    c = time.time() - start
    print(c)
