# coding: utf-8
from selenium import webdriver
from OtherJobs.otherJob import *
from Logs.logs import Logs
import os,sys,win32process,win32gui,time,win32con,collections,psutil
from win32api import *
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time,urllib.request,random,sys,importlib
from urllib.parse import quote
import urllib,subprocess
class BaiDuSearch:
    def __init__(self):
        self.inter_other_baidu = OtherJobs()
        self.other_job_log_baidu = Logs()
    def baidu_search(self,contents):
        if not contents:
            tips_baidu = '未输入百度搜索内容。'
            self.inter_other_baidu.Resource_show(tips_baidu)
            self.other_job_log_baidu.LogsSave(tips_baidu)
        else:
            dr = webdriver.Chrome()
            self.url = self.inter_other_baidu.Get_Config_Info('url_info', 'baidu_url')
            baidu_input = self.inter_other_baidu.Get_Config_Info('element_xpath','baidu_input')
            baidu_click = self.inter_other_baidu.Get_Config_Info('element_xpath','baidu_click')
            try:
                dr.get(self.url)
                dr.maximize_window()
                dr.find_element_by_id(baidu_input).send_keys(contents)
                dr.find_element_by_id(baidu_click).click()
            except Exception as msg:
                print(msg)
                self.other_job_log_baidu.LogsSave(msg)
                tips_baidu_err = '打开百度搜索失败。'
                print(tips_baidu_err)
                self.other_job_log_baidu.LogsSave(tips_baidu_err)
    def open_websuit_com(self,num):
        try:
            if int(num) == 1:
                pass
        except Exception as msg:
            open_websute_err = '请选择需要打开的网站！'
            print(msg)
            print(open_websute_err)
            self.inter_other_baidu.Resource_show(open_websute_err)
            self.other_job_log_baidu.LogsSave(msg)
            self.other_job_log_baidu.LogsSave(msg)
        else:
            houtian_blog = self.inter_other_baidu.Get_Config_Info('url_info','houtian_blog')
            bilibili=self.inter_other_baidu.Get_Config_Info('url_info','bilibili')
            jinxuexiaofang = self.inter_other_baidu.Get_Config_Info('url_info', 'jinxuexiaofang')
            mokecom = self.inter_other_baidu.Get_Config_Info('url_info', 'mokecom')
            github = self.inter_other_baidu.Get_Config_Info('url_info', 'github')
            baidufanyi = self.inter_other_baidu.Get_Config_Info('url_info', 'baidufanyi')
            dr = webdriver.Chrome()
            dr.maximize_window()
            if int(num) == 1:
                tips_houtian_blog = '正在打开后天博客网站！'
                self.inter_other_baidu.Resource_show(tips_houtian_blog)
                self.other_job_log_baidu.LogsSave(tips_houtian_blog)
                dr.get(houtian_blog)
            elif int(num) == 2:
                tips_bilibili = '正在打开哔哩哔哩网站！'
                self.inter_other_baidu.Resource_show(tips_bilibili)
                self.other_job_log_baidu.LogsSave(tips_bilibili)
                dr.get(bilibili)
            elif int(num) == 3:
                tips_jinxuexiaofang = '正在打开简学消防网站！'
                self.inter_other_baidu.Resource_show(tips_jinxuexiaofang)
                self.other_job_log_baidu.LogsSave(tips_jinxuexiaofang)
                dr.get(jinxuexiaofang)
            elif int(num) == 4:
                tips_mokecom = '正在打开慕课网站！'
                self.inter_other_baidu.Resource_show(tips_mokecom)
                self.other_job_log_baidu.LogsSave(tips_mokecom)
                dr.get(mokecom)
            elif int(num) == 5:
                tips_github = '正在打开github网站！'
                self.inter_other_baidu.Resource_show(tips_github)
                self.other_job_log_baidu.LogsSave(tips_github)
                dr.get(github)
            elif int(num) == 6:
                tips_baidufanyi = '正在打开github网站！'
                self.inter_other_baidu.Resource_show(tips_baidufanyi)
                self.other_job_log_baidu.LogsSave(tips_baidufanyi)
                dr.get(baidufanyi)
    def baidu_search_title_auto(self,contents):
        if not contents:
            tips_baidu = '未输入百度搜索内容。'
            self.inter_other_baidu.Resource_show(tips_baidu)
            self.other_job_log_baidu.LogsSave(tips_baidu)
        user_agents_baidu_search_auto = self.inter_other_baidu.Get_Config_Info('other_info','user_agents_baidu_search_auto')
        #user_agents_baidu_search_auto = dict(user_agents_baidu_search_auto)
        url_baidu_search_auto = self.inter_other_baidu.Get_Config_Info('url_info','url_baidu_search_auto')
        for i in range(2):
            url_baidu_search__auto_format = url_baidu_search_auto + urllib.parse.quote(contents) + '&pn=' + str(i*100)
            req = urllib.request.Request(url_baidu_search__auto_format)#,None,headers=user_agents_baidu_search_auto
            response = urllib.request.urlopen(req, None, 30)  # 设置超时时间
            try:
                html = response.read().decode('utf-8')
            except Exception as msg:
                print('获取失败,请重试！ %s'% msg)
                self.inter_other_baidu.Resource_show('获取失败,请重试！ %s'% msg)
                self.other_job_log_baidu.LogsSave('获取失败,请重试！ %s'% msg)
            else:
                # 提取搜索结果SERP的标题
                soup = BeautifulSoup(''.join(html))
                for i in soup.findAll("h3"):
                    title = i.text
                    if '百度' in title:
                        try:
                            title = title.split('\n')[1]
                        except Exception as msg:
                            pass
                        print(title)
                        self.inter_other_baidu.Resource_show(title)#需要修改
                        self.other_job_log_baidu.LogsSave(title)#需要修改
                    else:
                        print(title)
                        self.inter_other_baidu.Resource_show(title)#需要修改
                        self.other_job_log_baidu.LogsSave(title)#需要修改
