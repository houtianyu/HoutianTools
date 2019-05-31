from OtherJobs.otherJob import OtherJobs
from OverAll.overAll import OverAll
from InterfaceCall.interfaceCall import *
class FunctionCall:
    def __init__(self):
        self.otherjob_fun = OtherJobs()
        self.overall = OverAll()
        self.inter_fun_mon = Resource_Monitor()
    def BaiduSearch(self):
        baidu_object = self.overall.get_value(0)
        baidu_object_content = self.otherjob_fun.get_entryContent(baidu_object)
        function_baidusearch = BaiDuSearch()
        function_baidusearch.baidu_search(baidu_object_content)
    def OpenFiles(self):
        openfile_object = self.overall.get_value(1)
        openfile_object_content = self.otherjob_fun.get_entryContent(openfile_object)
        function_newfile = NewFiles()
        function_newfile.open_file(openfile_object_content)
    def SearchFiles(self):
        searchfile_object = self.overall.get_value(2)
        searchfile_object_content = self.otherjob_fun.get_entryContent(searchfile_object)
        function_search_files = LocateSearch()
        function_search_files.locate_search(searchfile_object_content)
    def LoginWechat(self):
        default_Login_User_object = self.overall.get_value(3)
        default_Login_User_num = self.otherjob_fun.get_entryContent(default_Login_User_object)
        function_LoginWechat = WeiChat()
        function_LoginWechat.LoginWechat(default_Login_User_num)
    def PlayMusic(self):
        play_Music_Name_object = self.overall.get_value(4)
        play_Music_Name_Names = self.otherjob_fun.get_entryContent(play_Music_Name_object)
        play_Music_Name_Kugou = KuGouMusic()
        play_Music_Name_Kugou.play_Music_Name(play_Music_Name_Names)
    def Garbage_Clear(self):
        garbage_Clear_object = self.overall.get_value(5)
        Garbage_Clear_Value = self.otherjob_fun.get_entryContent(garbage_Clear_object)
        Garbage_Clear_360 = LaJiQingLi()
        Garbage_Clear_360.Clear_All(Garbage_Clear_Value)
    def LoginEmail(self):
        login_email_object = self.overall.get_value(6)
        print(login_email_object)
        login_email_user = self.otherjob_fun.get_entryContent(login_email_object[0])
        login_email_passwd = self.otherjob_fun.get_entryContent(login_email_object[1])
        login_email_mailType = self.otherjob_fun.get_entryContent(login_email_object[2])
        login_eamil_mail_operate = Mails_operate()
        login_eamil_mail_operate.LoginEmail(login_email_mailType,login_email_user,login_email_passwd)
    def Disk_Used(self):
        disk_used_msg = self.inter_fun_mon.GetCpan()
        self.otherjob_fun.Resource_show(disk_used_msg)
    def Cpu_Used(self):
        cpu_used_msg = self.inter_fun_mon.GetCpu()
        self.otherjob_fun.Resource_show(cpu_used_msg)
    def Mem_Used(self):
        mem_used_msg = self.inter_fun_mon.GetMemory()
        self.otherjob_fun.Resource_show(mem_used_msg)
    def Mails_Unread(self):
        mails_used_msg = self.inter_fun_mon.Get_Unreadmails_Num()
        self.otherjob_fun.Resource_show(mails_used_msg)
    def Up_Monitor(self):
        up_monitor = self.inter_fun_mon.Monitor()