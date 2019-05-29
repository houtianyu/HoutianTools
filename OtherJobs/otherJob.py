import threading,win32com.client,win32api,win32con,win32gui,os,time
from win32gui import *
from win32api import *
from win32process import *
from win32con import *
class OtherJobs:

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
    def mouse_click_order(self,handle,num):
        handleDetail = win32gui.GetWindowRect(handle)
        x = handleDetail[0]
        y = handleDetail[1]
        if num == 0:
            x = handleDetail[0] - 300
            y = handleDetail[1] - 200
        time.sleep(0.5)
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
    def input_stream_remote(self,strip_ckcode):
        for i, ch in enumerate(strip_ckcode):
            print(ch)
            if ch == '.':
                outstr = 110
            else:
                outstr = ord(ch)#ord
            print(outstr)
            self.mouse_input_remote_onup(outstr)#outstr
    def save_winfile(self):
        time.sleep(0.5)
        hld = win32gui.FindWindow(None,'导出结果列表')
        time.sleep(0.5)
        hld_filename = win32gui.FindWindowEx(hld,None,u'Button',u'保存(&S)')
        #hld_filepath = win32gui.FindWindowEx(hld,None,'ToolbarWindow32','地址: 桌面')
        print(hld)
        #print(hld_filepath)dp
        print(hld_filename)
        self.mouse_click_order(hld_filename,0)
        #hld_filepath_num = [68,58,92,80,121,116,104,111,110,92,72,111,117,116,105,111,110,84,111,111,108,115,92,70,105,108,101,115]
        path = 'D:\Python\HoutianTools\Files\search_result.txt'
        self.input_stream_remote(path)
        time.sleep(2)
if __name__ == '__main__':
    a = OtherJobs()
    a.save_winfile()