import urllib2
from bs4 import BeautifulSoup

class ZhihuSpider(object):
    def __init__(self):
        pass

    def get_all_questions(self, topic_id):
        url_list = self.get_pages(topic_id)
        questions_url = []
        for url in url_list:
            response = urllib2.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html)
            for link in soup.find_all('a'):
                question_url = str(link.get('href'))
                if question_url.find("question") != -1:
                    questions_url.append("http://www.zhihu.com" + question_url)
        return questions_url

    def get_pages(self, topic_id):
        url = "http://www.zhihu.com/topic/" + str(topic_id) + "/questions"
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        page_len = 0
        for link in soup.find_all("a"):
            page_url = str(link.get("href"))
            if page_url.find("page") != -1:
                page_len = max(page_len, int(page_url.split("=")[1]))
        url_list = []
        for page_id in range(1, page_len+1):
            url_list.append("http://www.zhihu.com/topic/" + str(topic_id) + "/questions?pages=" + str(page_id))
        return url_list

    
    def run(self):
        for question_url in self.get_all_questions(19554298):
            print question_url

