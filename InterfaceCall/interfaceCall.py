# coding: utf-8
from selenium import webdriver
from OverAll.overAll import OverAll
from OtherJobs.otherJob import *
from Logs.logs import Logs
import os,sys,win32process,win32gui,time,win32con,collections,psutil
from win32api import *
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time,urllib.request,random,sys,importlib,shutil
from urllib.parse import quote
import urllib,subprocess,itchat
from itchat.content import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from lxml import etree
from urllib.request import urlretrieve
from tkinter.filedialog import askdirectory
import requests,urllib.request,json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import email.mime.multipart,smtplib,subprocess,email.mime.text
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib,poplib,email,base64,imaplib, string
from email.mime.application import MIMEApplication
from io import StringIO
from email.parser import Parser

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
        title_all = {}
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
                        title_all[title] = '内容需要完善'
                        self.other_job_log_baidu.LogsSave(title)#需要修改
                    else:
                        title_all[title] = '内容需要完善'
                        self.other_job_log_baidu.LogsSave(title)#需要修改
        print(title_all)
        self.inter_other_baidu.Resource_show(title_all)
        self.other_job_log_baidu.LogsSave(title_all)
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
        self.text_contents = []
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
        else:
            time.sleep(0.1)
            wChat_Conversation_hld = win32gui.FindWindow(wChat_Conversation_window_class,None)#绘画窗口
            wChat_Login_hld = win32gui.FindWindow(wChat_Login_window_class,None)
            if wChat_Conversation_hld:
                if not num or int(num) == 1:
                    pass
                else:
                    time.sleep(0.05)
                    current_locate = win32gui.GetWindowRect(wChat_Conversation_hld)
                    self.inter_other_wc.mouse_click_order(current_locate[0] + 20,current_locate[3] - 20 )
                    time.sleep(0.1)
                    for i in range(2):
                        self.inter_other_wc.mouse_input_remote_onup(9)
                    self.inter_other_wc.mouse_input_remote_onup(13)
                    time.sleep(0.3)
                    self.inter_other_wc.mouse_click_order(950, 350 )
                    time.sleep(0.1)
                    for i in range(4):
                       self.inter_other_wc.mouse_input_remote_onup(9)
                    self.inter_other_wc.mouse_input_remote_onup(13)
                    time.sleep(0.05)
                    self.inter_other_wc.mouse_input_remote_onup(13)
                    time.sleep(1)
                    self.inter_other_wc.mouse_input_remote_onup(9)
                    time.sleep(0.1)
                    self.inter_other_wc.mouse_input_remote_onup(13)
            elif wChat_Login_hld:
                #handleDetail = win32gui.GetWindowRect(wChat_Login_hld)
                if  not num or int(num) == 1:
                    self.inter_other_wc.mouse_input_remote_onup(13)
                    #self.inter_other_wc.mouse_click_order(680, 410)
                else:
                    #self.inter_other_wc.mouse_click_order(660, 485)
                    self.inter_other_wc.mouse_input_remote_onup(9)
                    time.sleep(0.1)
                    self.inter_other_wc.mouse_input_remote_onup(13)
    def Show_Msg_WeChat(self,top,contents,row):
        try:
            textlabel.grid_forget()
        except Exception as msg:
            print(msg)
            pass
        v_monitor = StringVar()
        v_monitor.set(contents)
        textlabel = Message(top, textvariable=v_monitor, justify=LEFT, width=325, font=("华康少女字体", 10),fg="red")
        textlabel.grid(padx=5, pady=1, row=row, column=0, columnspan=3, sticky=W)
    def LoginWeChat_Sweepcode_Method(self,num,top):
        def close_QR_img():
            #creat_time_2 = os.path.getctime(wechat_qr_path)
            #print(wechat_qr_path)
            #if creat_time_1 != creat_time_2:
            #render = PhotoImage(file=wechat_qr_path)
            #img = Label(top, image=render)
            #img.grid(padx=1, pady=5, row=1, column=1, columnspan=3, sticky=W)
            userinfo = itchat.web_init()
            print('登陆完成！账号为：%s!' % userinfo['User']['NickName'])
            self.Show_Msg_WeChat(top,('登陆完成！账号为：%s!' % userinfo['User']['NickName']),1)
            self.inter_other_wc.End_Program('Microsoft.Photos.exe')
        def loginout_img():
            print('已退出登录！')
            self.Show_Msg_WeChat(top, '登陆完成！', 1)
        if not num or int(num) == 1:
            value = True
        else:
            value = False
        #wechat_qr_path = os.path.dirname(os.path.dirname(__file__)) + '\\GuiDisplay\\QR.png'
        #creat_time_1 = os.path.getctime(wechat_qr_path)
        print('请扫码登陆！')
        itchat.auto_login(hotReload=value,loginCallback=close_QR_img,exitCallback=loginout_img)#hotReload=True,
        itchat.run()
    def SearchWeChat_Contacts_Method(self,Contacts_name,top):
        result = itchat.search_friends(name=Contacts_name)
        if not result:
            contacts_msg = '请确认微信是否已经登录，若已登录，则您当前无此联系人！'
            print(contacts_msg)
            self.Show_Msg_WeChat(top,contacts_msg,2)
        else:
            if result[0]['Sex'] == 2:
                sex = '女'
            else:
                sex = '男'
            contacts_msg = '查找的好友信息：微信名称：'+ result[0]['NickName'] +' 当前昵称：' + result[0]['RemarkName'] + \
                           ' 个性签名：' + result[0]['Signature'] + ' 性别：' + sex
            print(contacts_msg)
            try:
                self.Show_Msg_WeChat(top,contacts_msg,2)
            except Exception as msg:
                print(msg)
                print('用户信息包含特殊文字，微信名：%s' % result[0]['NickName'])
                self.Show_Msg_WeChat(top,('用户信息包含特殊文字，微信名：%s' % result[0]['NickName']),2)
    def SendWeChat_Messages_Method(self,Contacts_name,Send_contents,top):
        user_info = itchat.search_friends(name=Contacts_name)
        if len(user_info) > 0:
            user_name = user_info[0]['UserName']
            itchat.send_msg(Send_contents,user_name)
        else:
            print('联系人昵称不存在')
            self.Show_Msg_WeChat(top, '联系人昵称不存在', 4)
    def SendWeChat_Files_Method(self,Contacts_name,Send_contents,top):
        def send_files(contents):
            if contents.split('.')[-1] in ['jpg', 'png']:
                itchat.send_image(contents, user_name)
            elif contents.split('.')[-1] in ['mp4']:
                itchat.send_video(contents, user_name)
            else:
                itchat.send_file(contents, user_name)
        user_info = itchat.search_friends(name=Contacts_name)
        if not self.text_contents and not Send_contents:
            print('请选择或输入要发送的文件！')
        else:
            if len(user_info) > 0:
                user_name = user_info[0]['UserName']
                if Send_contents:
                    #Send_contents = Send_contents.encode('utf8')
                    send_files(Send_contents)
                    print('%s文件发送成功！' % Send_contents.split('/')[-1])
                if self.text_contents:
                    for text in self.text_contents:
                        #text = text.encode('utf8')
                        send_files(text)
                        print('%s 文件发送成功！' % text.split('/')[-1])
            else:
                print('联系人昵称不存在')
                self.Show_Msg_WeChat(top, '联系人昵称不存在', 4)
    def ChoiseWeChat_Files_Method(self,top,text):
        self.text_contents = []
        selectFiles = tk.filedialog.askopenfilenames(title='可选择1个或多个文件')  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
        for selectFile in selectFiles:
            text.insert(tk.END, selectFile + '\n')  # 更新text中内容
            text.update()
        self.text_contents= text.get('0.0', 'end').split('\n')[0:-2]
        print(self.text_contents)
    def GetWeChat_Messages_Method(self,Contacts_name_get,type,top):
        # 文件临时存储页
        rec_tmp_dir = os.path.dirname(os.path.dirname(__file__)) + '\\files\\wechat\\tmp\\'
        print(Contacts_name_get)
        if not os.path.exists(rec_tmp_dir):
            os.mkdir(rec_tmp_dir)
        # 存储数据的字典
        rec_msg_dict = {}
        # 好友信息监听
        @itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True)
        def handle_friend_msg(msg):
            msg_id = msg['MsgId']
            msg_from_user = msg['User']['NickName']
            msg_content = ''
            # 收到信息的时间
            msg_time_rec = time.strftime("%Y-%m-%d %H:%M%S", time.localtime())
            msg_create_time = msg['CreateTime']
            msg_type = msg['Type']
            if msg['Type'] == 'Text':
                msg_content = msg['Content']
            elif msg['Type'] == 'Picture' \
                    or msg['Type'] == 'Recording' \
                    or msg['Type'] == 'Video' \
                    or msg['Type'] == 'Attachment':
                msg_content = r"" + msg['FileName']
                msg['Text'](rec_tmp_dir + msg['FileName'])
            rec_msg_dict.update({
                msg_id: {
                    'msg_from_user': msg_from_user,
                    'msg_time_rec': msg_time_rec,
                    'msg_create_time': msg_create_time,
                    'msg_type': msg_type,
                    'msg_content': msg_content
                }
            })
            if msg_from_user == Contacts_name_get and type == 0:
                print('*****和联系人 %s 的最新消息是: %s,时间：%s' % (Contacts_name_get,msg_content,msg['CreateTime']))
                self.Show_Msg_WeChat(top,('*****和联系人 %s 的最新消息是: %s,时间：%s' % (Contacts_name_get,msg_content,msg['CreateTime'])),2)
            else:
                print('其他联系人 %s 消息:%s,发送时间：%s' % (msg['User']['NickName'],msg_content,msg['CreateTime']))
                self.Show_Msg_WeChat(top, ('其他联系人 %s 消息:%s,发送时间：%s' % (msg['User']['NickName'],msg_content,msg['CreateTime'])), 2)
        # 群聊信息监听
        @itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
        def information(msg):
            msg_id = msg['MsgId']
            msg_from_user = msg['ActualNickName']
            msg_content = ''
            # 收到信息的时间
            msg_time_rec = time.strftime("%Y-%m-%d %H:%M%S", time.localtime())
            msg_create_time = msg['CreateTime']
            msg_type = msg['Type']

            if msg['Type'] == 'Text':
                msg_content = msg['Content']
            elif msg['Type'] == 'Picture' \
                    or msg['Type'] == 'Recording' \
                    or msg['Type'] == 'Video' \
                    or msg['Type'] == 'Attachment':
                msg_content = r"" + msg['FileName']
                msg['Text'](rec_tmp_dir + msg['FileName'])
            rec_msg_dict.update({
                msg_id: {
                    'msg_from_user': msg_from_user,
                    'msg_time_rec': msg_time_rec,
                    'msg_create_time': msg_create_time,
                    'msg_type': msg_type,
                    'msg_content': msg_content
                }
            })
            if msg_from_user == Contacts_name_get and type == 0:
                print('*****%s昵称的群成员最新消息是: %s,发送者群昵称：%s,发送时间：%s' % (Contacts_name_get,msg_content,msg['ActualNickName'],msg['CreateTime']))
                self.Show_Msg_WeChat(top, ('*****%s昵称的群成员最新消息是: %s,发送者群昵称：%s,发送时间：%s' % (Contacts_name_get,msg_content,msg['ActualNickName'],msg['CreateTime'])), 2)
            else:
                print('其他群消息: %s,发送者群昵称：%s,发送时间：%s' % (msg_content,msg['ActualNickName'],msg['CreateTime']))
                self.Show_Msg_WeChat(top,('其他群消息: %s,发送者群昵称：%s,发送时间：%s' % (msg_content,msg['ActualNickName'],msg['CreateTime'])),2)
    def CancelWeChat_LoginOut_Method(self,top):
        itchat.logout()
        print('正在注销！')
        self.Show_Msg_WeChat(top, '正在注销！', 2)
