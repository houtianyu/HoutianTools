import threading,win32com.client,win32api,win32con,win32gui,os,time,configparser
import email.mime.multipart,logging,datetime,smtplib
import email.mime.text,json
from win32gui import *
from win32api import *
from win32process import *
from win32con import *
class OtherJobs:
    def __init__(self):
        self.i = 0
    def thread_add(self,func,*args):
        tt2 = threading.Thread(target=func,args=args)
        tt2.setDaemon(True)
        tt2.start()
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
            print(msg)
    def print_File_Content(self,path):
        for line in open(path,encoding='utf-8'):
            print(line,end='')
    def Get_Config_Info(self, label, infos):
        cf = configparser.ConfigParser()
        cf.read('D:\\python\\test\\files\\Config.ini', encoding='UTF-8')
        return cf.get(label, infos)
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
        smtp.connect(yeah_smtp_server_addr, yeah_smtp_server_port)
        smtp.login(from_username_yeah, from_passwd_yeah)
        smtp.sendmail(from_username_yeah, to_username_yeah, str(msg))
        smtp.quit()

    def Save_Cookies(self,dr,cookies_name, url):
        if os.path.exists(cookies_name):
            pass
        else:
            dr.get(url)
            get_cookies_tips = self.Get_Config_Info('tips', 'get_cookies')  #
            input(get_cookies_tips)
            # elementi = dr.find_element_by_xpath('//*[@frameborder="0"]')
            # dr.switch_to_frame(elementi)  # 切换frame
            # dr.find_element_by_xpath('//input[@data-placeholder="邮箱帐号或手机号"]').send_keys('houtian_yu')
            # dr.find_element_by_name("password").send_keys('yulei927623')
            # dr.find_element_by_id('dologin').send_keys(Keys.ENTER)
            # 获取cookie并通过json模块将dict转换成str
            dictCookies = dr.get_cookies()  # 核心
            jsonCookies = json.dumps(dictCookies)
            # 登录完成后将cookie保存到本地文件
            with open(cookies_name, 'w') as f:
                f.write(jsonCookies)
            time.sleep(1)
            dr.close()

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

class Logs:
    def __init__(self):
        self.get_info = OtherJobs()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        base_dir = self.get_info.Get_Config_Info('file_name','logs_base_dir')
        base_dir_path = os.getcwd() + base_dir
        log_file_dir = base_dir_path + '_' + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
        self.file_logs = logging.FileHandler(log_file_dir,'a',encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelno)s %(levelname)s<->%(message)s')
        self.file_logs.setFormatter(formatter)
        self.logger.addHandler(self.file_logs)
    def get_logger(self):
        return self.logger
    def close_log(self):
        self.file_logs.close()
        self.logger.removeHandler(self.file_logs)
    def LogsSave(self,msg_content,level_info=None):
        logging = self.get_logger()
        if level_info == 'info':
            logging.info(msg_content)
        if level_info == 'debug':
            logging.debug(msg_content)
        if level_info == 'warning':
            logging.warning(msg_content)
        if level_info == 'error':
            logging.error(msg_content)
        if level_info == 'critical':
            logging.critical(msg_content)
        else:
            logging.debug(msg_content)
if __name__ == '__main__':
    a = OtherJobs()