class NewFiles:
    def __init__(self):
        self.inter_newfile = OtherJobs()
        self.other_job_log_newfile = Logs()
    def open_file(self,filepanth):
        if not filepanth:
            tps_open_content_empty = '未输入打开文件内容。'
            self.inter_newfile.Resource_show(tps_open_content_empty)
            self.other_job_log_newfile.LogsSave(tps_open_content_empty)
        elif '.' not in filepanth:
            tps_open_file_empty = '未输入打开的文件。'
            self.inter_newfile.Resource_show(tps_open_file_empty)
            self.other_job_log_newfile.LogsSave(tps_open_file_empty)
        else:
            if os.path.exists(filepanth):
                pass
            else:
                with open(filepanth,'w') as f:
                    f.close()
            os.system(filepanth)
    def open_dir_windows(self,path):
        if not path:
            path = r'C:\Users'
        elif '.' in path:
            path = os.path.split(path)[0]
        win32api.ShellExecute(0, 'open', path, '', '', 1)
        lists = os.listdir(path)
        print('%s的目录下内容包括:%s' % (path, lists))
        self.other_job_log_newfile.LogsSave('%s的目录下内容包括:%s' % (path, lists))
        self.inter_newfile.Resource_show('%s的目录下内容包括:%s' % (path, lists))
class LocateSearch:
    def __init__(self):
        self.inter_other = OtherJobs()
        self.inter_other_log_ls = Logs()
    def locate_search(self,search_content):
        if not search_content:
            tips_locate_search_content = '未输入搜索文件内容。'
            self.inter_other.Resource_show(tips_locate_search_content)
            self.inter_other_log_ls.LogsSave(tips_locate_search_content)
        else:
            search_all_cmd = self.inter_other.Get_Config_Info('file_name','search_all_cmd')
            search_close_cmd = self.inter_other.Get_Config_Info('file_name','search_close_cmd')
            save_path_searchresult = self.inter_other.Get_Config_Info('file_name','save_path_searchresult')
            save_path_search_result_path = os.path.dirname(os.path.dirname(__file__)) + save_path_searchresult
            search_all = search_all_cmd + ' ' + search_content
            subprocess.Popen(search_all)
            time.sleep(0.3)
            num_list0 = [18,70]
            num_list1 = [17,69]
            self.inter_other.mouse_input_remote_on(num_list0)
            self.inter_other.mouse_input_remote_up(num_list0)
            self.inter_other.mouse_input_remote_on(num_list1)
            self.inter_other.mouse_input_remote_up(num_list1)
            save_Path = save_path_search_result_path + search_content + '.txt'
            time.sleep(0.5)
            try:
                self.inter_other.save_WinSearchFile(save_Path)
                time.sleep(0.5)
            except Exception as msg:
                print(msg)
                save_search_result = '保存搜索结果失败！'
                print(save_search_result)
                self.inter_other_log_ls.LogsSave(msg)
                self.inter_other_log_ls.LogsSave(save_search_result)
            else:
                self.inter_other.print_File_Content(save_Path)
                time.sleep(1.5)
                #os.system(search_close_cmd)
                subprocess.Popen(search_close_cmd)