class KuGouMusic:
    def __init__(self):
        self.inter_other_kugou = OtherJobs()
        self.mp3_info = {} #全局变量，存放歌曲名和hash
        self.music_download_path = os.path.dirname(os.path.dirname(__file__)) + '\\files\\music_download\\'
        self.music_status = None
    def play_Music_Name(self,type):
        global status
        kugou_music_path = self.inter_other_kugou.Get_Config_Info('file_name','kugou_music_path')
        if type == 0:
            win32process.CreateProcess(kugou_music_path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None,win32process.STARTUPINFO())
            time.sleep(2)
            self.inter_other_kugou.mouse_input_remote_on([18,116])
            self.inter_other_kugou.mouse_input_remote_up([18,116])
            status = 0
        elif type == 1:
            if status == 0:
                self.inter_other_kugou.mouse_input_remote_on([18, 37])
                self.inter_other_kugou.mouse_input_remote_up([18, 37])
            else:
                print('请先播放音乐！')
        elif type == 2:
            if status == 0:
                self.inter_other_kugou.mouse_input_remote_on([18, 39])
                self.inter_other_kugou.mouse_input_remote_up([18, 39])
            else:
                print('请先播放音乐！')
        elif type == 3:
            if status == 0:
                self.inter_other_kugou.mouse_input_remote_on([18, 38])
                self.inter_other_kugou.mouse_input_remote_up([18, 38])
            else:
                print('请先播放音乐！')
        elif type == 4:
            if status == 0:
                self.inter_other_kugou.mouse_input_remote_on([18, 40])
                self.inter_other_kugou.mouse_input_remote_up([18, 40])
            else:
                print('请先播放音乐！')
        elif type == 5:
            if status == 0:
                self.inter_other_kugou.mouse_input_remote_on([17, 18,88])
                self.inter_other_kugou.mouse_input_remote_up([17, 18,88])
                time.sleep(1)
                download_hld = win32gui.FindWindow(None,'下载窗口')
                print(download_hld)
                if download_hld:
                    for i in range(11):
                        self.inter_other_kugou.mouse_input_remote_onup(9)
                    self.inter_other_kugou.mouse_input_remote_onup(13)
                    print('歌曲已下载至“D:\KuGou\”目录！')
                else:
                    print('此歌曲无法下载！')
            else:
                print('请先播放音乐！')
        else:
            pass
    def Show_Msg_Kugou_Music(self,top,contents,row):
        try:
            textlabel.grid_forget()
        except Exception as msg:
            print(msg)
            pass
        v_monitor = StringVar()
        v_monitor.set(contents)
        textlabel = Message(top, textvariable=v_monitor, justify=LEFT, width=325, font=("华康少女字体", 10),fg="red")
        textlabel.grid(padx=5, pady=10, row=row, column=0, columnspan=7, sticky=W)
    def Play_Music_More_Method(self,top,names,text_music,type):
        if not names:
            print('请输入需要播放的歌曲！')
            self.Show_Msg_Kugou_Music(top,'请输入需要播放的歌曲！',3)
        else:
            def show_music_result():
                text_music.delete(0, END)
                song = names  # 获得歌曲名
                url = "http://songsearch.kugou.com/song_search_v2?callback=jQuery112407470964083509348_1534929985284&keyword={}&" \
                      "page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filte" \
                      "r=0&_=1534929985286".format(song)
                res = requests.get(url).text  # 收到的数据 type(res)是个str 把不必要地方去掉 因为loads方法的字符串应该形如字典{}
                js = json.loads(res[res.index('(') + 1:-2])
                data = js['data']['lists']  # 这是一个列表
                for i in range(len(data)):
                    text_music.insert(END, ">>" + str(data[i]['FileName']).replace('<em>', '').replace('</em>', ''))
                    text_music.see(END)
                    text_music.update()
                    name = str(data[i]['FileName']).replace('<em>', '').replace('</em>', '')
                    fhash = str(data[i]['FileHash'])
                    self.mp3_info[name] = fhash
            def start_music(num_cu_type=None):
                if self.music_status == None or self.music_status == 2:
                    if names:
                        try:
                            num = text_music.curselection()[0]  # 结果是一个一维元组如(5,)获取当前鼠标位置
                        except Exception as msg:
                            print(msg)
                            print('请选择歌曲！')
                        else:
                            if num != None:  # 选择的是num首歌，对应的data[num] ，listbox下标从0开始
                                if num_cu_type == None:
                                    num_cu = num
                                elif num_cu_type == 0:
                                    if num == 0:
                                        mp3_name1 = text_music.get(0)[2:]
                                        print('当前%s是第一首歌，无法进行上一曲！' % mp3_name1)
                                        self.Show_Msg_Kugou_Music(top,('当前%s是第一首歌，无法进行上一曲！' % mp3_name1), 3)
                                        num_cu = num
                                    else:
                                        num_cu = num - 1
                                else:
                                    if num == 29:
                                        mp3_name1 = text_music.get(29)[2:]
                                        print('当前%s是最后一首歌，无法进行下一曲！' % mp3_name1)
                                        self.Show_Msg_Kugou_Music(top,('当前%s是最后一首歌，无法进行下一曲！' % mp3_name1), 3)
                                        num_cu = num
                                    else:
                                        num_cu = num + 1
                                global mp3_name
                                mp3_name = text_music.get(num_cu)[2:]  # 因为前三个符号是>>>用于提示，剔除后才是真正的歌名
                                mp3_hash = self.mp3_info.get(mp3_name)  # hash码
                                url2 = 'https://www.kugou.com/song/#hash=' + mp3_hash
                                print('请等待播放:%s' % mp3_name)
                                self.Show_Msg_Kugou_Music(top,('请等待播放:%s' % mp3_name), 3)
                                chrome_options = Options()
                                chrome_options.add_argument('--headless')
                                chrome_options.add_argument('--disable-gpu')
                                global driver
                                driver = webdriver.Chrome(chrome_options=chrome_options)
                                #driver = webdriver.Chrome()
                                driver.get(url2)
                                driver.find_element_by_xpath('//*[@id="toggle"]').click()
                                self.music_status = 0
                                print('正在播放:%s 歌曲' % mp3_name)
                                self.Show_Msg_Kugou_Music(top,('正在播放:%s 歌曲' % mp3_name), 3)
                else:
                    print('请先停止当前音乐:%s' % mp3_name)
                    self.Show_Msg_Kugou_Music(top,('请先停止当前音乐:%s' % mp3_name),3)
            def download_music():
                if names:
                    num = text_music.curselection()[0]  # 结果是一个一维元组如(5,)
                    if num != None:  # 选择的是num首歌，对应的data[num] ，listbox下标从0开始
                        mp3_name = text_music.get(num)[3:]  # 因为前三个符号是>>>用于提示，剔除后才是真正的歌名
                        mp3_hash = self.mp3_info.get(mp3_name)  # hash码
                        url2 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=' + mp3_hash + '&album_id=&dfid=1su9ai3vuKEp0AvUgT0sXDoE&mid=8a2d9e872bdbd1b9d25aa62d1473aa1f&platid=4&_=1559998974444'
                        req = urllib.request.Request(url2)  #
                        response = urllib.request.urlopen(req, None, 30)  # 设置超时时间
                        html = response.read().decode('utf-8')
                        html = json.loads(html)
                        play_url = html['data']['play_url']
                        try:
                            path = self.music_download_path + mp3_name + '.mp3'#+ '/'
                            if '\\' in path:
                                path = path.replace('\\', '/')
                            urlretrieve(play_url, path)
                            tkinter.messagebox._show('提示', '下载成功')
                            self.Show_Msg_Kugou_Music(top,'下载成功', 3)
                            return
                        except Exception as e:
                            print("写入文件失败,原因：%s" % e)
                            self.Show_Msg_Kugou_Music(top,("写入文件失败,原因：%s" % e), 3)
                            return
            def cleartxt_music():
                text_music.delete(0, END)
            def help_info():
                tkinter.messagebox._show('帮助','输入下载的歌曲名，单曲搜索结果选中某行后再进行下载,重新搜索记得清空列表!')
            def suspend_music():
                if self.music_status == 0 or self.music_status == 1:
                    driver.find_element_by_xpath('//*[@id="toggle"]').click()
                    self.music_status = 1
                else:
                    print('请先播放音乐！')
                    self.Show_Msg_Kugou_Music(top,'请先播放音乐！', 3)
            def stop_music():
                if self.music_status == 0 or self.music_status ==1:
                    driver.close()
                    self.music_status = 2
                else:
                    print('音乐未播放，无需停止！')
                    self.Show_Msg_Kugou_Music(top,'音乐未播放，无需停止！', 3)
            def last_music():
                driver.close()
                self.music_status = 2
                self.inter_other_kugou.mouse_input_remote_onup(38)
                start_music(0)
            def next_music():
                driver.close()
                self.music_status = 2
                self.inter_other_kugou.mouse_input_remote_onup(40)
                start_music(1)
            if type == 0:
                show_music_result()
            elif type == 1:
                start_music()
            elif type == 2:
                download_music()
            elif type == 3:
                cleartxt_music()
            elif type == 4:
                help_info()
            elif type == 5:
                stop_music()
            elif type == 6:
                suspend_music()
            elif type == 7:
                last_music()
            elif type == 8:
                next_music()
