# -*- coding: UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import datetime
import json
from urllib.parse import urlencode
import urllib

iPDP=input("iPlanetDirectoryPro")
formDatainp=input("formData2")


s = requests.Session()
url = 'http://e-office2.nuist.edu.cn/infoplus/form/XNYQSB/start'
# cookies = dict(INGRESSCOOKIE='1612425402.576.120.251848', JSESSIONID='1C75229FB4005E181C8DAAF8857AB3FA.TomcatC',iPlanetDirectoryPro='Xdu0h0zdQlig2dtROU3fee7rhZx0lYJh')
cookies = dict(INGRESSCOOKIE='1612582906.278.2210.770261', JSESSIONID='1C364619F41C8D6A58B2AE534EB5CF5B.TomcatC', iPlanetDirectoryPro='dtSG7P14FyxuKWFpkc4HWa5BVypxk0nj')
cookies = dict(iPlanetDirectoryPro=iPDP)
r1 = s.get(url,cookies=cookies)
cookieNew = r1.cookies
htmlTextOri = r1.text
html = BeautifulSoup(htmlTextOri,'lxml')
print(html)
tar1 = str(html.find_all('meta')[3])
csrfToken = tar1.split('"')[1]
url2 = 'http://e-office2.nuist.edu.cn/infoplus/interface/start'
data2 = {'idc':'XNYQSB',
         'release':'',
         'csrfToken':csrfToken,
         'formData':'{"_VAR_EXECUTE_INDEP_ORGANIZE_Name":"计算机与软件学院-王韵璐","_VAR_ACTION_INDEP_ORGANIZES_Codes":"20900\n20900-850319","_VAR_ACTION_REALNAME":"褚午杰","_VAR_ACTION_ORGANIZE":"20900-850319","_VAR_EXECUTE_ORGANIZE":"20900-850319","_VAR_ACTION_INDEP_ORGANIZE":"20900","_VAR_ACTION_INDEP_ORGANIZE_Name":"计算机与软件学院","_VAR_ACTION_ORGANIZE_Name":"计算机与软件学院-王韵璐","_VAR_EXECUTE_ORGANIZES_Names":"计算机与软件学院-王韵璐","_VAR_OWNER_ORGANIZES_Codes":"20900-850319\n20900","_VAR_ADDR":"112.2.120.135","_VAR_OWNER_ORGANIZES_Names":"计算机与软件学院-王韵璐\n计算机与软件学院","_VAR_URL":"http://e-office2.nuist.edu.cn/infoplus/form/3963215/render","_VAR_EXECUTE_ORGANIZE_Name":"计算机与软件学院-王韵璐","_VAR_RELEASE":"true","_VAR_NOW_MONTH":"2","_VAR_ACTION_USERCODES":"201883290620","_VAR_ACTION_EMAIL":"201883290620@nuist.edu.cn","_VAR_ACTION_ACCOUNT":"201883290620","_VAR_ACTION_INDEP_ORGANIZES_Names":"计算机与软件学院\n计算机与软件学院-王韵璐","_VAR_OWNER_ACCOUNT":"201883290620","_VAR_ACTION_ORGANIZES_Names":"计算机与软件学院-王韵璐\n计算机与软件学院","_VAR_STEP_CODE":"Tbxx","_VAR_OWNER_USERCODES":"201883290620","_VAR_EXECUTE_ORGANIZES_Codes":"20900-850319","_VAR_NOW_DAY":"6","_VAR_OWNER_EMAIL":"201883290620@nuist.edu.cn","_VAR_OWNER_REALNAME":"褚午杰","_VAR_NOW":"1612583121","_VAR_URL_Attr":"{}","_VAR_ENTRY_NUMBER":"3780854","_VAR_EXECUTE_INDEP_ORGANIZES_Names":"计算机与软件学院-王韵璐","_VAR_STEP_NUMBER":"3963215","_VAR_POSITIONS":"20900-850319:002:201883290620\n20900:2","_VAR_EXECUTE_INDEP_ORGANIZES_Codes":"20900-850319","_VAR_EXECUTE_POSITIONS":"20900-850319:002:201883290620","_VAR_ACTION_ORGANIZES_Codes":"20900-850319\n20900","_VAR_EXECUTE_INDEP_ORGANIZE":"20900-850319","_VAR_NOW_YEAR":"2021","groupMQJCRList":[0],"fieldFLid":"","fieldSQSJ":1612583121,"fieldJBXXxm":"201883290620","fieldJBXXxm_Name":"褚午杰","fieldJBXXgh":"201883290620","fieldJBXXxb":"1","fieldJBXXxb_Name":"男（male）","fieldJBXXlxfs":"15952532002","fieldJBXXdw":"20900-850319","fieldJBXXdw_Name":"计算机与软件学院-王韵璐","fieldJBXXnj":"18软工1班","fieldJBXXsfzh":"321023200006060415","fieldJBXXJG":"1","fieldJBXXcsny":"","fieldJBXXfdyxm":"","fieldJBXXfdyxm_Name":"","fieldJBXXfdygh":"","fieldJBXXjgs":"320000","fieldJBXXjgs_Name":"江苏省","fieldJBXXjgshi":"321000","fieldJBXXjgshi_Name":"扬州市","fieldJBXXjgshi_Attr":"{\"_parent\":\"320000\"}","fieldJBXXjgq":"321023","fieldJBXXjgq_Name":"宝应县","fieldJBXXjgq_Attr":"{\"_parent\":\"321000\"}","fieldJBXXjgsjtdz":"","fieldJBXXjjlxr":"顾云莉","fieldJBXXjjlxrdh":"13651512136","fieldSTQKsfstbs":"1","fieldSTQKks":false,"fieldSTQKgm":false,"fieldSTQKfs":false,"fieldSTQKfl":false,"fieldSTQKhxkn":false,"fieldSTQKfx":false,"fieldSTQKqt":false,"fieldSTQKqtms":"","fieldSTQKfrtw":"36.6","fieldWXTS":"温馨提示：体温若超过37.3℃，请带好口罩至学校医务所复测！","fieldSTQKqtqksm":"","fieldSTQKdqstzk":"","fieldSTQKglsjrq":"","fieldSTQKglsjsf":"","fieldSTQKfrsjrq":"","fieldSTQKfrsjsf":"","fieldCXXXcxzt":"1","fieldCXXXjtzz":"320000","fieldCXXXjtzz_Name":"江苏省","fieldCXXXjtzzs":"321000","fieldCXXXjtzzs_Name":"扬州市","fieldCXXXjtzzs_Attr":"{\"_parent\":\"320000\"}","fieldCXXXjtzzq":"321023","fieldCXXXjtzzq_Name":"宝应县","fieldCXXXjtzzq_Attr":"{\"_parent\":\"321000\"}","fieldCXXXjtjtzz":"五洲国际","fieldCXXXfxxq":"1","fieldCXXXfxxq_Name":"南京校区","fieldCXXXssh":"","fieldCXXXdqszd":"","fieldCXXXcqwdq":"","fieldCXXXfxcfsj":"","fieldCXXXjtfsfj":false,"fieldCXXXjtfshc":false,"fieldCXXXjtfsdb":false,"fieldCXXXjtfspc":false,"fieldCXXXjtfslc":false,"fieldCXXXjtfsqt":false,"fieldCXXXjtfsqtms":"","fieldCXXXjtgjbc":"","fieldYQJLjrsfczbl":"2","fieldYQJLjrsfczbldqzt":"","fieldYQJLsfjcqtbl":"2","fieldCXXXsftjwh":"","fieldCXXXsftjhb":"2","fieldCXXXsftjhbss":"","fieldCXXXsftjhbss_Name":"","fieldCXXXsftjhbs":"","fieldCXXXsftjhbs_Name":"","fieldCXXXsftjhbs_Attr":"{\"_parent\":\"\"}","fieldCXXXsftjhbq":"","fieldCXXXsftjhbq_Name":"","fieldCXXXsftjhbq_Attr":"{\"_parent\":\"\"}","fieldCXXXsftjhbjtdz":"","fieldYC":"420000","fieldMQJCRxh":[1],"fieldMQJCRxm":[""],"fieldMQJCRlxfs":[""],"fieldMQJCRcjdd":[""],"fieldCNS":true,"_VAR_ENTRY_NAME":"学生健康状况申报","_VAR_ENTRY_TAGS":"学工部"}'
        }
