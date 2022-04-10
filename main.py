# coding=utf-8
import time
import os

import pandas as pd
import requests

from src import urls_getter
from src import page_parser

root_url = "http://sofasofa.io/"  # 主站地址
page_interface = "http://sofasofa.io/public_forum_exe.php?action=load_more"  # 分页请求接口

url_pools = './data/main/urls_pool.csv'
url_pools_df = None
if os.path.exists(url_pools):
    url_pools_df = pd.read_csv(url_pools, index_col=[0])
else:
    with open(url_pools, 'a+') as fw:
        for i in range(171):
            print('*' * 100)
            print(f'get {i}th page')
            payload = {"start": i*10, "filter": None, "type": 0}  # 接口传递参数
            get_url = urls_getter.UrlGetter()
            get_url.get_entities(root_url, page_interface, 'POST', payload)
            titles = get_url.get_urls()
            fw.writelines('\n'.join(titles))
            fw.write('\n')
            time.sleep(0.1)

    url_pools_df = pd.read_csv(url_pools, header=None)
    url_pools_df.columns = ['url']
    url_pools_df = url_pools_df.sort_values(by='url').reset_index(drop=True)
    url_pools_df.to_csv(url_pools)

parse_page = page_parser.Parser()
for question_url in titles:
    print('*'*100)
    print(f'get page of {question_url}')
    parse_page.get_page(question_url)
    title = parse_page.get_question()
    parse_page.get_tags()
    break
