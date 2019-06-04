from tkinter import *
from OtherJobs.otherJob import OtherJobs
from FunctionCall.functionCall import FunctionCall
from OverAll.overAll import OverAll
class MainGui:
    def __init__(self):
        self.list_var = []
        self.root = Tk()
        self.otherJob = OtherJobs(self.root)
        self.functioncall = FunctionCall()
        self.overall = OverAll()
    def oneGui(self):
        self.root.title('HoutianTools_v1.0')
        width=850
        height=330
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - 150)
        self.root.geometry(alignstr)
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.root.resizable(width=True, height=True)
        self.frame_v= [[0,'v_baidu','frame_baidu'],[1,'v_files','frame_files'],[2,'v_search','frame_search'],[3,'v_weixin','frame_weixin'],\
                     [4,'v_kugou','frame_kugou'],[5,'v_garbage','frame_garbage'],[6,['v_mails_login_user','v_mails_login_passwd',
                     'v_mails_types'],'frame_mails'],[7,'v_monitor','frame_monitor'],[8,'v_websuit','frame_websuit'],[9,'v_show','frame_show']]
        for value in self.frame_v:
            if value[0] == 6:
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
        Label(self.frame_v[3][2], text="请点击后登陆微信！", width=16,bg='LightYellow',justify = LEFT).grid(padx=5,row=3, column=0,columnspan=2, sticky=W)
        Checkbutton(self.frame_v[3][2], text='默认登陆(后天)', width=14,variable=self.frame_v[3][1],bg='LightYellow',justify = LEFT).grid(padx=1,row=3,column=2,columnspan=2,sticky=W)
        Button(self.frame_v[3][2], text="开始登陆", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.LoginWechat)). \
            grid(padx=1,row=3, column=7, sticky=W)
        #酷狗
        Label(self.frame_v[4][2], text="音乐名称:", width=8,bg='LightYellow',justify = LEFT).grid(padx=5,row=4, column=0, sticky=W)
        Entry(self.frame_v[4][2], width=15, textvariable=self.frame_v[4][1],justify = LEFT).grid(padx=1,row=4, column=1, columnspan=2,sticky=W)
        Button(self.frame_v[4][2], text="播放", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic)). \
            grid(padx=1,row=4, column=7, sticky=W)
        #垃圾清理
        Label(self.frame_v[5][2], text="默认360垃圾清理！", width=16,bg='LightYellow',justify = LEFT).grid(padx=5,row=5, column=0,columnspan=2,sticky=W)
        Button(self.frame_v[5][2], text="开始清理", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Garbage_Clear)). \
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
        Button(self.frame_v[6][2], text="登录", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.LoginEmail)). \
            grid(padx=1,row=6, column=7, sticky=W)
        #磁盘、内存、CPU、邮件
        Button(self.frame_v[7][2], text="磁盘占用", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Disk_Used)). \
            grid(padx=1, row=7, column=0, sticky=W)
        Button(self.frame_v[7][2], text="CPU占用", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Cpu_Used)). \
            grid(padx=1, row=7, column=1, sticky=W)
        Button(self.frame_v[7][2], text="内存占用", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Mem_Used)). \
            grid(padx=1, row=7, column=2, sticky=W)
        Button(self.frame_v[7][2], text="未读邮件", state='normal', width=8,bg='PowderBlue',command=lambda: self.otherJob.thread_add(self.functioncall.Mails_Unread)). \
            grid(padx=1, row=7, column=3, sticky=W)
        Button(self.frame_v[7][2], text="启动监控", state='normal', width=8,bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Up_Monitor)). \
            grid(padx=1, row=7, column=7, sticky=W)
        #常用网站
        website_member = Menubutton(self.frame_v[8][2],text='»选择访问的网站',relief=GROOVE,bg='LightYellow',activebackground='Bisque',justify=LEFT)
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
            grid(padx=1,row=8,column=7,sticky=W)
        #初始化配置
        Button(self.frame_v[9][2], text='INIT', state='normal', width=8, bg='LightGreen',command=lambda: self.otherJob.thread_add(self.functioncall.Init_Config)). \
            grid(padx=1, row=9, column=7, sticky=NW)
        mainloop()

if __name__ == '__main__':

    houtian = MainGui()
    houtian.oneGui()