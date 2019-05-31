from selenium import webdriver
from OtherJobs.otherJob import OtherJobs
import os,sys,win32process,win32gui,time,win32con,collections,psutil
from win32api import *
from selenium.webdriver.chrome.options import Options
class BaiDuSearch:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.inter_other_baidu = OtherJobs()
        self.url = self.inter_other_baidu.Get_Config_Info('url_info','baidu_url')
    def baidu_search(self,contents):
        baidu_input = self.inter_other_baidu.Get_Config_Info('element_xpath','baidu_input')
        baidu_click = self.inter_other_baidu.Get_Config_Info('element_xpath','baidu_click')
        self.dr.get(self.url)
        self.dr.maximize_window()
        self.dr.find_element_by_id(baidu_input).send_keys(contents)
        self.dr.find_element_by_id(baidu_click).click()
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
        search_all_cmd = self.inter_other.Get_Config_Info('file_name','search_all_cmd')
        search_close_cmd = self.inter_other.Get_Config_Info('file_name','search_close_cmd')
        save_path_searchresult = self.inter_other.Get_Config_Info('file_name','save_path_searchresult')
        save_path_search_result_path = os.getcwd() + save_path_searchresult
        search_all = search_all_cmd + search_content
        os.system(search_all)
        time.sleep(0.3)
        num_list0 = [18,70]
        num_list1 = [17,69]
        self.inter_other.mouse_input_remote_on(num_list0)
        self.inter_other.mouse_input_remote_up(num_list0)
        self.inter_other.mouse_input_remote_on(num_list1)
        self.inter_other.mouse_input_remote_up(num_list1)
        save_Path = save_path_search_result_path + search_content + '.txt'
        try:
            self.inter_other.save_WinSearchFile(save_Path)
            time.sleep(0.5)
        except Exception as msg:
            print(msg)
        else:
            self.inter_other.print_File_Content(save_Path)
            time.sleep(3)
            os.system(search_close_cmd)
class WeiChat:
    def __init__(self):
        self.inter_other_wc = OtherJobs()
    def LoginWechat(self,num):
        wechat_path = self.inter_other_wc.Get_Config_Info('file_name','wechat_path')
        wChat_Conversation_window_class = self.inter_other_wc.Get_Config_Info('windows','wChat_Conversation_window_class')
        wChat_Login_window_class = self.inter_other_wc.Get_Config_Info('windows','wChat_Login_window_class')
        win32process.CreateProcess(wechat_path, '',None, None, 0, win32process.CREATE_NO_WINDOW, None, None,\
                                   win32process.STARTUPINFO())
        time.sleep(0.5)
        wChat_Conversation_hld = win32gui.FindWindow(wChat_Conversation_window_class,None)
        wChat_Login_hld = win32gui.FindWindow(wChat_Login_window_class,None)
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
        kugou_music_path = self.inter_other_kugou.Get_Config_Info('file_name','kugou_music_path')
        print(music_name)
        win32process.CreateProcess(kugou_music_path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None,None, \
                                   win32process.STARTUPINFO())
        self.inter_other_kugou.mouse_input_remote_on([18,116])
        self.inter_other_kugou.mouse_input_remote_up([18,116])
class LaJiQingLi:
    def __init__(self):
        self.inter_other_Garbage = OtherJobs()
    def Clear_All(self,value):
        qh360_grabage_path = self.inter_other_Garbage.Get_Config_Info('file_name', 'qh360_grabage_path')
        print(value)
        win32process.CreateProcess(qh360_grabage_path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, \
                                   win32process.STARTUPINFO())
