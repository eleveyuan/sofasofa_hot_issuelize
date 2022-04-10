# coding=utf-8
import requests
from bs4 import BeautifulSoup


class Parser:
    def get_page(self, url):
        res = requests.get(url)
        self.content = res.content.decode('utf-8')
        self.soup = BeautifulSoup(self.content, 'lxml')

    def get_question(self):
        return self.soup.find('h1').string

    def get_viewer(self):
        tags = []
        for tag in self.soup.find_all('a', attrs={"class": ["tag_link", "m-r"]}):
            print(tag)
            tags.append(tag.string)
        return tags

    def get_tags(self):
        pass

    def get_answer(self):
        pass