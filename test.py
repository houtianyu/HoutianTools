import os,time,string
import json,re,urllib,urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import shutil,requests,psutil
import http.cookiejar
import execjs,js2py,time,datetime


class DiskClean(object):
    def Get_Unreadmails_Info(self):
        url = 'https://mail.yeah.net/js6/s?sid=KAuVfZCbTaRGqcwVKqbbaeUnICemwhfc&func=mbox:listMessages&YxInboxBottomShow=deptId=1|projectId=117&mbox_title_unread=folder'
        data = {'var': '<?xml version="1.0"?><object><array name="fids"><int>1</int></array><object name="filter"><object name=\
        "flags"><boolean name="read">false</boolean></object></object><string name="order">date</string><boolean name="desc">true\
        </boolean><int name="limit">20</int><int name="start">0</int><boolean name="skipLockedFolders">false</boolean><boolean name=\
        "returnTag">true</boolean><boolean name="returnTotal">true</boolean></object>'}
        header = {'Accept': 'text/javascript','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh;q=0.9','Connection': 'keep-alive',
                    'Content-Length': '663',
                    'Content-type': 'application/x-www-form-urlencoded',
                    'Cookie': 'mail_health_check_time=1560658183701; mail_upx_nf=; mail_idc=""; secu_info=1; locale=; mail_style=js6; mail_uid=houtian_yu@yeah.net; mail_host=mail.yeah.net; MailMasterPopupTips=1560658187232; MailPromotePopup2=1560658402502; starttime=; ANTICSRF=cleared; P_INFO=; df=mail163_letter; MAIL_PINFO=""; NTES_SESS=E4zZQu1tH4BHq8XTNmXxm5stLtamnbzUTr6jvJnFbML.ybvYyrnuZzvAN3rMRBZg8v_k4_WTZQJApgsxACUR0JklV1vsp0JId03y9dMIWQPztEMuzV2DrXk4mFlNuJ4DfSng5AyLj70EmIik3P.D1S3IzomYRIRA_B_rQO1yNgagzgQdpVgqcyfG5eOKdTrlKYairptS0_ZDDinnBvvEmNON7; NTES_PASSPORT=dgPrFO0p4WEZ7s6wm6J05OpMO9fcsbe.bPqIwSoC2NUWFjMNF3qU1PMOJk3p.a1DcMzdmzGW19g4PJKs3N5sKm3a968rjYLNXxGxbMD_z40id5Nfamx.QAX4WgD6lwuiKSIHXAoeGAkcQHaizsxbF_gmZyeidY7E2B4Au.LA3MXflDIIUEqucSMpiwTLk4hRt3WKUNgXgBrnP; S_INFO=1560684989|0|##3&80|houtian_yu@yeah.net; P_INFO=houtian_yu@yeah.net|1560684989|1|mailyeah|00&99|bej&1560683995&mailyeah#bej&null#10#0#0|&0|mailyeah|houtian_yu@yeah.net; mail_upx=t1hz.mail.yeah.net|t2hz.mail.yeah.net|t3hz.mail.yeah.net|t4hz.mail.yeah.net|t7hz.mail.yeah.net|t8hz.mail.yeah.net|t4bj.mail.yeah.net|t1bj.mail.yeah.net|t2bj.mail.yeah.net|t3bj.mail.yeah.net; Coremail=e7627503b44da%KAuVfZCbTaRGqcwVKqbbaeUnICemwhfc%g1a8.mail.yeah.net; cm_last_info=dT1ob3V0aWFuX3l1JTQweWVhaC5uZXQmZD1odHRwcyUzQSUyRiUyRm1haWwueWVhaC5uZXQlMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzREtBdVZmWkNiVGFSR3Fjd1ZLcWJiYWVVbklDZW13aGZjJnM9S0F1VmZaQ2JUYVJHcWN3VktxYmJhZVVuSUNlbXdoZmMmaD1odHRwcyUzQSUyRiUyRm1haWwueWVhaC5uZXQlMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzREtBdVZmWkNiVGFSR3Fjd1ZLcWJiYWVVbklDZW13aGZjJnc9aHR0cHMlM0ElMkYlMkZtYWlsLnllYWgubmV0Jmw9LTEmdD0tMSZhcz10cnVl; MAIL_SESS=E4zZQu1tH4BHq8XTNmXxm5stLtamnbzUTr6jvJnFbML.ybvYyrnuZzvAN3rMRBZg8v_k4_WTZQJApgsxACUR0JklV1vsp0JId03y9dMIWQPztEMuzV2DrXk4mFlNuJ4DfSng5AyLj70EmIik3P.D1S3IzomYRIRA_B_rQO1yNgagzgQdpVgqcyfG5eOKdTrlKYairptS0_ZDDinnBvvEmNON7; MAIL_SINFO=1560684989|0|##3&80|houtian_yu@yeah.net; mail_entry_sess=6efb18d372726bded20070f9424514326dd66be0dd1bbf50f4bca5a67d60b047c8b121018ff0debf63ca44265ba0d169c86f4bca1a20d04b6e8771f2a76acfa76eb1716b9bc55b12de58c5264b57577e9a1620efa9bb02ea51d774d7c3de6d5816ad995847783ac0fdaf4ec71fce1636ff70dbf03650a21b617303fd92b74ff7c26dc4024f29eb70f5355b51ff3365fb055ea5675da6ead5f405720596644da68d4409afd22c98e9a317b3982513af4e76be1eff306717931568e298bf105176; JSESSIONID=2760A8AC584A73118BB77DB6DCA627D6; Coremail.sid=KAuVfZCbTaRGqcwVKqbbaeUnICemwhfc',
                    'Host': 'mail.yeah.net',
                    'Origin': 'https://mail.yeah.net',
                    'Referer': "https://mail.yeah.net/js6/main.jsp?sid=hAbVnMNKwbXeJAJQlJKKneHIwMiMPFrq&df=mail163_letter",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        unread_info_all = []
        unread_mails_from = ''
        unread_mails_subject = ''
        sendtime = ''
        total = 0
        timeOut = 10
        r = requests.post(url,data=data,headers=header,timeout=timeOut,allow_redirects=True, verify=False)
        res = r.content.decode('utf-8')
        res_lists = res.split('\'var\':')[-1].split('},\n{')
        for res_list_every in res_lists:
            #for info_list in res_list_every.split('\n'):
            if 'from' in res_list_every:
                unread_mails_from = res_list_every.split('\n')[4].split(':')[-1].split('\'')[1]
            if 'subject' in res_list_every:
                unread_mails_subject = res_list_every.split('\n')[6].split(':')[-1].split('\'')[1]
            if 'sentDate' in res_list_every:
                sendtime = res_list_every.split('\n')[7].split(':')[-1].split('(')[-1].split('),')[0].replace(',',':')
            if 'total' in res_list_every:
                total = res_list_every.split('\n')[18].split(':')[-1].split('}')[0]
            unread_info_dic = {'发件人':unread_mails_from,'主题':unread_mails_subject,'发件时间':sendtime}
            unread_info_all.append(unread_info_dic)
        print(unread_info_all)
        print(total)
    def process_info(self):
        proc_mem_percent, cmdlines, cpu_percent = '', '', ''
        proc, all_processes = [], psutil.process_iter()
        for items in all_processes:
            try:
                procinfo = items.as_dict(attrs=["pid", "name"])
                try:
                    # the process start path
                    p_path_cwd = items.cwd().encode('utf-8')
                    #p_path_cwd = items.exe()
                    # the process accounts for system memory uasge
                    proc_mem_percent = items.memory_percent()
                    # the process starts cmdline content
                    cmdlines = str(items.cmdline())
                    # the process accounts for system CPU usage
                    cpu_percent = items.cpu_percent(interval=1)
                except Exception as e:
                    #print(e)
                    try:
                        p_path_cwd = items.exe()
                    except Exception as e:
                        p_path_cwd = e.name
                p_status, p_create_time, proc_user, proc_io_info = items.status(), items.create_time(), items.username(), {}
                try:
                    proc_io = items.io_counters()
                    proc_io_info["ReadCount"] = proc_io.read_count
                    proc_io_info["WriteCount"] = proc_io.write_count
                    proc_io_info["ReadBytes"] = proc_io.read_bytes
                    proc_io_info["WriteBytes"] = proc_io.write_bytes
                except Exception as e:
                    pass
                procinfo.update({"path": p_path_cwd,
                                 "cmdline": cmdlines,
                                 "cpu_percent": cpu_percent,
                                 "status": p_status,
                                 "CreateTime": p_create_time,
                                 "MemPercent": proc_mem_percent,
                                 "user": proc_user,
                                 "DiskIo": proc_io_info})
            except Exception as e:
                pass
            finally:
                proc.append(procinfo)
        cpuhigh_percent_data,Memhigh_Percent_data=[],[]
        for proc_list in proc:
            try:
                if float(proc_list['cpu_percent']) >= 5.0:
                    cpuhigh_percent_data.append(proc_list)
            except Exception as msg:
                pass
            try:
                if float(proc_list['MemPercent']) >= 0.6:
                    Memhigh_Percent_data.append(proc_list)
            except Exception as msg:
                pass
        for list in cpuhigh_percent_data:
            print(list)
        for list in Memhigh_Percent_data:
            print(list)
    def test(self):
        data_list = 1560740660.0
        a = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data_list)))
        print(a)
    def moke(self):
        url_baidu_search__auto_format = 'https://www.imooc.com/search/?words=' + urllib.parse.quote('安全测试')
        #print(url_baidu_search__auto_format)
        req = urllib.request.Request(url_baidu_search__auto_format)
        response = urllib.request.urlopen(req, None, 30)  # 设置超时时间
        html = response.read().decode('utf-8')
        title = r"class='course-detail-title'>\n(\t\t\t\t.*)"
        contents = r"</a>\n\t\t\t<p>(.*)"
        title_list = re.findall(title,html)
        contents_list = re.findall(contents,html)
        print(len(title_list))
        print(len(contents_list))
        title_list_result = []
        contents_list_result = []
        if len(title_list) == len(contents_list):
            for i in title_list:
                i = i.strip().lstrip()#.rstrip('s')
                i = i.translate(str.maketrans('', '', "<span  class='highlight'>"))
                i = i.translate(str.maketrans('', '', '</span>'))
                print(i)
                title_list_result.append(i)
            for i in contents_list:
                i = i.translate(str.maketrans('', '', '</p>'))
                contents_list_result.append(i)
        else:
            print('数据获取可能不正确。')
    def boke(self,tpye):
        def find_result(url,blog_content_search):
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req,None,30)
            html = response.read().decode('utf-8')
            blog_contents_list = re.findall(blog_content_search, html)
            return blog_contents_list
        self.blog_result = []
        blog_result_dic = {}
        if tpye == 0:
            url = 'http://blog.sina.com.cn/s/articlelist_7009815884_0_' + '1' + '.html'
            blog_content_search = r'title="" target="_blank" href="(h.*)">'
            blog_content_search_page_num = r'共(.*)页'
            blog_contents_page_num = str(find_result(url, blog_content_search_page_num))
            page_num = int(blog_contents_page_num.split("'")[1])
            for i in range(1,page_num+1):
                url_c = 'http://blog.sina.com.cn/s/articlelist_7009815884_0_' + str(i) + '.html'
                blog_contents_list = find_result(url_c,blog_content_search)
                for list_url in blog_contents_list:
                    list_search = r'class="titName SG_txta"(>.*)</h2>'
                    blog_content_result = find_result(list_url,list_search)
                    blog_content_result = str(blog_content_result).split('>')[-1].split("'")[0]
                    blog_result_dic[blog_content_result] = list_url
                    self.blog_result.append(blog_result_dic)
                    blog_result_dic = {}
            for i in self.blog_result:
                print(i)
        elif tpye == 1:
            if not self.blog_result:
                print('请先点击搜索按钮！')
            else:
                self.num_list_moke = text_listbox.curselection()
                for num in self.num_list_moke:
                    self.inter_other_baidu.Show_Top_Msg(top, 3, self.blog_result[(num - 1)])
    def bilibili(self):
        bilibili_search_title_list = []
        bilibili_search_url_list = []
        def find_result(url,blog_content_search):
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req,None,30)
            html = response.read().decode('utf-8')
            blog_contents_list = re.findall(blog_content_search, html)
            return blog_contents_list
        url_baidu_search__auto_format = 'https://search.bilibili.com/all?keyword=' + urllib.parse.quote('红海行动') + '&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.2'
        bilibili_search = r'</span><a title="(.*)" target="'
        bilibili_search_contents = find_result(url_baidu_search__auto_format,bilibili_search)
        for every_search in bilibili_search_contents:
            bilibili_search_title = every_search.split('" href="//')[0]
            bilibili_search_url = every_search.split('" href="//')[-1]
            bilibili_search_title_list.append(bilibili_search_title)
            bilibili_search_url_list.append(bilibili_search_url)
            print(bilibili_search_title)
            print(bilibili_search_url)
    def jianxue(self):
        self.jianxue_result_one_list = []
        def post(url,data,header):
            timeOut = 10
            r = requests.post(url, data=data, headers=header, timeout=timeOut, allow_redirects=True, verify=False)
            res = r.content.decode('utf-8')
            return res
        postdata = urllib.parse.urlencode({
            "account": "18686524648",
            "password": "18686524648",
            "remeberMe": "true"
        }).encode('utf-8')
        getresult_data = urllib.parse.urlencode({
            "classPackageId": "8592"
        }).encode('utf-8')
        header_login = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9',
                  'Connection': 'keep-alive',
                  'Content-Length': '44',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'Cookie': 'acw_tc=d3a2a61815612160876231799e7bf3d951ba2398674fbb7022ae3b7735; SESSION=37c24aeb-7a30-46bc-90dc-9a56a479e03c; yunId=1f8f54870946ef11ba006d7000059b10; MEIQIA_VISIT_ID=1N0RajY3Ok8cUHWemccAiDjEeAe; account_=18686524648; account_www.jianxueedu.com.cn=18686524648; UM_distinctid=16b7fbb62a54ef-013d1626f3d084-e353165-e1000-16b7fbb62a660f; CNZZDATA1274666026=113334421-1561213183-http%253A%252F%252Fwww.jianxueedu.com.cn%252F%7C1561213183; JSESSIONID=2A9F078BB9C9CFB8AA879B40C070D02E; sec_tc=AQAAANlFeVt1JggAc7ct2/dJ9C+pRRY0',
                  'Host': 'www.jianxueedu.com.cn',
                  'Origin': 'http://www.jianxueedu.com.cn',
                  'Referer': 'http://www.jianxueedu.com.cn/',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        header_result = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "19",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "acw_tc=d3a2a61815612160876231799e7bf3d951ba2398674fbb7022ae3b7735; yunId=1f8f54870946ef11ba006d7000059b10; account_=18686524648; account_www.jianxueedu.com.cn=18686524648; UM_distinctid=16b7fbb62a54ef-013d1626f3d084-e353165-e1000-16b7fbb62a660f; cookie_user_=%7B%22companyId%22%3A72489%2C%22id%22%3A1323051%2C%22sign%22%3A%22D43978DD1FFF32539C8803CF30359AEA%22%2C%22time%22%3A%221561557595278%22%7D; SESSION=4e62b5ea-a892-4191-8b6e-9c82c1c5fa64; MEIQIA_VISIT_ID=1NBbmuxOhYPiehcUGMzd8gl0IRE; CNZZDATA1274666026=113334421-1561213183-http%253A%252F%252Fwww.jianxueedu.com.cn%252F%7C1561554100; JSESSIONID=8798E9D10C03ED984939EE4F5384359F; sec_tc=AQAAADwqGVFiFgQAc7ct21OE6FEwtJVO",
            "Host": "www.jianxueedu.com.cn",
            "Origin": "http://www.jianxueedu.com.cn",
            "Referer": "http://www.jianxueedu.com.cn/classPackage/classPackageDetail/8592",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        url = 'http://www.jianxueedu.com.cn/login'
        url_kecheng = 'http://www.jianxueedu.com.cn/classPackage/findAllStageAndCtInStage'
        post(url,postdata,header_login)
        html = post(url_kecheng,getresult_data,header_result)
        content_search = r'target="_blank">\n                                    (.*)\n'
        url_one_search = r'<a href="(.*)" target="_blank"'
        content_search_two = r'<p>(.*)</p>'
        content_search_two_url = r''
        contents_list = re.findall(content_search, html)
        print(contents_list)
        contents_list_urlone = list(set(re.findall(url_one_search,html)))
        if len(contents_list) == len(contents_list_urlone):
            for i in range(len(contents_list)):
                self.jianxue_result_one_list.append({contents_list[i]:contents_list_urlone[i]})
        print(self.jianxue_result_one_list)
    def github(self):
        result_list = []
        def post(url,data,header):
            timeOut = 20
            r = requests.post(url, data=data, headers=header, timeout=timeOut, allow_redirects=True, verify=False)
            res = r.content.decode('utf-8')
            return res
        def find_result(url,content_search,data,header):
            response = requests.get(url, params=data)
            html = response.text
            blog_contents_list = re.findall(content_search, html)
            return blog_contents_list
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "205",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "logged_in=no; _octo=GH1.1.60950074.1560874587; _ga=GA1.2.1830632947.1560879073; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=SW9Kay9yVTdhUXVIcENzZllvcWpyYmZZbDBWbGdRNDNyZ3FpL3FseHFtakFOaC9MeSszKy9zR1M1dHFxL09hLzM4KzdSZUY1bGZZVE5ESXQ2cWtzT2tod3RtRjlPMVN6bzlTWm5QS1g5SFViTnNTbzRqNWt1YStNdW44bzVUbjFaNFo1dzhPVDBuNjZaM1ZjbGxiejNzVFFrWTRGTzhuWVYwaXB6MkdSd3dZTWZrY3d5aTJqVVFIMWQ5WDY1T1VuZDF1ZzVMVEJWMGRrNHVQSUZERHlEemhiaEJSY1BXeGo2MXN6bEY1cGZwMkNLZy9obzZ6d1RNR0R3QUk4N2wvSzRFN2ZhMlBXWVZDL0h1ejBIMTEwdGNsUTJLTWRscjJpU2J2bFZ6SUZxbFdwSnFtaXdtRWFpQ0RqN2tqVW5vaFAyVHgvd1JjOGhRbWcwb05TTGJYckZSb1JhQWJpOGsrd3FQa1JaZ3UyMVROWjV4dWZvWXA5cmtwYWllQ2dkWjhpRzJ5NjI5VXZlbFdYN0tFRHJna0pIdEl0RERENFlxZ2ZGTzdCd3NnRWFHR0w4YndUWUp4azFnY0t6L1FUb3o4ZGJPOUxOeDZwaFVtbzJvNzVLUjVIWmYyc2FhLy9EaGlCWGtqd3BDS3NLaGt1bkdhTk5iZ0p2allJc1poSm9OK2VkTjRCcTM1OFFRYnNPQjMxdUJHcFJwaUVvMk5TRDBDMC9MQWh3NUErMDRPMjNzSk1SZ0pCaDFnWVBFRHRCblZlRFJJMGlIUUdxRGpwdkpJZmhpemUyOWRueW4rdThCWkxyNnVadTZaejdzUnZBWmFwVFJiRE81WS9ScXI2VGdwYzJQYkFvYnRITU10b3VjRGljcTQ0Ymw1S3ZBTEZ4R29xUTB5R0EwUHBIS0FNRVFTak1NVTNQNUgwSXlENndoS3k5ZEhxeEN3aG9HM0x0c3A0K0hZdUtnPT0tLUUyNGV1a3lXTVU4UmpLaytmYW8relE9PQ%3D%3D--7969d1cb34cc28b49032cb1cbfeaf17635fad074",
            "Host": "github.com",
            "Origin": "https://github.com",
            "Referer": "https://github.com/login?return_to=%2Fjoin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        data = urllib.parse.urlencode({
            "authenticity_token": "kwhRO7gSJlIRxpROIJOGSJ9nQ4PBllB9IiVxx5a+qjUcd5kQPqkmvlylhQMginWaq5ULN6eMf6qkEPSPJUoGAg==",
            "login": "houtianyu",
            "password": "yulei927623",
            "webauthn-support": "unknown",
            "commit": "Sign in"
        }).encode('utf-8')
        header_g = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_octo=GH1.1.60950074.1560874587; _ga=GA1.2.1830632947.1560879073; has_recent_activity=1; tz=Asia%2FShanghai; _device_id=857f8342a24f1e471d035ddaff539972; user_session=ikAm6VNDJY1sSLcx9D6OnriZxXcpUgmYvVWQrBiPFE42rl6Z; __Host-user_session_same_site=ikAm6VNDJY1sSLcx9D6OnriZxXcpUgmYvVWQrBiPFE42rl6Z; logged_in=yes; dotcom_user=houtianyu; _gh_sess=Z245N1dLemhLZHhYQjVvVDRQdDY1NCtBUXNHTlhVNG02U1hwbEZ5K3k0THEvd1pnZnQ2QkEyM0NDcFcybGVnQ20xa3VVajdFSmo2bG5Da2c0dmxwL0lSWDlwRGdDYXR2dkFMSW1FdStPNXJ4WXBXbmZsaittRmdubkpNQkl0V01USU9JK2F2ejBVcE8zL0N0bWxsaHhBM00rekIrZXI3NGRWT3gwdFZsVmNKZlN4NkE4WFpaajYyMloxWWY4VmFMOWJCK1VmSnlDQ0EvYkFDbFJZNEtKRGljS2R0bkRYL2hvS0c1QmxGZlFmYjloNFVkN0dvQlN5R3NOM1dma05YS1B6aXFhdis3SWVRRDdPamVtSVVQeG41bDEvMU4xS0pUakhFRWtDTStvdlhla0tpMzc2cFRZZEduNDVkL1BWMlFVQWV2VERpQWM4bmxGRUVDdUxiUUZRPT0tLVVOcWJjc0txMkRUNWo4UGRxWDBDK3c9PQ%3D%3D--81b156d5c9978050ebf19a7eaa10ef42794da5d9; _gat=1",
            "Host": "github.com",
            "If-None-Match":'W/"354e92314934d94841e91f990eb05ad7"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        data_g = urllib.parse.urlencode({
            "tab": "repositories"
        }).encode('utf-8')
        url_s = r'https://github.com/session'
        url = r'https://github.com/houtianyu?tab=repositories'
        content_search = r'" itemprop="name codeRepository" >\n(.*)</a>'
        post(url_s,data,header)
        for result in find_result(url,content_search,data_g,header_g):
            result_list.append(result.strip().lstrip())
        print(result_list)
    def baidufanyi(self):
        def find_result(url,data):
            header = {
                "authority": "fanyi.baidu.com",
                "method": "POST",
                "path": "/v2transapi",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "content-length": "136",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cookie": "BAIDUID=674189B37A88C987E365F832C2E5FA18:FG=1; PSTM=1560654964; BIDUPSID=322402D2E42B4CB2C5335FA59D41A0F1; BDUSS=UzRHpaNXZyUjI5VzlVaDRGNUZSODhsSkw2NXpWZWJyUH5Md1d2UTlEcjJKak5kSVFBQUFBJCQAAAAAAAAAAAEAAAA~-2Q50~DDq8fyNjg2OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPaZC132mQtdej; H_PS_PSSID=29250_1431_21081_18560_29135_29238_28519_29098_29131_29368_28830_29220_26350; delPer=0; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561474014; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1561474014; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=52cde8e76211af2f58df150d5af4c71a9e12c76b_1561474015_js; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
                "origin": "https://fanyi.baidu.com",
                "referer": "https://fanyi.baidu.com/?aldtype=16047",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
            timeOut = 20
            r = requests.post(url, data=data,headers=header,timeout=timeOut, allow_redirects=True, verify=False)
            res = json.loads(r.content.decode('utf-8'))
            return res
        url = 'https://fanyi.baidu.com/v2transapi'
        url_langedect = r'https://fanyi.baidu.com/langdetect'
        js_path = os.getcwd()
        js_hole_path = js_path + r'\Files\baidujs.js'
        data_langdetect = {
            "query": content_search
        }
        from_fy = find_result(url_langedect,data_langdetect)['lan']
        print(from_fy)
        if from_fy == 'zh':
            to_fy = 'en'
        else:
            to_fy = 'zh'
        with open(js_hole_path,encoding='utf8') as f:
            jsData = f.read()
        run_js = js2py.EvalJs({})
        run_js.execute(jsData)
        sign = run_js.e(content_search)
        data_fy = {
            "from": from_fy,
            "to": to_fy,
            "query": content_search,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "a19c31f26c6cbce5198765c20653af6d"
        }
        translate_result = find_result(url,data_fy)['trans_result']['data'][0]['dst']
        print(translate_result)
    def test1(self):
        ss = '\r\n  杜卡迪中国'
        ss = ss.translate(str.maketrans('', '', '\n')).translate(str.maketrans('', '', '\r')).strip()
        print(ss)
    def times(self):
        times = '7/22/2019 7:57:24.324'
        time_am = '7/22/2019 7:57:24 AM'
        timeArray = int(time.mktime(time.strptime(times, "%m/%d/%Y %H:%M:%S.%f")))
        timem = int(time.mktime(time.strptime(time_am, "%m/%d/%Y %H:%M:%S %p")))
        if 'PM' in time_am:
            timem = timem + 43200
        print(timem)
        print(timeArray)
    def file(self):
        file = os.listdir(r'D:\Python\HoutianTools\Files')
        for filename in file:
            filepath = os.path.join(r'D:\Python\HoutianTools\Files',filename)
            if os.path.isfile(filepath):
                print(filepath)
    def tttt(self,i):
        if 1 < i < 1:
            print('aaa')
        print('bbbb')


if __name__ == '__main__':
    cleaner = DiskClean()
    begin = time.time()
    #cleaner.Get_Unreadmails_Info()
    cleaner.tttt(1)
    end = time.time()
    cost = end - begin
    print(cost)