class LaJiQingLi:
    def __init__(self):
        self.inter_other_Garbage = OtherJobs()
        self.LaJiQingLi_show = WeiChat()
        self.del_info = {}
        self.del_file_paths = []
        self.total_size = 0
        self.del_all_files_num = 0
        self.del_faliue_file = []
        del_extension = {
            '.tmp': '临时文件',
            '._mp': '临时文件_mp',
            '.log': '日志文件',
            '.gid': '临时帮助文件',
            '.chk': '磁盘检查文件',
            '.old': '临时备份文件',
            '.xlk': 'Excel备份文件',
            '.bak': '临时备份文件bak'
        }
        self.wx_path = self.inter_other_Garbage.Get_Config_Info('file_name','weixin_userinfo')
        self.del_userprofile = ['Files', 'FileStorage', 'HDHeadImage', 'Image', 'Video', 'Attachment']
        SYS_DRIVE = os.environ['systemdrive'] + '\\'
        USER_PROFILE = os.environ['userprofile']
        WIN_DIR = os.environ['windir']
        self.scan_path = [SYS_DRIVE, USER_PROFILE, WIN_DIR]
        for k, v in del_extension.items():
            self.del_info[k] = dict(name=v, count=0)
    def Clear_All(self,value):
        qh360_grabage_path = self.inter_other_Garbage.Get_Config_Info('file_name', 'qh360_grabage_path')
        print(value)
        win32process.CreateProcess(qh360_grabage_path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None, \
                                   win32process.STARTUPINFO())
    def FormatSize(self,top):
        try:
            self.total_size = float(self.total_size)
            kb = self.total_size / 1024
        except:
            print("传入的字节格式不对!")
            self.LaJiQingLi_show.Show_Msg_WeChat(top,'传入的字节格式不对!',1)
            return "Error"
        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%fG" % (G)
            else:
                return "%fM" % (M)
        else:
            return "%fkb" % (kb)
    def Del_dir_or_file(self,root,top):
        try:
            if os.path.isfile(root):
                # 删除文件
                os.remove(root)
                print('文件: ' + root + ' 已经删除！')
                self.LaJiQingLi_show.Show_Msg_WeChat(top,('文件: ' + root + ' 已经删除！'),1)
            elif os.path.isdir(root):
                # 删除文件夹
                shutil.rmtree(root)
                print('目录： ' + root + ' 已经删除！')
                self.LaJiQingLi_show.Show_Msg_WeChat(top,('目录： ' + root + ' 已经删除！'),1)
        except WindowsError:
            print('错误: ' + root + " 删除失败！")
            self.LaJiQingLi_show.Show_Msg_WeChat(top,('错误: ' + root + " 删除失败！"),1)
            self.del_faliue_file.append(root)
    def Scan_Workspace_Method(self,top):
        for dirs_p in self.scan_path:
            for roots, dirs, files in os.walk(dirs_p, topdown=False):
                # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
                for file_item in files:
                    # 获取扩展名
                    file_extension = os.path.splitext(file_item)[1]
                    # print os.path.join(roots, file_item)
                    if file_extension in self.del_info:
                        # 文件完整路径
                        file_full_path = os.path.join(roots, file_item)
                        print('完成扫描%s 的路径' % file_full_path)
                        self.LaJiQingLi_show.Show_Msg_WeChat(top,('完成扫描%s 的路径' % file_full_path), 1)
                        self.del_file_paths.append(file_full_path)
                        self.del_info[file_extension]['count'] += 1
                        self.total_size += os.path.getsize(file_full_path)
            print('%s 目录扫描完成！' % dirs_p)
            self.LaJiQingLi_show.Show_Msg_WeChat(top,('%s 目录扫描完成！' % dirs_p), 1)
        for dirs_wx in self.del_userprofile:
            wx_dirs_path_all = self.wx_path + dirs_wx
            for roots,dirs,files in os.walk(wx_dirs_path_all,topdown=False):
                for wx_file_item in files:
                    wx_file_full_path = os.path.join(roots, wx_file_item)
                    print('完成扫描%s 的路径' % wx_file_full_path)
                    self.LaJiQingLi_show.Show_Msg_WeChat(top,('完成扫描%s 的路径' % wx_file_full_path), 1)
                    self.del_file_paths.append(wx_file_full_path)
                    self.del_all_files_num += 1
                    self.total_size += os.path.getsize(wx_file_full_path)
            print('%s 目录扫描完成！' % wx_dirs_path_all)
            self.LaJiQingLi_show.Show_Msg_WeChat(top,('%s 目录扫描完成！' % wx_dirs_path_all), 1)
        #print(json.dumps(self.del_info, indent=4, ensure_ascii=False))
        print('.tmp格式的%s数：%s,._mp格式的%s数：%s,.log格式的%s数：%s,.gid格式的%s数：%s,.chk格式的%s数：%s,.old格式的%s数：%s,.xlk格式的%s数：%s,.bak格式的%s数：%s' \
            % (self.del_info['.tmp']['name'], self.del_info['.tmp']['count'], self.del_info['._mp']['name'],self.del_info['._mp']['count'], \
               self.del_info['.log']['name'], self.del_info['.log']['count'], self.del_info['.gid']['name'],self.del_info['.gid']['count'], \
               self.del_info['.chk']['name'], self.del_info['.chk']['count'], self.del_info['.old']['name'],self.del_info['.old']['count'], \
               self.del_info['.xlk']['name'], self.del_info['.xlk']['count'], self.del_info['.bak']['name'],self.del_info['.bak']['count']))
        self.del_all_files_num = self.del_all_files_num + self.del_info['.tmp']['count'] + self.del_info['._mp']['count'] + self.del_info['.gid']['count'] + self.del_info['.log']['count'] + self.del_info['.old']['count'] + \
                                 self.del_info['.chk']['count'] + self.del_info['.xlk']['count'] + self.del_info['.bak']['count']
        print('总共可删除%s个文件,删除可节省:%s 空间' % (self.del_all_files_num,self.FormatSize(top)))
        self.LaJiQingLi_show.Show_Msg_WeChat(top,('总共可删除%s个文件,删除可节省:%s 空间' % (self.del_all_files_num,self.FormatSize(top))), 1)
    def Delete_Files_Method(self,top):
        if self.del_file_paths:
            for i in self.del_file_paths:
                print('正在删除%s 文件或目录！' % i)
                self.LaJiQingLi_show.Show_Msg_WeChat(top,('正在删除%s 文件或目录！' % i), 1)
                self.Del_dir_or_file(i,top)
        else:
            print('请先扫描需要清理的文件！')
            self.LaJiQingLi_show.Show_Msg_WeChat(top,'请先扫描需要清理的文件！', 1)
        print('删除失败文件：%s' % self.del_faliue_file)
        self.LaJiQingLi_show.Show_Msg_WeChat(top,'请先扫描需要清理的文件！', 1)
