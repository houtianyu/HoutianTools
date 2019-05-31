class OverAll:
    def __init__(self):#初始化
        global _global_dict
        global _global_frame
        _global_dict = []
        _global_frame = []
    def set_value(self,value):
        """ 定义一个全局变量 """
        _global_dict.append(value)
    def set_frame_value(self,value):
        _global_frame.append(value)
    def get_value(self,i, defValue=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        try:
            return _global_dict[i]
        except KeyError:
            return defValue
    def get_frame_value(self,i, defValue=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        try:
            return _global_dict[i]
        except KeyError:
            return defValue