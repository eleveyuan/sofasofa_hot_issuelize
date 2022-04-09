# coding=utf-8
import requests
from bs4 import BeautifulSoup


class UrlGetter:
    def get_entities(self, root_url, interface, method='POST', payload=''):
        if method == 'POST':
            res = requests.request(method, interface, data=payload)
            self.root_url = root_url
            self.content = res.content.decode('utf-8')
        else:
            pass

    def get_urls(self):
        doc = self.content
        soup = BeautifulSoup(doc, "lxml")
        titles = []
        for item in soup.find_all('a', class_='title_link'):
            # titles.append({
            #     'title_name': item.string.strip(),
            #     'title_href': self.root_url + item.get('href')
            # })
            titles.append(self.root_url + item.get('href'))
        return titles




