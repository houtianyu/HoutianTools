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
                     [4,'v_kugou','frame_kugou'],[5,'v_garbage','frame_garbage']]
        for value in frame_v:
            value[1]= StringVar()
            self.overall.set_value(value[1])
            value[2] = Frame(self.root,height=5,relief=GROOVE).grid(padx=20,pady=5,row=value[0],column=0,columnspan=8,stick=W)
        #百度
        Entry(frame_v[0][2],width=80,textvariable=frame_v[0][1]).grid(padx=20,pady=5,row=0,column=0,columnspan=5,stick=W)
        Button(frame_v[0][2],text="百度一下",state='normal',width=10,command=lambda:self.otherJob.thread_add(self.functioncall.BaiduSearch)).\
            grid(padx=20,pady=5,row=0,column=7,stick=W)
        #打开文件
        Label(frame_v[1][2],text="文件路径：",width=10).grid(padx=10,pady=5,row=1,column=0,stick=W)
        Entry(frame_v[1][2],width=55,textvariable=frame_v[1][1]).grid(padx=2,pady=5,row=1,column=1,columnspan=3,stick=W)
        Label(frame_v[1][2], text="eg: D:/Python/test.txt").grid(padx=10, pady=5, row=1, column=4, columnspan=3,stick=W)
        Button(frame_v[1][2],text="打开",state='normal',width=10,command=lambda:self.otherJob.thread_add(self.functioncall.OpenFiles)).\
            grid(padx=20,pady=5,row=1,column=7,stick=W)
        #本地搜索
        Label(frame_v[2][2], text="文件名：", width=10).grid(padx=5, pady=5, row=2, column=0, stick=W)
        Entry(frame_v[2][2],width=30,textvariable=frame_v[2][1]).grid(padx=3,pady=5,row=2,column=1,columnspan=2,stick=W)
        Button(frame_v[2][2],text="本地搜索",state='normal',width=10,command=lambda:self.otherJob.thread_add(self.functioncall.SearchFiles)).\
            grid(padx=20,pady=5,row=2,column=7,stick=W)
        #微信
        Label(frame_v[3][2], text="扫码登陆：", width=10).grid(padx=10, pady=5, row=3, column=0, stick=W)
        Button(frame_v[3][2], text="开始登陆", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.LoginWechat)). \
            grid(padx=20, pady=5, row=3, column=7, stick=W)
        #酷狗
        Label(frame_v[4][2], text="音乐名：", width=10).grid(padx=5, pady=5, row=4, column=0, stick=W)
        Entry(frame_v[4][2], width=30, textvariable=frame_v[4][1]).grid(padx=5, pady=5, row=4, column=1, columnspan=2,stick=W)
        Button(frame_v[4][2], text="播放", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.PlayMusic)). \
            grid(padx=20, pady=5, row=4, column=7, stick=W)
        #垃圾清理
        Label(frame_v[5][2], text="默认360垃圾清理！", width=15).grid(padx=10, pady=5, row=5, column=0,columnspan=2,stick=W)
        Button(frame_v[5][2], text="开始清理", state='normal', width=10,command=lambda: self.otherJob.thread_add(self.functioncall.LoginWechat)). \
            grid(padx=20, pady=5, row=5, column=7, stick=W)

        mainloop()



if __name__ == '__main__':

    houtian = MainGui()
    houtian.oneGui()