class Mails_operate:
    def __init__(self):
        self.inter_other_mails = OtherJobs()
        self.other_job_log_mail_operate = Logs()
        self.mails_enclosure_text_contents = []
        self.mails_tips_enclosure = ''
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
            get_login_state_yeah = self.inter_other_mails.Get_Config_Info('element_xpath','get_login_state_yeah')
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
                    dr.find_element_by_xpath(get_login_state_yeah).click()
                    time.sleep(0.5)
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
    def ChoiseMails_Files_Method(self,top,text):
        self.mails_enclosure_text_contents = []
        selectFiles = tk.filedialog.askopenfilenames(title='可选择1个或多个文件')  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
        for selectFile in selectFiles:
            text.insert(tk.END, selectFile + '\n')  # 更新text中内容
            text.update()
        mails_text_contents = text.get('0.0', 'end').split('\n')[0:-2]
        self.mails_enclosure_text_contents = mails_text_contents
        print(self.mails_enclosure_text_contents)
    def Send_mails_Fun_Method(self,top,send_mail_userinfos,to_username_f,subject_f,contents_f,type,mail_enclosure_addr_f):
        #判断选择是否正确
        att_filename = []
        mail_addr_type = ''
        def send_mail(from_username,from_passwd,smtp_server_addr,smtp_server_port,to_username,alert_info,detail_info,file_enclosure):
            msgRoot = MIMEMultipart('related')
            # 主题
            msgRoot['Subject'] = Header(alert_info, 'utf-8')
            # 构造附件
            for file_path_addr in file_enclosure:
                file_name = file_path_addr.split('\\')[-1]
                print(file_name)
                file_name = MIMEText(open(file_path_addr, 'rb').read(), 'base64', 'utf-8')
                att_filename.append(file_name)
            txt = email.mime.text.MIMEText(detail_info)
            msgRoot['From'] = from_username
            msgRoot['To'] = ','.join(to_username)  # Header("所有人", 'utf-8')
            for att in att_filename:
                att['Content-Type'] = 'application/octet-stream'
                att['Content-Disposition'] = 'attachment;filename =' + str(att)
                msgRoot.attach(att)
            msgRoot.attach(txt)
            smtp = smtplib.SMTP()
            smtp.connect(smtp_server_addr,smtp_server_port)
            smtp.login(from_username, from_passwd)
            smtp.sendmail(from_username,to_username, msgRoot.as_string())
            smtp.quit()
            tips_send_mail_content = '邮件：' + alert_info + '发送成功！'
            print(tips_send_mail_content)
        global smtp_server_addr_f, smtp_server_port_f,from_username_f,from_passwd_f
        if int(send_mail_userinfos) == 1:
            from_username_f = self.inter_other_mails.Get_Config_Info('mails_login_info_client','user_login_yeah_houtian').split(',')[0]
            from_passwd_f = self.inter_other_mails.Get_Config_Info('mails_login_info_client','user_login_yeah_houtian').split(',')[-1]
            smtp_server_addr_f = self.inter_other_mails.Get_Config_Info('mails_info', 'yeah_smtp_server_addr')  #
            smtp_server_port_f = self.inter_other_mails.Get_Config_Info('mails_info', 'yeah_smtp_server_port')
            mail_addr_type = 'yeah'
        elif int(send_mail_userinfos) == 2:
            from_username_f = self.inter_other_mails.Get_Config_Info('mails_login_info_client', 'user_login_126_weiyu').split(',')[0]
            from_passwd_f = self.inter_other_mails.Get_Config_Info('mails_login_info_client', 'user_login_126_weiyu').split(',')[-1]
            smtp_server_addr_f = self.inter_other_mails.Get_Config_Info('mails_info', '126_smtp_server_addr')  #
            smtp_server_port_f = self.inter_other_mails.Get_Config_Info('mails_info', '126_smtp_server_port')
            mail_addr_type = '126'
        elif int(send_mail_userinfos) == 3:
            from_username_f = self.inter_other_mails.Get_Config_Info('mails_login_info_client', 'user_login_qq_719').split(',')[0]
            from_passwd_f = self.inter_other_mails.Get_Config_Info('mails_login_info_client', 'user_login_qq_719').split(',')[-1]
            # from_passwd_f = 'jafkuwbbyaxfbbgh'
            smtp_server_addr_f = self.inter_other_mails.Get_Config_Info('mails_info', 'qq_smtp_server_addr')  #
            smtp_server_port_f = self.inter_other_mails.Get_Config_Info('mails_info', 'qq_smtp_server_port')
            mail_addr_type = 'qq'
        if not mail_enclosure_addr_f and not self.mails_enclosure_text_contents:
            self.mails_tips_enclosure = '未选择附件，请确认！'
            print(self.mails_tips_enclosure)
        elif not mail_enclosure_addr_f and self.mails_enclosure_text_contents:
            self.mails_tips_enclosure = str(self.mails_enclosure_text_contents).split('[[')[-1].split(']]')[0]

        elif mail_enclosure_addr_f and not self.mails_enclosure_text_contents:
            self.mails_tips_enclosure = str(mail_enclosure_addr_f)
            self.mails_enclosure_text_contents.append(mail_enclosure_addr_f)
        else:
            self.mails_tips_enclosure = "'" + str(mail_enclosure_addr_f) + "'," + str(self.mails_enclosure_text_contents).split('[[')[-1].split(']]')[0]
            self.mails_enclosure_text_contents.append(mail_enclosure_addr_f)
        self.mails_enclosure_text_contents= list(set(self.mails_enclosure_text_contents))
        if int(type) == 0:
            tips_msg = '请确认：此封' + mail_addr_type + '邮件发件人：' + from_username_f + '，收件人：' + to_username_f + '，主题：' + subject_f + '，邮件正文内容：' + contents_f + '，附件：<' + self.mails_tips_enclosure + '>。'
            print(tips_msg)
        else:
            send_mail(from_username_f, from_passwd_f, smtp_server_addr_f, smtp_server_port_f, to_username_f,subject_f, contents_f, mail_enclosure_addr_f)
