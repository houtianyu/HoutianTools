from selenium import webdriver
from OtherJobs.otherJob import OtherJobs
import os,sys,win32process,win32gui,time,win32con
from win32api import *
class BaiDuSearch:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.url = 'https://www.baidu.com/'
    def baidu_search(self,contents):
        self.dr.get(self.url)
        self.dr.maximize_window()
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
        search_all = 'E:\\softinstall\\Everything\\Everything.exe -search ' + search_content
        search_close = 'E:\\softinstall\\Everything\\Everything.exe -close'
        os.system(search_all)
        time.sleep(0.3)
        num_list0 = [18,70]
        num_list1 = [17,69]
        self.inter_other.mouse_input_remote_on(num_list0)
        self.inter_other.mouse_input_remote_up(num_list0)
        self.inter_other.mouse_input_remote_on(num_list1)
        self.inter_other.mouse_input_remote_up(num_list1)
        save_Path = 'D:\Python\HoutianTools\Files' + '\\' + search_content + '.txt'
        try:
            self.inter_other.save_WinSearchFile(save_Path)
            time.sleep(0.5)
        except Exception as msg:
            print(msg)
        else:
            self.inter_other.print_File_Content(save_Path)
            time.sleep(3)
            os.system(search_close)
class WeiChat:
    def __init__(self):
        self.inter_other_wc = OtherJobs()
    def LoginWechat(self,num):
        win32process.CreateProcess('E:\\软件\\WeChat\\WeChat.exe', '',None, None, 0, win32process.CREATE_NO_WINDOW, None, None,\
                                   win32process.STARTUPINFO())
        time.sleep(0.5)
        wChat_Conversation_hld = win32gui.FindWindow('uWeChatMainWndForPC',None)
        wChat_Login_hld = win32gui.FindWindow('WeChatLoginWndForPC',None)
        if wChat_Conversation_hld:
            pass
        if wChat_Login_hld:
            #handleDetail = win32gui.GetWindowRect(wChat_Login_hld)
            if int(num) == 0:
                self.inter_other_wc.mouse_click_order(660, 485)
            else:
                self.inter_other_wc.mouse_click_order(680, 410)
class KuGouMusic:
    def __init__(self):
        self.inter_other_kugou = OtherJobs()
    def play_Music_Name(self,music_name):
        print(music_name)
        win32process.CreateProcess('E:\KGMusic\KuGou.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None,None, \
                                   win32process.STARTUPINFO())
        self.inter_other_kugou.mouse_input_remote_on([18,116])
        self.inter_other_kugou.mouse_input_remote_up([18,116])
class LaJiQingLi:
    def __init__(self):
        self.inter_other_Garbage = OtherJobs()
    def Clear_All(self,value):
        print(value)
        win32process.CreateProcess('E:\\软件\\360\\360Safe\\360Safe.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, \
                                   win32process.STARTUPINFO())