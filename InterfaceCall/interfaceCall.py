from selenium import webdriver
from OtherJobs.otherJob import OtherJobs
import os,sys,win32process,win32gui,time,win32api,win32con
from pywinauto import application
from pykeyboard import *
from pymouse import *
#import SendKeys
class BaiDuSearch:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.url = 'https://www.baidu.com/'
    def baidu_search(self,contents):
        self.dr.get(self.url)
        self.dr.find_element_by_id('kw').send_keys(contents)
        self.dr.find_element_by_id('su').click()
class NewFiles:
    def open_file(self,filepanth):
        if os.path.exists(filepanth):
            pass
        else:
            with open(filepanth,'w') as f:
                f.close()
        os.system(filepanth)
class LocateSearch:
    def __init__(self):
        self.inter_other = OtherJobs()
        self.app = application.Application()
    def locate_search(self,search_content):
        #self.app.start('E:\\softinstall\\Everything\\Everything.exe')
        search_all = 'E:\\softinstall\\Everything\\Everything.exe -search ' + search_content
        search_close = 'E:\\softinstall\\Everything\\Everything.exe -close'
        os.system(search_all)
        num_list0 = [18,70]
        num_list1 = [17,69]
        self.inter_other.mouse_input_remote_on(num_list0)
        self.inter_other.mouse_input_remote_up(num_list0)
        self.inter_other.mouse_input_remote_on(num_list1)
        self.inter_other.mouse_input_remote_up(num_list1)
        self.inter_other.save_winfile()

        time.sleep(5)
        #os.system(search_close)





class WeiChat:
    pass

class KuGouMusic:
    pass

class LaJiQingLi:
    pass
