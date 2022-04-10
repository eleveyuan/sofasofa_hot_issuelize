# coding=utf-8
import re

import requests
from bs4 import BeautifulSoup


class Parser:
    def get_page(self, url):
        res = requests.get(url)
        self.content = res.content.decode('utf-8')
        self.soup = BeautifulSoup(self.content, 'lxml')

    def get_question(self):
        print('get question title')
        return self.soup.find('h1').string

    def get_question_desc(self):
        print('get question desc')
        desc = self.soup.find_all('div', class_='col-md-11 col-xs-10')
        # desc = self.soup.select('div[class="col-md-11 col-xs-10"]')
        desc = re.sub(r'<div style="max-width: 650px; float:left;"></div>', '', str(desc[0]))
        return desc

    def get_viewer(self):
        print('get number of viewer of question')
        return int(self.soup.find_all('div', class_='container p-y')[0].find('span').string.strip().split('：')[1])

    def get_tags(self):
        print('get tags of question ')
        tags = []
        # for tag in self.soup.find_all('a', attrs={"class": ["tag_link", "m-r"]}):
        for tag in self.soup.find_all('a', class_="tag_link m-r"):
            tags.append(tag.string.strip())
        return tags

    def get_answer(self):
        print('get answer of question')
        coarse_answers = self.soup.find_all('div', class_='col-md-11 col-xs-10 p-r')
        fined_answers = []
        for answer in coarse_answers:
            # first level comment
            lvl1_answer = re.sub(
                r'<a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a>',
                '', str(answer))
            lvl1_answer = re.sub(
                r'<a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a>',
                '', str(lvl1_answer))
            lvl1_answer = re.sub(
                r'<div style="height:2rem;">\s+<div class="modal fade" id="modalDeletePost">(\s.*)*</div>',
                '', str(lvl1_answer))
            # second leve comment
            lvl2_answers = []
            for lvl2_answer in answer.find_all('div', class_='col-xs-11'):
                lvl2_answer = re.sub(r'<div class="col-xs-11">', '', str(lvl2_answer))
                lvl2_answer = re.sub(r'- <a class="darkgray"(.*\s*)*', '', str(lvl2_answer))
                lvl2_answers.append(lvl2_answer.strip())
            fined_answers.append({'lvl1_answer': lvl1_answer + '</div>', 'lvl2_answer': lvl2_answers})
        return fined_answers