class Resource_Monitor:
    def __init__(self):
        self.resource_monitor = OtherJobs()
        self.other_job_log_rm = Logs()
        self.overall_RM = OverAll()
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
    def Get_Unreadmails_Num(self,type):
        cookies_file_path_all = ''
        yeah_url = ''
        element_xpath_get_unread_num = ''
        if int(type) == 1:
            cookies_file_path = self.resource_monitor.Get_Config_Info('file_name', 'save_cookies_path')  #
            cookies_file_path_all = os.path.dirname(os.path.dirname(__file__))+ cookies_file_path + '_yeah'
            yeah_url = self.resource_monitor.Get_Config_Info('mails_info', 'yeah_mail_url')  #
            element_xpath_get_unread_num = self.resource_monitor.Get_Config_Info('element_xpath', 'unread_mails_yeah')  #
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        dr = webdriver.Chrome(chrome_options=chrome_options)
        #dr = webdriver.Chrome()
        status = self.resource_monitor.Save_Cookies(dr,cookies_file_path_all, yeah_url)
        time.sleep(0.1)
        if status:
            dr = webdriver.Chrome(chrome_options=chrome_options)
            #dr = webdriver.Chrome()
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
            dr.close()
            self.other_job_log_rm.LogsSave(cookies_noused)
            os.remove(cookies_file_path_all)
            self.Get_Unreadmails_Num()
        else:
            cookies_url = dr.current_url
            sid = cookies_url.split('=')[1].split('#')[0]
            cookies_url = 'https://mail.yeah.net/js6/s?sid=' + sid + '&func=mbox:listMessages&YxInboxBottomShow=deptId=1|projectId=117&mbox_title_unread=folder'
            dr.get(cookies_url)
            time.sleep(0.5)
            dictCookies = dr.get_cookies()
            #转换ccokies
            cookie = [item["name"] + "=" + item["value"] for item in dictCookies]
            cookiestr = ';'.join(item for item in cookie)
            unread_mails_num = self.Get_Unreadmails_infos(cookies_url,cookiestr)
            time.sleep(0.1)
            dr.close()
        return unread_mails_num
    def Get_Unreadmails_infos(self,url,cookies):
        data = {'var': '<?xml version="1.0"?><object><array name="fids"><int>1</int></array><object name="filter"><object name=\
        "flags"><boolean name="read">false</boolean></object></object><string name="order">date</string><boolean name="desc">true\
        </boolean><int name="limit">20</int><int name="start">0</int><boolean name="skipLockedFolders">false</boolean><boolean name=\
        "returnTag">true</boolean><boolean name="returnTotal">true</boolean></object>'}
        header = {'Accept': 'text/javascript','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh;q=0.9','Connection': 'keep-alive',
                    'Content-Length': '663',
                    'Content-type': 'application/x-www-form-urlencoded',
                    'Cookie':cookies,
                    'Host': 'mail.yeah.net',
                    'Origin': 'https://mail.yeah.net',
                    'Referer': "https://mail.yeah.net/js6/main.jsp?sid=hAbVnMNKwbXeJAJQlJKKneHIwMiMPFrq&df=mail163_letter",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        unread_info_all = []
        unread_mails_from = ''
        unread_mails_subject = ''
        sendtime = ''
        timeOut = 10
        r = requests.post(url,data=data,headers=header,timeout=timeOut,allow_redirects=True, verify=False)
        res = r.content.decode('utf-8')
        res_lists = res.split('\'var\':')[-1].split('},\n{')
        for res_list_every in res_lists:
            if 'from' in res_list_every:
                unread_mails_from = res_list_every.split('\n')[4].split(':')[-1].split('\'')[1]
            if 'subject' in res_list_every:
                unread_mails_subject = res_list_every.split('\n')[6].split(':')[-1].split('\'')[1]
            if 'sentDate' in res_list_every:
                sendtime = res_list_every.split('\n')[7].split(':')[-1].split('(')[-1].split('),')[0].replace(',',':')
            unread_info_dic = {'发件人':unread_mails_from,'主题':unread_mails_subject,'发件时间':sendtime}
            unread_info_all.append(unread_info_dic)
        print(unread_info_all)
        self.overall_RM.set_unread_mails_info_value(unread_info_all,0)
        unread_mails_num_show = 'houtian_yu@yeah.com的未读邮件：' + str(len(unread_info_all)) + '条。'
        return unread_mails_num_show
    def Get_Resource_Monitor_System_Result(self,top,type_resouce):
        proc_mem_percent, cmdlines, cpu_percent = '', '', ''
        proc, all_processes = [], psutil.process_iter()
        for items in all_processes:
            try:
                procinfo = items.as_dict(attrs=["pid", "name"])
                try:
                    # the process start path
                    p_path_cwd = items.cwd().encode('utf-8')
                    # p_path_cwd = items.exe()
                    # the process accounts for system memory uasge
                    proc_mem_percent = items.memory_percent()
                    # the process starts cmdline content
                    cmdlines = str(items.cmdline())
                    # the process accounts for system CPU usage
                    cpu_percent = items.cpu_percent(interval=1)
                except Exception as e:
                    # print(e)
                    try:
                        p_path_cwd = items.exe()
                    except Exception as e:
                        p_path_cwd = e.name
                p_status, p_create_time, proc_user, proc_io_info = items.status(), items.create_time(), items.username(), {}
                try:
                    proc_io = items.io_counters()
                    proc_io_info["ReadCount"] = proc_io.read_count
                    proc_io_info["WriteCount"] = proc_io.write_count
                    proc_io_info["ReadBytes"] = proc_io.read_bytes
                    proc_io_info["WriteBytes"] = proc_io.write_bytes
                except Exception as e:
                    pass
                procinfo.update({"path": p_path_cwd,
                                 "cmdline": cmdlines,
                                 "cpu_percent": cpu_percent,
                                 "status": p_status,
                                 "CreateTime": p_create_time,
                                 "MemPercent": proc_mem_percent,
                                 "user": proc_user,
                                 "DiskIo": proc_io_info})
            except Exception as e:
                pass
            finally:
                proc.append(procinfo)
        cpuhigh_percent_data, Memhigh_Percent_data = [], []
        for proc_list in proc:
            try:
                if float(proc_list['cpu_percent']) >= 5.0:
                    cpuhigh_percent_data.append(proc_list)
            except Exception as msg:
                pass
            try:
                if float(proc_list['MemPercent']) >= 1.2:
                    Memhigh_Percent_data.append(proc_list)
            except Exception as msg:
                pass
        text_listbox = ''
        if int(type_resouce) == 0:
            text_listbox = self.resource_monitor.Show_Result_Lists(top,Memhigh_Percent_data,1,len(Memhigh_Percent_data),1,10)
        elif int(type_resouce) == 1:
            text_listbox = self.resource_monitor.Show_Result_Lists(top,cpuhigh_percent_data,1,len(cpuhigh_percent_data),2,10)
        return text_listbox
    def Get_Resource_Monitor_content(self,top,listbox):
        num_list = listbox.curselection()
        for num in num_list:
            userhigh_info = listbox.get(num)[1:]
            program_name = userhigh_info.split(',')[1].split(':')[-1]
            self.resource_monitor.Stop_Exe_Program(program_name)