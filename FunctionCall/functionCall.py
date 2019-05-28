from OtherJobs.otherJob import OtherJobs
from OverAll.overAll import OverAll
from InterfaceCall.interfaceCall import *
class FunctionCall:
    def __init__(self):
        self.otherjob_fun = OtherJobs()
        self.overall = OverAll()
    def BaiduSearch(self):
        baidu_object = self.overall.get_value(0)
        baidu_object_content = self.otherjob_fun.get_entryContent(baidu_object)
        self.function_baidusearch = BaiDuSearch()
        self.function_baidusearch.baidu_search(baidu_object_content)
    def OpenFiles(self):
        openfile_object = self.overall.get_value(1)
        openfile_object_content = self.otherjob_fun.get_entryContent(openfile_object)
        print(openfile_object_content)
        self.function_newfile = NewFiles()
        self.function_newfile.open_file(openfile_object_content)
    def SearchFiles(self):
        searchfile_object = self.overall.get_value(2)
        searchfile_object_content = self.otherjob_fun.get_entryContent(searchfile_object)
        print(searchfile_object_content)
        self.function_search_files = LocateSearch()
        self.function_search_files.locate_search(searchfile_object_content)
    def LoginWechat(self):
        pass
    def PlayMusic(self):
        pass