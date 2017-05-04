#coding=utf-8
import re
import qqLogin as login
from bs4 import BeautifulSoup

def get_question_info(question_url):
    url = str(question_url);
    html = login.login(url);
    soup = BeautifulSoup(html, "html.parser")
    #获取问题标题
    question_title = soup.h2.string.strip()
    #获取问题内容
    question_content = soup.find(id="zh-question-detail").find(class_="zm-editable-content").text
    #获取评论数，不过不太好，有的没有评论的话 就没有该ID树形，需要后面统计
    answers_num = soup.find(id="zh-question-answer-num").text
    
    
#     answers = []
    print question_title
    print question_content
    print answers_num
    
    for answer in soup.find_all(attrs={"itemtype":"http://schema.org/Answer"}):
        avatar = answer.find(attrs={"class":"zm-item-link-avatar"})
        if avatar==None:
            print "匿名用户"
        else:
            user_name = avatar.find_next_sibling("a")
            print user_name.text
            
        answer_content = answer.find(class_=re.compile("zm-editable-content")).text;
        print answer_content.strip()
        print '------'
        
        
        
# get_question_info("http://www.zhihu.com/question/34852948")
get_question_info("http://www.zhihu.com/question/19557358")