from selenium import webdriver
from OtherJobs.otherJob import OtherJobs
import os,sys,win32process,win32gui
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
    def locate_search(self,search_content):
        self.inter_other.input_value(search_content,'Everything',)




class WeiChat:
    pass

class KuGouMusic:
    pass

class LaJiQingLi:
    pass
