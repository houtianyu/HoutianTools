_global_dict = []
_global_frame = []
_global_wechat_info = []
_global_unread_mails_info = ['']
_global_websuite_contents = []

class OverAll:
    def __init__(self):#初始化
        pass
    def set_value(self,value):
        """ 定义一个全局变量 """
        _global_dict.append(value)
    def set_label_value(self,value):
        _global_frame.append(value)
    def set_wechat_info(self,value):
        _global_wechat_info.append(value)
    def set_unread_mails_info_value(self,value,index):
        if index == 0:
            _global_unread_mails_info[0] = value
        else:
            _global_unread_mails_info.append(value)
    def set_websuite_contents(self,value):
        _global_websuite_contents.append(value)
    def get_value(self,i, defValue=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        #try:
        return _global_dict[i]
        #except KeyError:
            #return defValue
    def get_label_value(self,i, defValue=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        try:
            return _global_frame[i]
        except KeyError:
            return defValue
    def get_wechat_info(self,i):
        return _global_wechat_info[i]
    def get_unread_mails_info(self,i):
        return _global_unread_mails_info[i]
    def get_websuite_contents(self,i):
        return _global_websuite_contents[i]
    def show_len(self):
        print(len(_global_wechat_info))
        return _global_wechat_info