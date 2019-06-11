from tkinter import *
from OtherJobs.otherJob import OtherJobs
from FunctionCall.functionCall import FunctionCall
from OverAll.overAll import OverAll
import time
class MainGui:
    def __init__(self):
        self.list_var = []
        self.root = Tk()
        self.otherJob = OtherJobs(self.root)
        self.functioncall = FunctionCall()
        self.overall = OverAll()
        self.wechat_mails_web_contents = [[0,'v_Contacts'], [1,'v_Contacts_m', 'v_send_content'], [2,'v_Contacts_f', 'v_file_path'],[3,'v_Contacts_num'],\
                                [4,'v_Contacts_get'],[5,'v_mail_subject'],[6,'v_contents'],[7,'v_enclosure'],[8,'v_receive_addr']]
        for input_ss in self.wechat_mails_web_contents:
            if len(input_ss) == 3:
                input_ss[1] = StringVar()
                input_ss[2] = StringVar()
                self.overall.set_wechat_info([input_ss[1], input_ss[2]])
            else:
                input_ss[1] = StringVar()
                self.overall.set_wechat_info(input_ss[1])
    def MainPageGui(self):
        self.root.title('HoutianTools_v1.0')
        width=850
        height=330
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2 - 180, (screenheight - height) / 2 - 100)
        self.root.geometry(alignstr)
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.root.resizable(width=True, height=True)
        self.frame_v= [[0,'v_baidu','frame_baidu'],[1,'v_files','frame_files'],[2,'v_search','frame_search'],[3,['v_weixin_login','v_weixin_web'],'frame_weixin'],\
                     [4,'v_kugou','frame_kugou'],[5,'v_garbage','frame_garbage'],[6,['v_mails_login_user','v_mails_login_passwd',
                     'v_mails_types'],'frame_mails'],[7,'v_monitor','frame_monitor'],[8,'v_websuit','frame_websuit'],[9,'v_show','frame_show']]
        for value in self.frame_v:
            if value[0] == 3:
                value[1][0] = StringVar()
                value[1][1] = IntVar()
                self.overall.set_value([value[1][0], value[1][1]])
            elif value[0] == 6:
                value[1][0] = StringVar()
                value[1][1] = StringVar()
                value[1][2] = IntVar()
                value[1][2].set(1)
                self.overall.set_value([value[1][0],value[1][1],value[1][2]])
            else:
                value[1]= StringVar()
                self.overall.set_value(value[1])
            if value[0] == 9:
                value[2] = Frame(self.root, height=60, relief="ridge", bd=1, width=850, bg='SkyBlue').grid(padx=1,row=value[0],column=0,columnspan=8,sticky=W)
            else:
                value[2] = Frame(self.root,height=30,relief="ridge", bd=1,width=850,bg='SkyBlue').grid(padx=1,row=value[0],column=0,columnspan=8,sticky=W)
        #百度
        Entry(self.frame_v[0][2],width=80,textvariable=self.frame_v[0][1],justify = LEFT).grid(padx=5,row=0,column=0,columnspan=5,sticky=W)
        Button(self.frame_v[0][2],text="手动搜索",state='normal',width=8,bg='LightGreen',command=lambda:self.otherJob.thread_add(self.functioncall.BaiduSearch)).\
            grid(padx=1,row=0,column=7,sticky=W)
        Button(self.frame_v[0][2], text="自动搜索", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.BaiduSearch_Auto)). \
            grid(padx=1, row=0, column=6, sticky=W)
        #打开文件
        Label(self.frame_v[1][2],text="文件路径:",width=8,bg='LightYellow',justify = LEFT).grid(padx=5,row=1,column=0,sticky=W)
        Entry(self.frame_v[1][2],width=45,textvariable=self.frame_v[1][1],justify = LEFT).grid(padx=1,row=1,column=1,columnspan=3,sticky=W)
        Label(self.frame_v[1][2], text="eg: D:/Python/test.txt",bg='LightYellow',justify = LEFT).grid(padx=1, row=1, column=4, columnspan=3,sticky=W)
        Button(self.frame_v[1][2],text="打开文件",state='normal',width=8,bg='LightGreen',command=lambda:self.otherJob.thread_add(self.functioncall.OpenFiles)).\
            grid(padx=1,row=1,column=7,sticky=W)
        Button(self.frame_v[1][2], text="打开目录", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.OpenDirWindows)). \
            grid(padx=1, row=1, column=6, sticky=W)
        #本地搜索
        Label(self.frame_v[2][2], text="文件名称:", width=8,bg='LightYellow',justify = LEFT).grid(padx=5,row=2, column=0, sticky=W)
        Entry(self.frame_v[2][2],width=30,textvariable=self.frame_v[2][1],justify = LEFT).grid(padx=1,row=2,column=1,columnspan=2,sticky=W)
        Button(self.frame_v[2][2],text="本地搜索",state='normal',width=8,bg='LightGreen',command=lambda:self.otherJob.thread_add(self.functioncall.SearchFiles)).\
            grid(padx=1,row=2,column=7,sticky=W)
        #微信
        Label(self.frame_v[3][2], text="请点击登陆微信！", width=14,bg='LightYellow',justify = LEFT).grid(padx=5,row=3, column=0,columnspan=2, sticky=W)
        Checkbutton(self.frame_v[3][2], text='默认登陆(后天)', width=14,variable=self.frame_v[3][1][0],bg='LightYellow',justify = LEFT).grid(padx=1,row=3,column=2,columnspan=2,sticky=W)
        Button(self.frame_v[3][2], text="客户端登录", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.LoginWechat)). \
            grid(padx=1, row=3, column=7, sticky=W)
        wechat_member = Menubutton(self.frame_v[3][2], text='»微信交互', relief=RAISED, bg='LightGreen',activebackground='Bisque', justify=LEFT)
        wechat_member.grid(padx=1, row=3, column=6,sticky=W)
        wechat_menu = Menu(wechat_member, tearoff=False)
        wechat_menu.add_radiobutton(label='登录微信', variable=self.frame_v[3][1][1], selectcolor="Crimson",activebackground='Pink',command=lambda: self.otherJob.thread_add(self.LoginWeChatGui),value=1)
        wechat_menu.add_radiobutton(label='搜索联系人', variable=self.frame_v[3][1][1], selectcolor="Crimson",activebackground='Pink', command=lambda: self.otherJob.thread_add(self.SearchWeChatContacts),value=2)
        wechat_menu.add_radiobutton(label='发送消息', variable=self.frame_v[3][1][1], selectcolor="Crimson",activebackground='Pink', command=lambda: self.otherJob.thread_add(self.SendWeChatMessages),value=3)
        wechat_menu.add_radiobutton(label='发送文件', variable=self.frame_v[3][1][1], selectcolor="Crimson",activebackground='Pink', command=lambda: self.otherJob.thread_add(self.SendWeChatFiles),value=4)
        wechat_menu.add_radiobutton(label='获取消息', variable=self.frame_v[3][1][1], selectcolor="Crimson",activebackground='Pink',command=lambda: self.otherJob.thread_add(self.GetWeChatMessages), value=6)
        wechat_member.config(menu=wechat_menu)
        #酷狗
        Label(self.frame_v[4][2], text="酷狗音乐:", width=8,bg='LightYellow',justify = LEFT).grid(padx=5,row=4, column=0, sticky=W)
        #Entry(self.frame_v[4][2], width=15, textvariable=self.frame_v[4][1],justify = LEFT).grid(padx=1,row=4, column=1, columnspan=2,sticky=W)
        Button(self.frame_v[4][2], text="播放/暂停", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic,0)). \
            grid(padx=1,row=4, column=1, sticky=W)
        Button(self.frame_v[4][2], text="上一曲", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic,1)). \
            grid(padx=1, row=4, column=2, sticky=W)
        Button(self.frame_v[4][2], text="下一曲", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic,2)). \
            grid(padx=1, row=4, column=3, sticky=W)
        Button(self.frame_v[4][2], text="增大音量", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic,3)). \
            grid(padx=1, row=4, column=4, sticky=W)
        Button(self.frame_v[4][2], text="减小音量", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic,4)). \
            grid(padx=1, row=4, column=5, sticky=W)
        Button(self.frame_v[4][2], text="下载", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic,5)). \
            grid(padx=1, row=4, column=6, sticky=W)
        Button(self.frame_v[4][2], text="更多", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.PlayMusicMore)). \
            grid(padx=1, row=4, column=7, sticky=W)
        #垃圾清理
        Label(self.frame_v[5][2], text="默认360垃圾清理！", width=15,bg='LightYellow',justify = LEFT).grid(padx=5,row=5, column=0,columnspan=2,sticky=W)
        Button(self.frame_v[5][2], text="开启360", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Garbage_Clear)). \
            grid(padx=1, row=5, column=1, sticky=N+S)
        Button(self.frame_v[5][2], text="手动清理", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.Garbage_Clear_Ui)). \
            grid(padx=1,row=5, column=7, sticky=W)
        #登录邮件
        Label(self.frame_v[6][2], text="用户名称:", width=8,bg='LightYellow',justify = LEFT).grid(padx=5,row=6, column=0, sticky=W)
        login_user = Entry(self.frame_v[6][2], width=20, textvariable=self.frame_v[6][1][0],justify = LEFT)
        login_user.insert(END,'houtian_yu@yeah.net')
        login_user.grid(padx=1,row=6, column=1,columnspan=1,sticky=W)
        Label(self.frame_v[6][2], text="密码:", width=5,bg='LightYellow',justify = LEFT).grid(padx=1,row=6, column=2, sticky=W)
        login_passwd = Entry(self.frame_v[6][2], width=12, textvariable=self.frame_v[6][1][1],show='*',justify = LEFT)
        login_passwd.insert(END, 'yulei927623')
        login_passwd.grid(padx=1,row=6, column=3, sticky=W)
        member = Menubutton(self.frame_v[6][2],text="︾选择邮箱︾",relief=GROOVE,bg='LightYellow',activebackground='Bisque',justify = LEFT)
        member.grid(padx=1,row=6, column=4, sticky=W)
        mailmenu = Menu(member, tearoff=False)
        mailmenu.add_radiobutton(label="Yeah",variable=self.frame_v[6][1][2],selectcolor="Crimson",activebackground='Pink',value=1)
        mailmenu.add_radiobutton(label="126",variable=self.frame_v[6][1][2], selectcolor="Crimson",activebackground='Pink',value=2)
        mailmenu.add_radiobutton(label="QQ",variable=self.frame_v[6][1][2], selectcolor="Crimson",activebackground='Pink',value=3)
        member.config(menu=mailmenu)
        Button(self.frame_v[2][2],text='发送邮件',state='normal',width=8,bg='LightGreen',command=lambda:self.otherJob.thread_add(self.Mails_Operate_More)).\
            grid(padx=1,row=6,column=6,sticky=W)
        Button(self.frame_v[6][2], text="Web登陆", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.LoginEmail)). \
            grid(padx=1,row=6, column=7, sticky=W)
        #磁盘、内存、CPU、邮件
        Button(self.frame_v[7][2], text="磁盘占用", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Disk_Used)). \
            grid(padx=5, row=7, column=0, sticky=W)
        Button(self.frame_v[7][2], text="CPU占用", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Cpu_Used)). \
            grid(padx=1, row=7, column=1, sticky=W)
        Button(self.frame_v[7][2], text="内存占用", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Mem_Used)). \
            grid(padx=1, row=7, column=2, sticky=W)
        Button(self.frame_v[7][2], text="未读邮件", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Mails_Unread)). \
            grid(padx=1, row=7, column=3, sticky=W)
        Button(self.frame_v[7][2], text="启动监控", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Up_Monitor)). \
            grid(padx=1, row=7, column=7, sticky=W)
        #常用网站
        website_member = Menubutton(self.frame_v[8][2],text='»选择访问的网站',relief=RAISED,bg='LightYellow',activebackground='Bisque',justify=LEFT)
        website_member.grid(padx=5,row=8, column=0,columnspan=2,sticky=W)
        website_menu = Menu(website_member,tearoff=False)
        website_menu.add_radiobutton(label='后天博客',variable=self.frame_v[8][1],selectcolor="Crimson",activebackground='Pink',value=1)
        website_menu.add_radiobutton(label='哔哩哔哩',variable=self.frame_v[8][1],selectcolor="Crimson",activebackground='Pink',value=2)
        website_menu.add_radiobutton(label='简学消防',variable=self.frame_v[8][1],selectcolor="Crimson",activebackground='Pink',value=3)
        website_menu.add_radiobutton(label='慕课网',variable=self.frame_v[8][1],selectcolor="Crimson",activebackground='Pink',value=4)
        website_menu.add_radiobutton(label='GitHub',variable=self.frame_v[8][1],selectcolor="Crimson",activebackground='Pink',value=5)
        website_menu.add_radiobutton(label='百度翻译',variable=self.frame_v[8][1],selectcolor="Crimson",activebackground='Pink',value=6)
        website_member.config(menu=website_menu)
        Button(self.frame_v[8][2],text='打开网站',state='normal',width=8,bg='LightGreen',command=lambda:self.otherJob.thread_add(self.functioncall.Open_Websit)).\
            grid(padx=1,row=8,column=7,sticky=W)#functioncall.Open_Websit
        #初始化配置
        Button(self.frame_v[9][2], text='INIT', state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Init_Config)). \
            grid(padx=1, row=9, column=7, sticky=NW)
        mainloop()
    def getvalru(self):#测试使用
        print(self.wechat_mails_web_contents[0])
        aa = self.wechat_mails_web_contents[0][1].get()
        print(aa)
        print('qqqq')
    def SecondGui(self,title,height=330):
        self.second_gui = Toplevel(bg='LightYellow')
        self.second_gui.title(title)
        width = 350
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2 + 420 , (screenheight - height) / 2 - 100)
        self.second_gui.geometry(alignstr)
    def CloseToplevel(self):
        self.second_gui.destroy()
    def LoginWeChatGui(self):
        self.SecondGui('登录微信')
        Button(self.second_gui, text='登录微信', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.LoginWeChat_Sweepcode,self.second_gui)). \
            grid(padx=10,pady=20,row=0,column=0, sticky=W)
        Button(self.second_gui, text='注销当前账号', width=10, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.CancelWeChat_LoginOut, self.second_gui)). \
            grid(padx=170, pady=20, row=0, column=3, sticky=E)
        #time.sleep(30)
        #self.second_gui.destroy()
    def SearchWeChatContacts(self):
        self.SecondGui('查看联系人')
        Label(self.second_gui, text='输入联系人姓名：',width=13,bg='LightYellow',justify=LEFT).grid(padx=5,pady=10,row=0,column=0,sticky=W)
        Entry(self.second_gui,width=22,textvariable=self.wechat_mails_web_contents[0][1],justify=LEFT).grid(padx=1,pady=10,row=0,column=1,sticky=W)
        Button(self.second_gui,text='查找',width=8,state='normal',bg='LightGreen',command=lambda :self.otherJob.thread_add(self.functioncall.SearchWeChat_Contacts,self.second_gui)).\
            grid(padx=8,pady=10,row=0,column=2,sticky=W)
        # functioncall.SearchWeChat_Contacts
        Button(self.second_gui, text='发送消息', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.SendWeChatMessages)). \
            grid(padx=5, pady=10,row=1, column=0,sticky=W)
        Button(self.second_gui, text='发送文件', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.SendWeChatFiles)). \
            grid(padx=8, pady=10,row=1, column=2,sticky=W)
    def SendWeChatMessages(self):
        self.SecondGui('发送消息')
        Label(self.second_gui, text='输入联系人姓名：', width=13, bg='LightYellow', justify=LEFT).grid(padx=5, pady=10, row=0,column=0, sticky=W)
        Entry(self.second_gui, width=22, textvariable=self.wechat_mails_web_contents[1][1], justify=LEFT).grid(padx=1, pady=10, row=0,column=1, sticky=W)
        Label(self.second_gui, text='输入发送的内容：', width=13, bg='LightYellow', justify=LEFT).grid(padx=5, pady=10, row=1,column=0, sticky=W)
        Entry(self.second_gui, width=40, textvariable=self.wechat_mails_web_contents[1][2], justify=LEFT).grid(padx=5, pady=10, row=2,column=0, columnspan=3,sticky=W)
        Button(self.second_gui, text='发送消息', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.SendWeChat_Messages,self.second_gui)). \
            grid(padx=5, row=3, pady=10,column=0, sticky=W)
    def SendWeChatFiles(self):
        self.SecondGui('发送文件')
        Label(self.second_gui, text='输入联系人姓名：', width=13, bg='LightYellow', justify=LEFT).grid(padx=5, pady=10, row=0,column=0, sticky=W)
        Entry(self.second_gui, width=22, textvariable=self.wechat_mails_web_contents[2][1], justify=LEFT).grid(padx=1, pady=10, row=0,column=1, sticky=W)
        upload_files = Text(self.second_gui, width=30,height=5)
        upload_files.grid(padx=1, row=1, column=1,columnspan=2, sticky=W)
        Button(self.second_gui, text='选择文件', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.ChoiseWeChat_Files,self.second_gui,upload_files)). \
            grid(padx=5, row=1, pady=10, column=0, sticky=W)
        Label(self.second_gui, text='输入发送文件的路径：', width=17, bg='LightYellow', justify=LEFT).grid(padx=5, pady=10, row=2,column=0, columnspan=2,sticky=W)
        Entry(self.second_gui, width=40, textvariable=self.wechat_mails_web_contents[2][2], justify=LEFT).grid(padx=5, pady=5, row=3,column=0, columnspan=3,sticky=W)
        Label(self.second_gui, text='eg:D:\python\python.exe', width=20, bg='LightYellow', justify=LEFT).grid(padx=5, pady=5, row=4,column=1,sticky=W)
        Button(self.second_gui, text='发送文件', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.SendWeChat_Files,self.second_gui)). \
            grid(padx=5, row=4, pady=5, column=0, sticky=W)
    def GetWeChatMessages(self):
        self.SecondGui('获取消息')
        Label(self.second_gui, text='输入联系人姓名：', width=13, bg='LightYellow', justify=LEFT).grid(padx=5, pady=10, row=0,column=0, sticky=W)
        Entry(self.second_gui, width=30, textvariable=self.wechat_mails_web_contents[4][1], justify=LEFT).grid(padx=1, pady=20, row=0,column=1, sticky=W)
        Button(self.second_gui, text='开始获取', width=8, state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.GetWeChat_Messages,0,self.second_gui)).\
            grid(padx=5, row=1, pady=10, column=0, sticky=W)
    #酷狗音乐
    def PlayMusicMore(self):
        self.SecondGui('更多选择')
        Label(self.second_gui, text="音乐名称:", width=7, bg='LightYellow', justify=LEFT).grid(padx=5,pady=2,row=0, column=0,sticky=W)
        Entry(self.second_gui, width=20, textvariable=self.frame_v[4][1],justify = LEFT).grid(padx=1,pady=2,row=0, column=1, columnspan=2,sticky=W)
        text_music = Listbox(self.second_gui, selectmode=BROWSE, font=("Consolas", 10), width=47, height=12)
        text_music.grid(padx=5,pady=2,row=2, column=0,columnspan=7)
        Button(self.second_gui,width=4,text='搜索',state='normal',bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More,self.second_gui,text_music,0)).\
            grid(padx=3,pady=2,row=0,column=3,sticky=W)
        Button(self.second_gui, width=4, text='播放', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More,self.second_gui,text_music,1)). \
            grid(padx=3, pady=2, row=0, column=4, sticky=W)
        Button(self.second_gui, width=4, text='下载', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui,text_music,2)). \
            grid(padx=3, pady=2, row=0, column=5, sticky=W)
        Button(self.second_gui, width=5, text='上一曲', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui, text_music,7)). \
            grid(padx=5, pady=2, row=1, column=0, sticky=W)
        Button(self.second_gui, width=5, text='下一曲', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui, text_music,8)). \
            grid(padx=1, pady=2, row=1, column=1, sticky=W)
        Button(self.second_gui, width=8, text='清空列表', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui,text_music,3)). \
            grid(padx=1, pady=2, row=1, column=2, sticky=W)
        Button(self.second_gui, width=4, text='暂停', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui, text_music,6)). \
            grid(padx=3, pady=2, row=1, column=3, sticky=W)
        Button(self.second_gui, width=4, text='停止', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui, text_music,5)). \
            grid(padx=3, pady=2, row=1, column=4, sticky=W)
        Button(self.second_gui, width=4, text='帮助', state='normal', bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic_More, self.second_gui,text_music,4)). \
            grid(padx=3, pady=2, row=1, column=5, sticky=W)
    #垃圾清理
    def Garbage_Clear_Ui(self):
        self.SecondGui('垃圾清理')
        Button(self.second_gui, text="开始扫描", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Garbage_Scan,self.second_gui)). \
            grid(padx=5, row=0,pady=10, column=0, sticky=W)
        Button(self.second_gui, text="开使清理", state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Garbage_Delete,self.second_gui)). \
            grid(padx=200,row=0,pady=10,column=1, sticky=W)
    #邮件操作
    def Mails_Operate_More(self):
        self.SecondGui('发送邮件')
        Label(self.second_gui, text="邮件主题:", width=7, bg='LightYellow', justify=LEFT).grid(padx=5, pady=2, row=0,column=0, sticky=W)
        Entry(self.second_gui, width=38, textvariable=self.wechat_mails_web_contents[5][1], justify=LEFT).grid(padx=1, pady=2, row=0,column=1, columnspan=3,sticky=W)
        Label(self.second_gui,text='邮件正文:',width=7,bg='LightYellow',justify=LEFT).grid(padx=5,pady=2,row=1,column=0,sticky=W)
        Entry(self.second_gui, width=47, textvariable=self.wechat_mails_web_contents[6][1]).grid(padx=5, pady=2, row=2,column=0, columnspan=4,sticky=W)
        #contents_mail = Text(self.second_gui, width=47, height=6)
        #contents_mail.grid(padx=5, pady=2,row=2, column=0, columnspan=4, sticky=W)
        upload_files_mail = Text(self.second_gui, width=38, height=2)
        upload_files_mail.grid(padx=1, pady=2,row=3, column=1, columnspan=3, sticky=W)
        Button(self.second_gui,text='选择附件',width=7,state='normal',bg='LightGreen',command=lambda:self.otherJob.thread_add(self.functioncall.ChoiseMails_Files_Fun,self.second_gui,upload_files_mail)).\
            grid(padx=5,pady=2,row=3,column=0,sticky=SW)
        Label(self.second_gui,text="附件路径:",width=7,bg='LightYellow',justify=LEFT).grid(padx=5,pady=2,row=4,column=0,sticky=W)
        Entry(self.second_gui,width=38,textvariable=self.wechat_mails_web_contents[7][1],justify=LEFT).grid(padx=1,pady=2,row=4,column=1,columnspan=3,sticky=W)
        Label(self.second_gui, text="收件地址:", width=7, bg='LightYellow', justify=LEFT).grid(padx=5, pady=2, row=5,column=0, sticky=W)
        Entry(self.second_gui, width=28, textvariable=self.wechat_mails_web_contents[8][1], justify=LEFT).grid(padx=1,pady=2,row=5,column=1,columnspan=2,sticky=W)
        Button(self.second_gui, text='确认', width=7, bg='LightYellow', state='normal',command=lambda: self.otherJob.thread_add(self.functioncall.Send_mails_Fun, self.second_gui,0)). \
            grid(padx=5, pady=2, row=6, column=0, sticky=W)
        Button(self.second_gui,text='发送',width=7,bg='LightYellow',state='normal',command=lambda:self.otherJob.thread_add(self.functioncall.Send_mails_Fun,self.second_gui,1)).\
            grid(padx=215,pady=2,row=6,column=2,sticky=W)



if __name__ == '__main__':

    houtian = MainGui()
    houtian.MainPageGui()