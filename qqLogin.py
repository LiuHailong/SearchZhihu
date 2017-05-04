#coding=utf-8

import requests
from bs4 import BeautifulSoup

def login(question_url):
    login_url = 'http://www.zhihu.com/login/email'
    login_data = {
        'email': "787346616@qq.com", 
        'password': "ds931026",
        'rememberme': 'true',
    }
    headers_base = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
        'Referer': 'http://www.zhihu.com/',
        'X-Requested-With': "XMLHttpRequest",
        'cookie':'_za=ce89fd8b-806d-4b13-a54e-e3c820e837a7; _xsrf=614f18be8b94b1b6910c434fda77969c; r_c=1; _ga=GA1.2.540904587.1436407206; tc=AQAAAEFGCzme2QkAIaaI01/wutNidXY6; q_c1=6ce4035d4962418fb3846df8bafd05e9|1439171232000|1436407206000; cap_id="MGJmOTYyNzY4YjA5NDJkYmI5NDM1OGU0YmIyMDU0YmI=|1439530555|37c379d0f625b2f0986b8fc0fe3e848442f0dcad"; z_c0="QUFEQWVOVWVBQUFYQUFBQVlRSlZUU2xPQTFiNWhqSEFYbUEwUHYzbUlzZGM1NVBuellRU1hnPT0=|1440465194|973c981ba0d671f4f70545e597e3410da554d693"; n_c=1; __utma=51854390.540904587.1436407206.1440464715.1440472197.36; __utmb=51854390.4.10.1440472197; __utmc=51854390; __utmz=51854390.1440464715.35.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20131007=1^3=entry_date=20131007=1'
    }

#     s = requests.session()

#     res = s.post(login_url, headers=headers_base, data=login_data)
#     print res.status_code
#     print res.reason
#     print res.json()
#     print res.json()['msg']
#     print res.json()['data']['captcha']
#     m_cookies = res.cookies
#     print m_cookies
    
    res = requests.get(question_url, headers=headers_base)
    soup = BeautifulSoup(res.text,'html.parser')
#     print len(soup.find_all(attrs={"itemtype":"http://schema.org/Answer"}))
    return res.text
 

def work():
#     login("http://www.zhihu.com/question/34852948")
    print login("http://www.zhihu.com/question/19557358")
 
if __name__ == '__main__':
    work()