class WeiChat:
    def __init__(self):
        self.inter_other_wc = OtherJobs()
        self.other_job_log_wechat = Logs()
    def LoginWechat(self,num):
        wechat_path = self.inter_other_wc.Get_Config_Info('file_name','wechat_path')
        wChat_Conversation_window_class = self.inter_other_wc.Get_Config_Info('windows','wChat_Conversation_window_class')
        wChat_Login_window_class = self.inter_other_wc.Get_Config_Info('windows','wChat_Login_window_class')
        try:
            win32process.CreateProcess(wechat_path, '',None, None, 0, win32process.CREATE_NO_WINDOW, None, None,\
                                   win32process.STARTUPINFO())
        except Exception as msg:
            tips_open_wechat_err = '打开微信失败!'
            print(msg)
            print(tips_open_wechat_err)
            self.other_job_log_wechat.LogsSave(msg)
            self.other_job_log_wechat.LogsSave(tips_open_wechat_err)
        time.sleep(1)
        wChat_Conversation_hld = win32gui.FindWindow(wChat_Conversation_window_class,None)
        wChat_Login_hld = win32gui.FindWindow(wChat_Login_window_class,None)
        if wChat_Conversation_hld:
            pass
        if wChat_Login_hld:
            #handleDetail = win32gui.GetWindowRect(wChat_Login_hld)
            if  not num or int(num) == 1:
                self.inter_other_wc.mouse_input_remote_onup(13)
                #self.inter_other_wc.mouse_click_order(680, 410)
            else:
                #self.inter_other_wc.mouse_click_order(660, 485)
                self.inter_other_wc.mouse_input_remote_onup(9)
                time.sleep(0.1)
                self.inter_other_wc.mouse_input_remote_onup(13)
class KuGouMusic:
    def __init__(self):
        self.inter_other_kugou = OtherJobs()
    def play_Music_Name(self,music_name):
        kugou_music_path = self.inter_other_kugou.Get_Config_Info('file_name','kugou_music_path')
        print(music_name)
        win32process.CreateProcess(kugou_music_path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None,None, \
                                   win32process.STARTUPINFO())
        time.sleep(2)
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
        self.other_job_log_mail_operate = Logs()
    def LoginEmail(self, mail_addr, user_name, user_passwd):
        if not user_name or not user_passwd:
            tips_mail_content_empty = '未输入邮箱或者密码！'
            self.inter_other_mails.Resource_show(tips_mail_content_empty)
            self.other_job_log_mail_operate.LogsSave(tips_mail_content_empty)
        else:
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
            dr = webdriver.Chrome()
            dr.maximize_window()
            if int(mail_addr) == 2:
                try:
                    mail_yeah_url = self.inter_other_mails.Get_Config_Info('mails_info','126_mail_url')
                    dr.get(mail_yeah_url)
                    dr.find_element_by_xpath(get_login_state_126).click()
                    elementi = dr.find_element_by_xpath(get_frame_state_126)
                    dr.switch_to_frame(elementi)  # 切换frame
                    dr.find_element_by_xpath(input_login_username_126).send_keys(user_name)
                    dr.find_element_by_xpath(input_login_password_126).send_keys(user_passwd)
                    dr.find_element_by_xpath(click_login_button_126).click()
                    time.sleep(1)
                    dr.find_element_by_xpath(click_login_confirm_126).click()
                except Exception as msg:
                    login_126mail_err = '登陆126邮箱失败！'
                    print(msg)
                    print(login_126mail_err)
                    self.other_job_log_mail_operate.LogsSave(msg)
                    self.other_job_log_mail_operate.LogsSave(login_126mail_err)
                else:
                    time.sleep(600)
                    dr.close()
            if int(mail_addr) == 1:
                try:
                    mail_yeah_url = self.inter_other_mails.Get_Config_Info('mails_info', 'yeah_mail_url')
                    dr.get(mail_yeah_url)
                    elementi = dr.find_element_by_xpath(get_frame_state_yeah)
                    dr.switch_to_frame(elementi)  # 切换frame
                    dr.find_element_by_xpath(input_login_username_yeah).send_keys(user_name)
                    dr.find_element_by_xpath(input_login_password_yeah).send_keys(user_passwd)
                    dr.find_element_by_xpath(click_login_button_yeah).click()
                except Exception as msg:
                    login_yeahmail_err = '登陆yeah邮箱失败！'
                    print(msg)
                    print(login_yeahmail_err)
                    self.other_job_log_mail_operate.LogsSave(msg)
                    self.other_job_log_mail_operate.LogsSave(login_yeahmail_err)
                else:
                    time.sleep(600)
                    dr.close()
            if int(mail_addr) == 3:
                try:
                    mail_yeah_url = self.inter_other_mails.Get_Config_Info('mails_info', 'qq_mail_url')
                    dr.get(mail_yeah_url)
                    elementi = dr.find_element_by_xpath(get_frame_state_qq)
                    dr.switch_to_frame(elementi)  # 切换frame
                    dr.find_element_by_xpath(input_login_username_qq).send_keys(user_name)
                    dr.find_element_by_xpath(input_login_password_qq).send_keys(user_passwd)
                    dr.find_element_by_xpath(click_login_button_qq).click()
                except Exception as msg:
                    login_qqmail_err = '登陆qq邮箱失败！'
                    print(msg)
                    print(login_qqmail_err)
                    self.other_job_log_mail_operate.LogsSave(msg)
                    self.other_job_log_mail_operate.LogsSave(login_qqmail_err)
                else:
                    time.sleep(600)
                    dr.close()

