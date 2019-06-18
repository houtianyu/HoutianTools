import os,time
import json,re
from selenium import webdriver
import shutil,requests,psutil
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

if __name__ == '__main__':
    cleaner = DiskClean()
    begin = time.time()
    #cleaner.Get_Unreadmails_Info()
    cleaner.test()
    end = time.time()
    cost = end - begin
    print(cost)