class Mails_operate:
    def __init__(self):
        self.inter_other_mails = OtherJobs()
    def LoginEmail(self, mail_addr, user_name, user_passwd):
        get_frame_state_126 = self.inter_other_mails.Get_Config_Info('element_xpath', 'get_frame_state_126')
        get_login_state_126 = self.inter_other_mails.Get_Config_Info('element_xpath', 'get_login_state_126')
        input_login_username_126 = self.inter_other_mails.Get_Config_Info('element_xpath', 'input_login_username_126')
        input_login_password_126 = self.inter_other_mails.Get_Config_Info('element_xpath', 'input_login_password_126')
        click_login_button_126 = self.inter_other_mails.Get_Config_Info('element_xpath', 'click_login_button_126')
        click_login_confirm_126 = self.inter_other_mails.Get_Config_Info('element_xpath', 'click_login_confirm_126')
        get_frame_state_yeah = self.inter_other_mails.Get_Config_Info('element_xpath', 'get_frame_state_yeah')
        input_login_username_yeah = self.inter_other_mails.Get_Config_Info('element_xpath', 'input_login_username_yeah')
        input_login_password_yeah = self.inter_other_mails.Get_Config_Info('element_xpath', 'input_login_password_yeah')
        click_login_button_yeah = self.inter_other_mails.Get_Config_Info('element_xpath', 'click_login_button_yeah')
        get_frame_state_qq = self.inter_other_mails.Get_Config_Info('element_xpath', 'get_frame_state_qq')
        input_login_username_qq = self.inter_other_mails.Get_Config_Info('element_xpath', 'input_login_username_qq')
        input_login_password_qq = self.inter_other_mails.Get_Config_Info('element_xpath', 'input_login_password_qq')
        click_login_button_qq = self.inter_other_mails.Get_Config_Info('element_xpath', 'click_login_button_qq')
        if int(mail_addr) == 1:
            mail_yeah_url = self.inter_other_mails.Get_Config_Info('mails_info','yeah_mail_url')
            dr = webdriver.Chrome()
            dr.get(mail_yeah_url)
            dr.maximize_window()
            dr.find_element_by_xpath(get_login_state_126).click()
            elementi = dr.find_element_by_xpath(get_frame_state_126)
            dr.switch_to_frame(elementi)  # 切换frame
            dr.find_element_by_xpath(input_login_username_126).send_keys(user_name)
            dr.find_element_by_xpath(input_login_password_126).send_keys(user_passwd)
            dr.find_element_by_xpath(click_login_button_126).click()
            time.sleep(1)
            dr.find_element_by_xpath(click_login_confirm_126).click()
            time.sleep(600)
            dr.close()
        if int(mail_addr) == 2:
            mail_yeah_url = self.inter_other_mails.Get_Config_Info('mails_info', '126_mail_url')
            dr = webdriver.Chrome()
            dr.get(mail_yeah_url)
            dr.maximize_window()
            elementi = dr.find_element_by_xpath(get_frame_state_yeah)
            dr.switch_to_frame(elementi)  # 切换frame
            dr.find_element_by_xpath(input_login_username_yeah).send_keys(user_name)
            dr.find_element_by_xpath(input_login_password_yeah).send_keys(user_passwd)
            dr.find_element_by_xpath(click_login_button_yeah).click()
            time.sleep(600)
            dr.close()
        if int(mail_addr) == 3:
            mail_yeah_url = self.inter_other_mails.Get_Config_Info('mails_info', 'qq_mail_url')
            dr = webdriver.Chrome()
            dr.get(mail_yeah_url)
            dr.maximize_window()
            elementi = dr.find_element_by_xpath(get_frame_state_qq)
            dr.switch_to_frame(elementi)  # 切换frame
            dr.find_element_by_xpath(input_login_username_qq).send_keys(user_name)
            dr.find_element_by_xpath(input_login_password_qq).send_keys(user_passwd)
            dr.find_element_by_xpath(click_login_button_qq).click()
            time.sleep(600)
            dr.close()