class Resource_Monitor:
    def __init__(self):
        self.resource_monitor = OtherJobs()
        self.other_job_log_rm = Logs()
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
        print(disk_used)
        self.other_job_log_rm.LogsSave(disk_used)
        return disk_used

    def GetCpu(self):
        cpu_times = psutil.cpu_times()
        cpu_info = {'用户': 0, '系统': 0, '闲置': 0, '使用率': 0}
        cpu_info['用户'] = cpu_times.user
        cpu_info['系统'] = cpu_times.system
        cpu_info['闲置'] = cpu_times.idle
        cpu_info['使用率'] = '{}%'.format(psutil.cpu_percent(interval=2))
        print(cpu_info)
        self.other_job_log_rm.LogsSave(cpu_info)
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
        self.other_job_log_rm.LogsSave(memory_info)
        return memory_info

    def Monitor(self):
        while True:
            diskcost = self.GetCpan()
            cpucost = self.GetCpu()
            memorycost = self.GetCpu()
            alert = []
            for key, value in diskcost.items():
                if "%" in value:
                    disk_used_value = value.split('%')[0]
                    if float(disk_used_value) > 80:
                        alert.append(key + ' ' + value)
                        self.other_job_log_rm.LogsSave(alert)
            self.resource_monitor.SendMail(alert, diskcost)
            if float(str(cpucost['使用率']).split('%')[0]) > 10:
                cpu_alert = 'CPU使用率：' + cpucost['使用率']
                print(cpu_alert)
                self.other_job_log_rm.LogsSave(cpu_alert)
                self.resource_monitor.SendMail(cpu_alert, cpucost)
            if float(str(memorycost['使用率']).split('%')[0]) > 10:
                mem_alert = '内存使用率：' + memorycost['使用率']
                print(mem_alert)
                self.other_job_log_rm.LogsSave(mem_alert)
                self.resource_monitor.SendMail(mem_alert, memorycost)
            time.sleep(3600)
    def Get_Unreadmails_Num(self):
        global unread_mails_num_show
        cookies_file_path = self.resource_monitor.Get_Config_Info('file_name', 'save_cookies_path')  #
        cookies_file_path_all = os.path.dirname(os.path.dirname(__file__))+ cookies_file_path
        yeah_url = self.resource_monitor.Get_Config_Info('mails_info', 'yeah_mail_url')  #
        element_xpath_get_unread_num = self.resource_monitor.Get_Config_Info('element_xpath', 'unread_mails_yeah')  #
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        dr = webdriver.Chrome(chrome_options=chrome_options)
        #dr = webdriver.Chrome()
        unread_num = self.resource_monitor.Save_Cookies(dr,cookies_file_path_all, yeah_url)
        if unread_num:
            unread_mails_num_show = 'houtian_yu@yeah.com的未读邮件：' + unread_num + '条。'
            #self.other_job_log_rm.LogsSave(unread_mails_num_show)
        else:
            dr.get(yeah_url)
            #dr.maximize_window()
            self.resource_monitor.Read_Cookies(dr, cookies_file_path_all)
            try:
                time.sleep(0.5)
                unread_mails_num = dr.find_element_by_xpath(element_xpath_get_unread_num).text
            except Exception as msg:
                print(msg)
                cookies_noused = self.resource_monitor.Get_Config_Info('tips','cookies_noused')
                print(cookies_noused)
                self.other_job_log_rm.LogsSave(cookies_noused)
                os.remove(cookies_file_path_all)
                self.Get_Unreadmails_Num()
            else:
                unread_mails_num_show = 'houtian_yu@yeah.com的未读邮件：' + unread_mails_num + '条。'
                time.sleep(2)
                dr.close()
        self.other_job_log_rm.LogsSave(unread_mails_num_show)
        return unread_mails_num_show
