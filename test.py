import itchat,win32gui,win32api,win32con
def close_QR_img():
    hld_QR = win32gui.FindWindow('Windows.UI.Core.CoreWindow', None)
    print(hld_QR)
    win32gui.SendMessage(hld_QR,win32con.WM_CLOSE,0,0)
    print('登陆完成')
itchat.auto_login(loginCallback=close_QR_img)#
itchat.run()

