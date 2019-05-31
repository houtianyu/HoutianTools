from tkinter import *
from OtherJobs.otherJob import OtherJobs
from FunctionCall.functionCall import FunctionCall
from OverAll.overAll import OverAll
class MainGui:
    def __init__(self):
        self.list_var = []
        self.root = Tk()
        self.otherJob = OtherJobs()
        self.functioncall = FunctionCall()
        self.overall = OverAll()
    def return_var(self,i):
        return self.list_var[i]
    def oneGui(self):
        self.root.title('HoutianTools')
        self.root.geometry('800x300')
        frame_v= [[0,'v_baidu','frame_baidu'],[1,'v_files','frame_files'],[2,'v_search','frame_search'],[3,'v_weixin','frame_weixin'],\
                     [4,'v_kugou','frame_kugou'],[5,'v_garbage','frame_garbage'],[6,['v_mails_login_user','v_mails_login_passwd','v_mails_types'],'frame_mails']]
        for value in frame_v:
            if value[0] == 6:
                value[1][0] = StringVar()
                value[1][1] = StringVar()
                value[1][2] = IntVar()
                value[1][2].set(1)
                self.overall.set_value([value[1][0],value[1][1],value[1][2]])
            else:
                value[1]= StringVar()
                self.overall.set_value(value[1])
            value[2] = Frame(self.root,height=5,relief=GROOVE).grid(padx=1,row=value[0],column=0,columnspan=8,sticky=W)
        #百度
        Entry(frame_v[0][2],width=80,textvariable=frame_v[0][1],justify = LEFT).grid(padx=5,row=0,column=0,columnspan=5,sticky=W)
        Button(frame_v[0][2],text="百度一下",state='normal',width=10,command=lambda:self.otherJob.thread_add(self.functioncall.BaiduSearch)).\
            grid(padx=5,row=0,column=7,sticky=W)
        #打开文件
        Label(frame_v[1][2],text="文件路径:",width=8,justify = LEFT).grid(padx=5,row=1,column=0,sticky=W)
        Entry(frame_v[1][2],width=50,textvariable=frame_v[1][1],justify = LEFT).grid(padx=1,row=1,column=1,columnspan=3,sticky=W)
        Label(frame_v[1][2], text="eg: D:/Python/test.txt",justify = LEFT).grid(padx=5, row=1, column=4, columnspan=3,sticky=W)
        Button(frame_v[1][2],text="打开",state='normal',width=10,command=lambda:self.otherJob.thread_add(self.functioncall.OpenFiles)).\
            grid(padx=5,row=1,column=7,sticky=W)
        #本地搜索
        Label(frame_v[2][2], text="文件名称:", width=8,justify = LEFT).grid(padx=5,row=2, column=0, sticky=W)
        Entry(frame_v[2][2],width=30,textvariable=frame_v[2][1],justify = LEFT).grid(padx=1,row=2,column=1,columnspan=2,sticky=W)
        Button(frame_v[2][2],text="本地搜索",state='normal',width=10,command=lambda:self.otherJob.thread_add(self.functioncall.SearchFiles)).\
            grid(padx=5,row=2,column=7,sticky=W)
        #微信
        Label(frame_v[3][2], text="请点击后登陆微信：", width=16,justify = LEFT).grid(padx=5,row=3, column=0,columnspan=2, sticky=W)
        Checkbutton(frame_v[3][2], text='默认登陆(后天)', width=14,variable=frame_v[3][1],justify = LEFT).grid(padx=1,row=3,column=2,columnspan=2,sticky=W)
        Button(frame_v[3][2], text="开始登陆", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.LoginWechat)). \
            grid(padx=5,row=3, column=7, sticky=W)
        #酷狗
        Label(frame_v[4][2], text="音乐名称:", width=8,justify = LEFT).grid(padx=5,row=4, column=0, sticky=W)
        Entry(frame_v[4][2], width=15, textvariable=frame_v[4][1],justify = LEFT).grid(padx=1,row=4, column=1, columnspan=2,sticky=W)
        Button(frame_v[4][2], text="播放", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic)). \
            grid(padx=5,row=4, column=7, sticky=W)
        #垃圾清理
        Label(frame_v[5][2], text="默认360垃圾清理！", width=16,justify = LEFT).grid(padx=5,row=5, column=0,columnspan=2,sticky=W)
        Button(frame_v[5][2], text="开始清理", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.Garbage_Clear)). \
            grid(padx=5,row=5, column=7, sticky=W)
        #登录邮件
        Label(frame_v[6][2], text="用户名称:", width=8,justify = LEFT).grid(padx=5,row=6, column=0, sticky=W)
        login_user = Entry(frame_v[6][2], width=20, textvariable=frame_v[6][1][0],justify = LEFT)
        login_user.insert(END,'houtian_yu@yeah.net')
        login_user.grid(padx=1,row=6, column=1,sticky=W)
        Label(frame_v[6][2], text="密码:", width=4,justify = LEFT).grid(padx=1,row=6, column=2, sticky=W)
        login_passwd = Entry(frame_v[6][2], width=15, textvariable=frame_v[6][1][1],show='*',justify = LEFT)
        login_passwd.insert(END, 'yulei927623')
        login_passwd.grid(padx=1,row=6, column=3, sticky=W)
        member = Menubutton(frame_v[6][2],text="︾选择邮箱︾",relief=GROOVE,justify = LEFT)
        member.grid(padx=1,row=6, column=4, sticky=W)
        mailmenu = Menu(member, tearoff=False)
        mailmenu.add_radiobutton(label="Yeah",variable=frame_v[6][1][2],value=1)
        mailmenu.add_radiobutton(label="126",variable=frame_v[6][1][2], value=2)
        mailmenu.add_radiobutton(label="QQ",variable=frame_v[6][1][2], value=3)
        member.config(menu=mailmenu)
        Button(frame_v[6][2], text="登录", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.LoginEmail)). \
            grid(padx=5,row=6, column=7, sticky=W)
        mainloop()

if __name__ == '__main__':

    houtian = MainGui()
    houtian.oneGui()