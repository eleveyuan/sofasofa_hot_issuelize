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
        return int(self.soup.find_all('div', class_='container p-y')[0].find('span').string.strip().split('：')[1])

    def get_tags(self):
        tags = []
        # for tag in self.soup.find_all('a', attrs={"class": ["tag_link", "m-r"]}):
        for tag in self.soup.find_all('a', class_="tag_link m-r"):
            tags.append(tag.string.strip())
        return tags

    def get_answer(self):
        pass