class Resource_Monitor:
    def __init__(self):
        self.resource_monitor = OtherJobs()
    def GetCpan(self):
        disk_used = collections.OrderedDict()
        for id in psutil.disk_partitions():
            if 'cdrom' in id.opts or id.fstype == '':
                continue
            disk_name = id.device.split(':')
            s = disk_name[0]
            disk_info = psutil.disk_usage(id.device)
            disk_used[s + '盘使用率：'] = '{}%'.format(disk_info.percent)
            disk_used[s + '剩余空间：'] = '{}GB'.format(disk_info.free // 1024 // 1024 // 1024)
        # print(self.disk_used)
        return disk_used

    def GetCpu(self):
        cpu_times = psutil.cpu_times()
        cpu_info = {'用户': 0, '系统': 0, '闲置': 0, '使用率': 0}
        cpu_info['用户'] = cpu_times.user
        cpu_info['系统'] = cpu_times.system
        cpu_info['闲置'] = cpu_times.idle
        cpu_info['使用率'] = '{}%'.format(psutil.cpu_percent(interval=2))
        print(cpu_info)
        return cpu_info

    def GetMemory(self):
        mem_info = psutil.virtual_memory()
        memory_info = {'总共': 0, '可用': 0, '使用率': 0, '使用': 0, '空闲': 0}
        memory_info['总共'] = '{}MB'.format(mem_info.total // 1024 // 1024)
        memory_info['可用'] = '{}MB'.format(mem_info.available // 1024 // 1024)
        memory_info['使用率'] = '{}%'.format(mem_info.percent)
        memory_info['使用'] = '{}MB'.format(mem_info.used // 1024 // 1024)
        memory_info['空闲'] = '{}MB'.format(mem_info.free // 1024 // 1024)
        print(memory_info)
        return memory_info

    def Monitor(self):
        while True:
            diskcost = self.GetCpan()
            cpucost = self.GetCpu()
            memorycost = self.GetCpu()
            alert = []
            for key, value in diskcost.items():
                if "%" in value:
                    # print(value)
                    disk_used_value = value.split('%')[0]
                    if float(disk_used_value) > 80:
                        print(disk_used_value)
                        alert.append(key + ' ' + value)
            self.resource_monitor.SendMail(alert, diskcost)
            if float(str(cpucost['使用率']).split('%')[0]) > 70:
                cpu_alert = 'CPU使用率：' + cpucost['使用率']
                print(cpu_alert)
                self.resource_monitor.SendMail(cpu_alert, cpucost)
            if float(str(memorycost['使用率']).split('%')[0]) > 70:
                mem_alert = '内存使用率：' + memorycost['使用率']
                print(mem_alert)
                self.resource_monitor.SendMail(mem_alert, memorycost)
            time.sleep(3600)
    def Get_Unreadmails_Num(self):
        cookies_file_path = self.resource_monitor.Get_Config_Info('file_name', 'save_cookies_path')  #
        cookies_file_path_all = os.path.dirname(os.path.dirname(__file__))+ cookies_file_path
        print(cookies_file_path_all)
        yeah_url = self.resource_monitor.Get_Config_Info('mails_info', 'yeah_mail_url')  #
        element_xpath_get_unread_num = self.resource_monitor.Get_Config_Info('element_xpath', 'unread_mails_yeah')  #
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        dr = webdriver.Chrome(chrome_options=chrome_options)
        self.resource_monitor.Save_Cookies(cookies_file_path_all, yeah_url)
        # dr = webdriver.Chrome()
        dr.get(yeah_url)
        dr.maximize_window()
        try:
            self.resource_monitor.Read_Cookies(dr, cookies_file_path_all)
        except Exception as msg:
            print(msg)
            cookies_noused = self.resource_monitor.Get_Config_Info('tips','cookies_noused')
            print(cookies_noused)
            os.remove(cookies_file_path_all)
            self.Get_Unreadmails_Num()
        else:
            time.sleep(0.5)
            unread_mails_num = dr.find_element_by_xpath(element_xpath_get_unread_num).text
            time.sleep(2)
            dr.close()
        unread_mails_num_show = '未读邮件：' + unread_mails_num + '条。'
        return unread_mails_num_show