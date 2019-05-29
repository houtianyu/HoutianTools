import threading,win32com.client,win32api,win32con,win32gui,os,time
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
        time.sleep(0.5)
        hld = win32gui.FindWindow(None,u'导出结果列表')
        time.sleep(0.5)
        hld1 = win32gui.FindWindowEx(hld,None,"DUIViewWndClassName",None)
        hld2 = win32gui.FindWindowEx(hld1, None, "DirectUIHWND", None)
        hld3 = win32gui.FindWindowEx(hld2, None, "FloatNotifySink", None)
        hld4 = win32gui.FindWindowEx(hld3, None, "ComboBox", None)
        hld5 = win32gui.FindWindowEx(hld4, None, "Edit", None)
        win32gui.SendMessage(hld5, win32con.WM_SETTEXT, None, path)
        hwnd_save = win32gui.FindWindowEx(hld, None, "Button",u'保存(&S)')
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

if __name__ == '__main__':
    a = OtherJobs()
