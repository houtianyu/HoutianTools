# coding: utf-8
import threading,win32com.client,win32api,win32con,win32gui,os,time,configparser
import email.mime.multipart,smtplib,subprocess
import email.mime.text,json,inspect,ctypes
from tkinter import *
from selenium import webdriver
from OverAll.overAll import OverAll
from Logs.logs import Logs
from win32gui import *
from win32api import *
from win32process import *
from win32con import *
class OtherJobs:
    def __init__(self,tk=None):
        self.i = 0
        self.tk = tk
        self.other_all = OverAll()
        self.other_job_log = Logs()
        self.cf = configparser.ConfigParser()
    def Count_Down(self,b,msg=' '):
        count = 0
        while (count < b):
            ncount = b - count
            print(msg + '请等待··· %s' % ncount)
            self.Resource_show(msg + '请等待··· %s' % ncount)
            time.sleep(1)
            count += 1
    def thread_add(self,func,*args):
        tt2 = threading.Thread(target=func,args=args)
        tt2.setDaemon(True)
        tt2.start()
        return tt2
    def Stop_Thread_add(self,thread):
        # _async_raise(thread.ident, SystemExit)
        tid = thread.ident
        exctype = SystemExit
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            pass
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
            #self.other_job_log.LogsSave("PyThreadState_SetAsyncExc failed")
    def get_entryContent(self,frame_v):
        return str(frame_v.get())
    def CheckProcExistByPN(self,process_name):
        try:
            WMI = win32com.client.GetObject('winmgmts:')
            processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
        except Exception as e:
            print("%s error : %s" % process_name,e)
        if len(processCodeCov) > 0:
            print("%s exist" % process_name)
            return True
        else:
            print("is not exist")
            return False
    def mouse_click_order(self,x,y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    def mouse_input_remote_on(self,list_num):
        for num in list_num:
            win32api.keybd_event(num, 0, 0, 0)
    def mouse_input_remote_up(self,list_num):
        for num in list_num:
            win32api.keybd_event(num, 0, win32con.KEYEVENTF_KEYUP, 0)
    def mouse_input_remote_onup(self,outstr):
        win32api.keybd_event(outstr, 0, 0, 0)
        win32api.keybd_event(outstr, 0, win32con.KEYEVENTF_KEYUP, 0)
    def save_WinSearchFile(self,path):
        windows_search_import = self.Get_Config_Info('windows','windows_search_import')
        windows_search_import_edit_class1=self.Get_Config_Info('windows','windows_search_import_edit_class1')
        windows_search_import_edit_class2=self.Get_Config_Info('windows','windows_search_import_edit_class2')
        windows_search_import_edit_class3=self.Get_Config_Info('windows','windows_search_import_edit_class3')
        windows_search_import_edit_class4=self.Get_Config_Info('windows','windows_search_import_edit_class4')
        windows_search_import_edit_class5=self.Get_Config_Info('windows','windows_search_import_edit_class5')
        windows_search_import_save_class=self.Get_Config_Info('windows','windows_search_import_save_class')
        windows_search_import_save=self.Get_Config_Info('windows','windows_search_import_save')
        time.sleep(0.5)
        hld = win32gui.FindWindow(None,windows_search_import)
        time.sleep(0.5)
        hld1 = win32gui.FindWindowEx(hld,None,windows_search_import_edit_class1,None)
        hld2 = win32gui.FindWindowEx(hld1, None, windows_search_import_edit_class2, None)
        hld3 = win32gui.FindWindowEx(hld2, None, windows_search_import_edit_class3, None)
        hld4 = win32gui.FindWindowEx(hld3, None, windows_search_import_edit_class4, None)
        hld5 = win32gui.FindWindowEx(hld4, None, windows_search_import_edit_class5, None)
        win32gui.SendMessage(hld5, win32con.WM_SETTEXT, None, path)
        hwnd_save = win32gui.FindWindowEx(hld, None, windows_search_import_save_class,windows_search_import_save)
        win32gui.PostMessage(hwnd_save, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.PostMessage(hwnd_save, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        try:
            self.mouse_input_remote_on([18,89])
            self.mouse_input_remote_up([18,89])
        except Exception as msg:
            tips_exe_import_search_file = '执行导出搜索结果失败！'
            print(msg)
            print(tips_exe_import_search_file)
            self.other_job_log.LogsSave(msg)
            self.other_job_log.LogsSave(tips_exe_import_search_file)
    def print_File_Content(self,path):
        i = 0
        for line in open(path,encoding='utf-8'):
            print(line,end='')
            if i <= 5:
                self.Resource_show(line)
            else:
                pass
            i += 1
    def Get_Config_Info(self, label, infos):
        config_ini = os.path.dirname(os.path.dirname(__file__) ) + '\\files\\Config.ini'
        self.cf.read(config_ini,encoding='ANSI')
        return self.cf.get(label,infos)
    def Modify_Config_Info(self,label,infos,values):
        config_ini = os.path.dirname(os.path.dirname(__file__)) + '\\files\\Config.ini'
        self.cf.read(config_ini, encoding='ANSI')
        self.cf.remove_option(label,infos)
        self.cf.set(label,infos,values)
        with open(config_ini, "w",encoding='ANSI') as f:
            self.cf.write(f)
    def SendMail(self, alert_value, detail):
        print('告警')
        from_username_yeah = self.Get_Config_Info('users_login_info', 'user_login_yeah_houtian').split(',')[0]  #
        from_passwd_yeah = self.Get_Config_Info('users_login_info', 'user_login_126_houtian').split(',')[-1]  #
        to_username_yeah = self.Get_Config_Info('users_login_info', 'user_login_126_houtian').split(',')[0]  #
        yeah_smtp_server_addr = self.Get_Config_Info('mails_info', 'yeah_smtp_server_addr')  #
        yeah_smtp_server_port = self.Get_Config_Info('mails_info', 'yeah_smtp_server_port')  #
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = from_username_yeah
        msg['to'] = to_username_yeah
        alert_info = str(alert_value).split('[')[-1].split(']')[0]
        detail_info = str(detail).split('OrderedDict')[-1].split('([')[-1].split('])')[0]
        msg['subject'] = '告警：<<' + alert_info + '>>'
        content = '注意：您的<<' + alert_info + '>>，超过预定值，请及时处理。详细信息：<<' + detail_info + '>>'
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        smtp = smtplib.SMTP()
        smtp.connect(yeah_smtp_server_addr,yeah_smtp_server_port)
        smtp.login(from_username_yeah,from_passwd_yeah)
        smtp.sendmail(from_username_yeah,to_username_yeah, str(msg))
        smtp.quit()
        tips_send_mail_content = '告警：' + alert_info + '发送成功！'
        print(tips_send_mail_content)
        self.other_job_log.LogsSave(tips_send_mail_content)

    def Save_Cookies(self,dr,cookies_name, url):
        login_frame_yeah_element = self.Get_Config_Info('element_xpath', 'get_frame_state_yeah')
        login_username_yeah_element = self.Get_Config_Info('element_xpath', 'input_login_username_yeah')
        login_passwd_yeah_element = self.Get_Config_Info('element_xpath', 'input_login_password_yeah')
        login_click_yeah_element = self.Get_Config_Info('element_xpath', 'click_login_button_yeah')
        username_yeah = self.Get_Config_Info('users_login_info', 'user_login_yeah_houtian').split(',')[0]  #
        passwd_yeah = self.Get_Config_Info('users_login_info', 'user_login_yeah_houtian').split(',')[-1]
        unread_element = self.Get_Config_Info('element_xpath','unread_mails_yeah')
        global unread_num
        unread_num = ''
        if os.path.exists(cookies_name):
            pass
        else:
            #dr = webdriver.Chrome()
            dr.get(url)
            get_cookies_tips = self.Get_Config_Info('tips', 'get_cookies')  #
            try:
                elementi = dr.find_element_by_xpath(login_frame_yeah_element)
                dr.switch_to_frame(elementi)  # 切换frame
                dr.find_element_by_xpath(login_username_yeah_element).send_keys(username_yeah)
                dr.find_element_by_xpath(login_passwd_yeah_element).send_keys(passwd_yeah)
                dr.find_element_by_xpath(login_click_yeah_element).click()
                time.sleep(1.5)
                try:
                    unread_num = dr.find_element_by_xpath(unread_element).text
                except Exception as msg:
                    tips_get_unread_mail_num_err = '未读邮件初次获取失败！'
                    print(msg)
                    self.other_job_log.LogsSave(msg)
                    self.other_job_log.LogsSave(tips_get_unread_mail_num_err)
            except Exception as msg:
                print(msg)
                tips_auto_get_cookies_err = '自动获取yeah邮箱登陆cookies失败！'
                print(tips_auto_get_cookies_err)
                self.other_job_log.LogsSave(msg)
                self.other_job_log.LogsSave(tips_auto_get_cookies_err)
                dr.close()
                dr = webdriver.Chrome()
                dr.get(url)
                self.other_job_log.LogsSave(get_cookies_tips)
                input(get_cookies_tips)
            # 获取cookie并通过json模块将dict转换成str
            dictCookies = dr.get_cookies()  # 核心
            jsonCookies = json.dumps(dictCookies)
            # 登录完成后将cookie保存到本地文件
            with open(cookies_name, 'w') as f:
                f.write(jsonCookies)
            time.sleep(1)
            dr.close()
            return unread_num
    def Read_Cookies(self, dr, cookies_name):
        with open(cookies_name, 'r', encoding='utf8') as f:
            listCookies = json.loads(f.read())
        for cookie in listCookies:
            dr.add_cookie({
                "domain": cookie['domain'],
                "httpOnly": cookie['httpOnly'],
                "name": cookie['name'],
                "path": "/",
                "secure": cookie['secure'],
                "value": cookie['value']
            })
        dr.refresh()  # 读取完cookie刷新页面
    def Resource_show(self,msg):
        try:
            textlabel = self.other_all.get_label_value(0)
            textlabel.grid_forget()
        except Exception as msgs:
            pass
        v_monitor = StringVar()
        frame_monitor = Frame(self.tk,height=5,relief=GROOVE).grid(padx=5,row=9,column=0,columnspan=9,sticky=W)
        v_monitor.set(msg)
        textlabel = Message(frame_monitor, textvariable=v_monitor, justify=LEFT, width=800, font=("华康少女字体", 10),fg="red")
        self.other_all.set_label_value(textlabel)
        textlabel.grid(padx=5, pady=1, row=9, column=0, columnspan=9, sticky=W)
    def Init_Exe_Path(self):
        init_infos = {'kugou_music_path':'KuGou.exe','qh360_grabage_path':'360Safe.exe','wechat_path':'WeChat.exe'}
        for search_content_info,search_content in init_infos.items():
            search_all_cmd = self.Get_Config_Info('file_name','search_all_init_cmd')
            search_close_cmd = self.Get_Config_Info('file_name','search_close_init_cmd')
            save_path_searchresult = self.Get_Config_Info('file_name','save_path_searchresult')
            save_path_search_result_path = os.path.dirname(os.path.dirname(__file__)) + save_path_searchresult
            search_all = search_all_cmd + ' ' + search_content
            try:
                subprocess.Popen(search_all)
            except Exception as msg:
                print(msg)
                print('配置文件中Everything程序路径不正确，请检查。')
                self.Resource_show('配置文件中Everything程序路径不正确，请检查。')
                self.other_job_log.LogsSave('配置文件中Everything程序路径不正确，请检查。')
                self.other_job_log.LogsSave(msg)
            time.sleep(0.5)
            #num_list0 = [18,70]
            #num_list1 = [17,69]
            num_list2 = [17,83]
            #self.mouse_input_remote_on(num_list0)
            #self.mouse_input_remote_up(num_list0)
            #self.mouse_input_remote_on(num_list1)
            #self.mouse_input_remote_up(num_list1)
            self.mouse_input_remote_on(num_list2)
            self.mouse_input_remote_up(num_list2)
            save_Path = save_path_search_result_path + search_content + '.txt'
            try:
                self.save_WinSearchFile(save_Path)
                time.sleep(0.5)
            except Exception as msg:
                print(msg)
                save_search_result = '保存搜索结果失败！'
                self.other_job_log.LogsSave(msg)
                self.other_job_log.LogsSave(save_search_result)
            else:
                i = 0
                for line in open(save_Path,encoding='utf-8'):
                    if i == 1:
                        path = line.split(',')[0].split('"')[1].split('"')[0]
                        if 'Users' in path:
                            pass
                        else:
                            path = path.replace("\\", '\\\\')
                            if path.split('.')[-1] == 'exe':
                                print(path)
                                self.Modify_Config_Info('file_name',search_content_info,path)
                                break
                            else:
                                print('第一次未找到%s的执行文件！' % search_content)
                                self.Resource_show('第一次未找到%s的执行文件！' % search_content)
                                self.other_job_log.LogsSave('第一次未找到%s的执行文件！' % search_content)
                    if i == 2:
                        path = line.split(',')[0].split('"')[1].split('"')[0]
                        path = path.replace("\\", '\\\\')
                        if path.split('.')[-1] == 'exe':
                            print(path)
                            self.Modify_Config_Info('file_name',search_content_info,path)
                            break
                        else:
                            print('第二次未找到%s的执行文件！' % search_content)
                            self.Resource_show('第二次未找到%s的执行文件！' % search_content)
                            self.other_job_log.LogsSave('第二次未找到%s的执行文件！' % search_content)
                    i += 1
                time.sleep(1.2)
                subprocess.Popen(search_close_cmd)
    #def Display_login_Sweepcode(self):
        #os.path.dirname(os.path.dirname(__file__)) + '\\GuiDisplay\\QR.png'

if __name__ == '__main__':
    a = OtherJobs()
