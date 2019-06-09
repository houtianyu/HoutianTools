from OtherJobs.otherJob import *
from Logs.logs import Logs
from OverAll.overAll import OverAll
from InterfaceCall.interfaceCall import *
class FunctionCall:
    def __init__(self):
        self.otherjob_fun = OtherJobs()
        self.other_job_log = Logs()
        self.overall = OverAll()
        self.inter_fun_mon = Resource_Monitor()
        self.function_baidusearch = BaiDuSearch()
        self.function_LoginWechat = WeiChat()
        self.play_Music_Name_Kugou = KuGouMusic()

    def BaiduSearch(self):
        baidu_object = self.overall.get_value(0)
        baidu_object_content = self.otherjob_fun.get_entryContent(baidu_object)
        self.function_baidusearch.baidu_search(baidu_object_content)
    def BaiduSearch_Auto(self):
        baidu_auto_object = self.overall.get_value(0)
        baidu_object_content = self.otherjob_fun.get_entryContent(baidu_auto_object)
        self.function_baidusearch.baidu_search_title_auto(baidu_object_content)

    def OpenFiles(self):
        openfile_object = self.overall.get_value(1)
        openfile_object_content = self.otherjob_fun.get_entryContent(openfile_object)
        function_newfile = NewFiles()
        function_newfile.open_file(openfile_object_content)
    def OpenDirWindows(self):
        openfile_object = self.overall.get_value(1)
        openfile_object_content = self.otherjob_fun.get_entryContent(openfile_object)
        function_newfile = NewFiles()
        function_newfile.open_dir_windows(openfile_object_content)

    def SearchFiles(self):
        searchfile_object = self.overall.get_value(2)
        searchfile_object_content = self.otherjob_fun.get_entryContent(searchfile_object)
        function_search_files = LocateSearch()
        function_search_files.locate_search(searchfile_object_content)

    def LoginWechat(self):
        default_Login_User_object = self.overall.get_value(3)
        default_Login_User_num = self.otherjob_fun.get_entryContent(default_Login_User_object[0])
        self.function_LoginWechat.LoginWechat(default_Login_User_num)

    #交互
    def LoginWeChat_Sweepcode(self,top):
        LoginWeChat_Sweepcode_object = self.overall.get_value(3)
        LoginWeChat_Sweepcode_num = self.otherjob_fun.get_entryContent(LoginWeChat_Sweepcode_object[0])
        self.function_LoginWechat.LoginWeChat_Sweepcode_Method(LoginWeChat_Sweepcode_num,top)
    def SearchWeChat_Contacts(self,top):
        search_contacts_result_object = self.overall.get_wechat_info(0)
        search_contacts_result = self.otherjob_fun.get_entryContent(search_contacts_result_object[1])
        self.function_LoginWechat.SearchWeChat_Contacts_Method(search_contacts_result,top)
    def SendWeChat_Messages(self,top):
        sendwechat_msg_object = self.overall.get_wechat_info(1)
        Contacts_name = self.otherjob_fun.get_entryContent(sendwechat_msg_object[0])
        Send_contents = self.otherjob_fun.get_entryContent(sendwechat_msg_object[1])
        self.function_LoginWechat.SendWeChat_Messages_Method(Contacts_name,Send_contents,top)
    def ChoiseWeChat_Files(self,top,text):
        self.function_LoginWechat.ChoiseWeChat_Files_Method(top,text)
    def SendWeChat_Files(self,top):
        sendwechat_files_object = self.overall.get_wechat_info(2)
        Contacts_name = self.otherjob_fun.get_entryContent(sendwechat_files_object[0])
        Send_contents = self.otherjob_fun.get_entryContent(sendwechat_files_object[1])
        self.function_LoginWechat.SendWeChat_Files_Method(Contacts_name, Send_contents,top)
    def GetWeChat_Messages(self,tpye,top):
        add_wechat_contents_object = self.overall.get_wechat_info(4)
        Contacts_name_get = self.otherjob_fun.get_entryContent(add_wechat_contents_object[1])
        self.function_LoginWechat.GetWeChat_Messages_Method(Contacts_name_get,tpye,top)
    def CancelWeChat_LoginOut(self,top):
        self.function_LoginWechat.CancelWeChat_LoginOut_Method(top)

    def PlayMusic(self,type):
        self.play_Music_Name_Kugou.play_Music_Name(type)
    def PlayMusic_More(self,top,text_music,type):
        play_Music_Name_object = self.overall.get_value(4)
        play_Music_Name_Names = self.otherjob_fun.get_entryContent(play_Music_Name_object)
        self.play_Music_Name_Kugou.Play_Music_More_Method(top,play_Music_Name_Names,text_music,type)



    def Garbage_Clear(self):
        garbage_Clear_object = self.overall.get_value(5)
        Garbage_Clear_Value = self.otherjob_fun.get_entryContent(garbage_Clear_object)
        Garbage_Clear_360 = LaJiQingLi()
        Garbage_Clear_360.Clear_All(Garbage_Clear_Value)
    def LoginEmail(self):
        login_email_object = self.overall.get_value(6)
        login_email_user = self.otherjob_fun.get_entryContent(login_email_object[0])
        login_email_passwd = self.otherjob_fun.get_entryContent(login_email_object[1])
        login_email_mailType = self.otherjob_fun.get_entryContent(login_email_object[2])
        login_eamil_mail_operate = Mails_operate()
        login_eamil_mail_operate.LoginEmail(login_email_mailType,login_email_user,login_email_passwd)
    def Disk_Used(self):
        self.otherjob_fun.Resource_show('请等待。。。')
        tt_disk_used = self.otherjob_fun.thread_add(self.otherjob_fun.Count_Down,15)
        disk_used_msg = self.inter_fun_mon.GetCpan()
        disk_used_msg = str(disk_used_msg).split('OrderedDict')[-1].split('([')[-1].split('])')[0]
        self.otherjob_fun.Resource_show(disk_used_msg)
        self.otherjob_fun.Stop_Thread_add(tt_disk_used)
    def Cpu_Used(self):
        self.otherjob_fun.Resource_show('请等待。。。')
        tt_cpu_used = self.otherjob_fun.thread_add(self.otherjob_fun.Count_Down, 15)
        cpu_used_msg = self.inter_fun_mon.GetCpu()
        self.otherjob_fun.Resource_show(cpu_used_msg)
        self.otherjob_fun.Stop_Thread_add(tt_cpu_used)
    def Mem_Used(self):
        self.otherjob_fun.Resource_show('请等待。。。')
        mem_used_msg = self.inter_fun_mon.GetMemory()
        self.otherjob_fun.Resource_show(mem_used_msg)
    def Mails_Unread(self):
        self.otherjob_fun.Resource_show('请等待。。。')
        tt_mails_unread = self.otherjob_fun.thread_add(self.otherjob_fun.Count_Down, 30)
        mails_used_msg = self.inter_fun_mon.Get_Unreadmails_Num()
        self.otherjob_fun.Resource_show(mails_used_msg)
        self.otherjob_fun.Stop_Thread_add(tt_mails_unread)
    def Up_Monitor(self):
        up_monitor_job = '监控进程已经启动！'
        self.otherjob_fun.Resource_show(up_monitor_job)
        self.other_job_log.LogsSave(up_monitor_job)
        self.inter_fun_mon.Monitor()
    def Open_Websit(self):
        open_websuit_object = self.overall.get_value(8)
        open_websuilt_type = self.otherjob_fun.get_entryContent(open_websuit_object)
        print('111')
        print(open_websuilt_type)
        self.function_baidusearch.open_websuit_com(open_websuilt_type)
    def Init_Config(self):
        print('准备初始化，请确保配置文件中Everything路径的准确性！')
        self.otherjob_fun.Resource_show('准备初始化，请确保配置文件中Everything路径的准确性！')
        self.other_job_log.LogsSave('准备初始化，请确保配置文件中Everything路径的准确性！')
        init_config_tips = '正在初始化配置！'
        tt_init_config = self.otherjob_fun.thread_add(self.otherjob_fun.Count_Down, 60,init_config_tips)
        self.other_job_log.LogsSave(init_config_tips)
        self.otherjob_fun.Init_Exe_Path()
        init_config_tips_finish = '初始化配置完成！'
        self.otherjob_fun.Resource_show(init_config_tips_finish)
        self.other_job_log.LogsSave(init_config_tips_finish)
        self.otherjob_fun.Stop_Thread_add(tt_init_config)
