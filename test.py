import os,time
import json
import shutil
class DiskClean(object):
    def __init__(self):
        self.del_info = {}
        self.del_file_paths = []
        self.total_size = 0
        self.del_all_files_num = 0
        del_extension = {
            '.tmp': '临时文件',
            '._mp': '临时文件_mp',
            '.log': '日志文件',
            '.gid': '临时帮助文件',
            '.chk': '磁盘检查文件',
            '.old': '临时备份文件',
            '.xlk': 'Excel备份文件',
            '.bak': '临时备份文件bak'
        }
        self.wx_path = 'C:\\Users\\AT\\Documents\\WeChat Files\\yuwei927furui\\'
        self.del_userprofile = ['Files','FileStorage','HDHeadImage','Image','Video','Attachment']
        SYS_DRIVE = os.environ['systemdrive'] + '\\'
        USER_PROFILE = os.environ['userprofile']
        WIN_DIR = os.environ['windir']
        self.scan_path = [SYS_DRIVE,USER_PROFILE,WIN_DIR]
        for k, v in del_extension.items():
            self.del_info[k] = dict(name=v, count=0)
    # 字节bytes转化kb\m\g
    def formatSize(self):
        try:
            self.total_size = float(self.total_size)
            kb = self.total_size / 1024
        except:
            print("传入的字节格式不对")
            return "Error"
        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%fG" % (G)
            else:
                return "%fM" % (M)
        else:
            return "%fkb" % (kb)
    def del_dir_or_file(self,root):
        try:
            if os.path.isfile(root):
                # 删除文件
                os.remove(root)
                print('file: ' + root + ' removed')
            elif os.path.isdir(root):
                # 删除文件夹
                shutil.rmtree(root)
                print('directory: ' + root + ' removed')
        except WindowsError:
            print('failure: ' + root + " can't remove")
    def scan_workspace(self,dirs_format,wx_dirs_path):
        for dirs_p in dirs_format:
            for roots, dirs, files in os.walk(dirs_p, topdown=False):
                # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
                for file_item in files:
                    # 获取扩展名
                    file_extension = os.path.splitext(file_item)[1]
                    # print os.path.join(roots, file_item)
                    if file_extension in self.del_info:
                        # 文件完整路径
                        file_full_path = os.path.join(roots, file_item)
                        print('完成扫描%s 的路径' % file_full_path)
                        self.del_file_paths.append(file_full_path)
                        self.del_info[file_extension]['count'] += 1
                        self.total_size += os.path.getsize(file_full_path)
            print('%s 目录扫描完成！' % dirs_p)
        for dirs_wx in wx_dirs_path:
            wx_dirs_path_all = self.wx_path + dirs_wx
            print(wx_dirs_path_all)
            for roots,dirs,files in os.walk(wx_dirs_path_all,topdown=False):
                for wx_file_item in files:
                    wx_file_full_path = os.path.join(roots, wx_file_item)
                    print('完成扫描%s 的路径' % wx_file_full_path)
                    self.del_file_paths.append(wx_file_full_path)
                    self.del_all_files_num += 1
                    self.total_size += os.path.getsize(wx_file_full_path)
            print('%s 目录扫描完成！' % wx_dirs_path_all)
        #print(json.dumps(self.del_info, indent=4, ensure_ascii=False))
        print('.tmp格式的%s数：%s,._mp格式的%s数：%s,.log格式的%s数：%s,.gid格式的%s数：%s,.chk格式的%s数：%s,.old格式的%s数：%s,.xlk格式的%s数：%s,.bak格式的%s数：%s' \
            % (self.del_info['.tmp']['name'], self.del_info['.tmp']['count'], self.del_info['._mp']['name'],self.del_info['._mp']['count'], \
               self.del_info['.log']['name'], self.del_info['.log']['count'], self.del_info['.gid']['name'],self.del_info['.gid']['count'], \
               self.del_info['.chk']['name'], self.del_info['.chk']['count'], self.del_info['.old']['name'],self.del_info['.old']['count'], \
               self.del_info['.xlk']['name'], self.del_info['.xlk']['count'], self.del_info['.bak']['name'],self.del_info['.bak']['count']))
        self.del_all_files_num = self.del_all_files_num + self.del_info['.tmp']['count'] + self.del_info['._mp']['count'] + self.del_info['.gid']['count'] + self.del_info['.log']['count'] + self.del_info['.old']['count'] + \
                                 self.del_info['.chk']['count'] + self.del_info['.xlk']['count'] + self.del_info['.bak']['count']
        print('总共删除%s个文件,删除可节省:%s 空间' % (self.del_all_files_num,self.formatSize()))
    def delete_files(self):
        for i in self.del_file_paths:
            print('正在删除%s 文件或目录！' % i)
            self.del_dir_or_file(i)
if __name__ == '__main__':
    cleaner = DiskClean()
    begin = time.time()
    cleaner.scan_workspace(cleaner.scan_path,cleaner.del_userprofile)
    cleaner.delete_files()
    end = time.time()
    cost = end - begin
    print(cost)