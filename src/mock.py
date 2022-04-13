import time
import threading
from collections import defaultdict

import pandas as pd
import requests

# 缺少1022026
base_url = 'http://sofasofa.io/forum_main_post.php?postid='
path = '../data'


class MockThread(threading.Thread):
    def __init__(self, url_ids, path):
        threading.Thread.__init__(self)
        self.url_ids = url_ids
        self.path = path

    def run(self):
        mock_and_save(self.url_ids, self.path)


def mock_and_save(url_ids, path_):
    for url_id in url_ids:
        url = base_url + str(url_id)
        r = requests.get(url, allow_redirects=False)
        print(f'mock url {url}, and get status code {r.status_code}\n')
        with open(path_, 'a+') as fw:
            fw.write(','.join([url, str(r.status_code)]) + '\n')
        time.sleep(0.1)


ids = [_id for _id in range(1650000, 1656092, 1)]
n = 5
ids_split = defaultdict(list)
for i in range(n):
    ids_split[i] = []
for i in range(len(ids)):
    ids_split[i % n].append(ids[i])

threadz = []
for k, v in ids_split.items():
    threadz.append(MockThread(ids_split[k], f'{path}/mock{str(k)}.csv'))

for i in range(len(threadz)):
    threadz[i].start()