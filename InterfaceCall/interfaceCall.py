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
import urllib,subprocess,itchat
from itchat.content import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import requests
import tkinter.messagebox
from lxml import etree
from urllib.request import urlretrieve
from tkinter.filedialog import askdirectory
import json,mp3play
import requests,urllib.request,json
import mp3play
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
        textlabel = Message(top, textvariable=v_monitor, justify=LEFT, width=347, font=("华康少女字体", 10),fg="red")
        textlabel.grid(padx=5, pady=1, row=row, column=0, columnspan=3, sticky=W)
    def LoginWeChat_Sweepcode_Method(self,num,top):
        def close_QR_img():
            hld_QR = win32gui.FindWindow('Windows.UI.Core.CoreWindow', None)
            print(hld_QR)
            win32gui.SendMessage(hld_QR, win32con.WM_CLOSE, 0, 0)
            #creat_time_2 = os.path.getctime(wechat_qr_path)
            #print(wechat_qr_path)
            #if creat_time_1 != creat_time_2:
            #render = PhotoImage(file=wechat_qr_path)
            #img = Label(top, image=render)
            #img.grid(padx=1, pady=5, row=1, column=1, columnspan=3, sticky=W)
            userinfo = itchat.web_init()
            print('登陆完成！账号为：%s!' % userinfo['User']['NickName'])
            self.Show_Msg_WeChat(top,('登陆完成！账号为：%s!' % userinfo['User']['NickName']),1)
        def loginout_img():
            print('已退出登录！')
            self.Show_Msg_WeChat(top, '登陆完成！', 1)
        if not num or int(num) == 1:
            value = True
        else:
            value = False
        #wechat_qr_path = os.path.dirname(os.path.dirname(__file__)) + '\\GuiDisplay\\QR.png'
        #creat_time_1 = os.path.getctime(wechat_qr_path)
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
                    Send_contents = unicode(Send_contents,'utf-8')
                    send_files(Send_contents)
                    print('%s文件发送成功！' % Send_contents.split('/')[-1])
                if self.text_contents:
                    for text in self.text_contents:
                        send_files(text)
                        print('%s文件发送成功！' % text.split('/')[-1])
            else:
                print('联系人昵称不存在')
                self.Show_Msg_WeChat(top, '联系人昵称不存在', 4)
    def ChoiseWeChat_Files_Method(self,top,text):
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
        kugou_music_path = self.inter_other_kugou.Get_Config_Info('file_name','kugou_music_path')
        if type == 0:
            win32process.CreateProcess(kugou_music_path, '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None,win32process.STARTUPINFO())
            time.sleep(2)
            self.inter_other_kugou.mouse_input_remote_on([18,116])
            self.inter_other_kugou.mouse_input_remote_up([18,116])
            global status
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
                                        mp3_name1 = text_music.get(0)[3:]
                                        print('当前%s是第一首歌，无法进行上一曲！' % mp3_name1)
                                        self.Show_Msg_Kugou_Music(top,('当前%s是第一首歌，无法进行上一曲！' % mp3_name1), 3)
                                        num_cu = num
                                    else:
                                        num_cu = num - 1
                                else:
                                    if num == 29:
                                        mp3_name1 = text_music.get(29)[3:]
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
                start_music(0)
            def next_music():
                driver.close()
                self.music_status = 2
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
