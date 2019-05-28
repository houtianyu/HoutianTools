import threading,win32com.client,win32api,win32con,win32gui,os,time
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
    def mouse_click_order(self,handle):
        handleDetail = win32gui.GetWindowRect(handle)
        x = handleDetail[0] + 100
        y = handleDetail[1]
        time.sleep(0.5)
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    def mouse_input_remote(self,num):
        win32api.keybd_event(num, 0, 0, 0)
        win32api.keybd_event(num, 0, win32con.KEYEVENTF_KEYUP, 0)
    def input_stream_remote(self,strip_ckcode):
        for i, ch in enumerate(strip_ckcode):
            if ch == '.':
                outstr = 110
            else:
                outstr = ord(ch)
            self.mouse_input_remote(outstr)
    def input_value(self,search_content,windowsone,class_two,windowstwo=None):
        hld = win32gui.FindWindow(None,windowsone)
        if hld:
            pass
        else:
            exe = windowsone + '.exe'
            exe_path = 'E:\\softinstall\\Everything\\' + exe
            os.system(exe_path)
        hld = win32gui.FindWindow(None, windowsone)
        time.sleep(0.5)
        hld_two = win32gui.FindWindowEx(hld, None, class_two,windowstwo)  # 获取hld下第一个为edit控件的句柄
        self.mouse_click_order(hld_two)
        self.input_stream_remote(search_content)
        time.sleep(0.5)