header2 = {'Referer':'http://e-office2.nuist.edu.cn/infoplus/form/XNYQSB/start' ,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
           'Origin': 'http://e-office2.nuist.edu.cn',
           }
r2 = s.post(url2, data = data2 , cookies=cookieNew,headers=header2)
print(r2.text)
targetUrl = json.loads(r2.text)['entities'][0]
stepId = int(targetUrl.split('/')[5])
t2 = int(time.time())
formData2 = formDatainp
postData2={
    'actionId':1,
    'formData' : formData2,
    'remark':'',
    'rand': 185.43415117494698,
    'nextUsers':'{}',
    'stepId':stepId,
    'timestamp':t2,
    'boundFields':'fieldCXXXjtgjbc,fieldMQJCRxh,fieldCXXXsftjhb,fieldSTQKqt,fieldSTQKglsjrq,fieldYQJLjrsfczbldqzt,fieldCXXXjtfsqtms,fieldCXXXjtfsfj,fieldJBXXjjlxrdh,fieldJBXXxm,fieldJBXXjgsjtdz,fieldCXXXsftjhbss,fieldSTQKfrtw,fieldMQJCRxm,fieldCXXXsftjhbq,fieldSTQKqtms,fieldCXXXjtfslc,fieldJBXXlxfs,fieldJBXXxb,fieldCXXXjtfspc,fieldYQJLsfjcqtbl,fieldCXXXssh,fieldJBXXgh,fieldCNS,fieldYC,fieldSTQKfl,fieldCXXXsftjwh,fieldCXXXfxxq,fieldSTQKdqstzk,fieldSTQKhxkn,fieldSTQKqtqksm,fieldFLid,fieldYQJLjrsfczbl,fieldJBXXjjlxr,fieldCXXXfxcfsj,fieldMQJCRcjdd,fieldSQSJ,fieldSTQKfrsjrq,fieldSTQKks,fieldJBXXcsny,fieldSTQKgm,fieldJBXXnj,fieldCXXXjtzzq,fieldJBXXJG,fieldCXXXdqszd,fieldCXXXjtzzs,fieldSTQKfx,fieldSTQKfs,fieldCXXXjtfsdb,fieldCXXXcxzt,fieldCXXXjtfshc,fieldCXXXjtjtzz,fieldCXXXsftjhbs,fieldJBXXsfzh,fieldSTQKsfstbs,fieldCXXXcqwdq,fieldJBXXfdygh,fieldJBXXjgshi,fieldJBXXfdyxm,fieldWXTS,fieldCXXXjtzz,fieldJBXXjgq,fieldCXXXjtfsqt,fieldJBXXjgs,fieldSTQKfrsjsf,fieldSTQKglsjsf,fieldJBXXdw,fieldCXXXsftjhbjtdz,fieldMQJCRlxfs',
    'csrfToken':csrfToken,
    'lang':'zh',
}

url3 = 'http://e-office2.nuist.edu.cn/infoplus/interface/doAction'
header3 = {'Referer':'http://e-office2.nuist.edu.cn/infoplus/form/'+str(stepId)+'/render' ,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
           'Origin': 'http://e-office2.nuist.edu.cn',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          }
r3 = s.post(url3, data = postData2 , cookies=cookieNew,headers=header3)
print(r3.text)
