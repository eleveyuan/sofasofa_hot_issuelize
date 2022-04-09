# coding=utf-8
import requests
from bs4 import BeautifulSoup


class Parser:
    def get_page(self, url):
        res = requests.get(url)
        self.content = res.content.decode('utf-8')

    def get_question(self):
        pass

    def get_viewer(self):
        pass

    def get_tags(self):
        pass

    def get_answer(self):
        pass