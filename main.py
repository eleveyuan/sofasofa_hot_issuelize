# coding=utf-8
from src import urls_getter
from src import page_parser

root_url = "http://sofasofa.io/"  # 主站地址
page_interface = "http://sofasofa.io/public_forum_exe.php?action=load_more"  # 分页请求接口
payload = {"start": 0, "filter": None, "type": 0}  # 接口传递参数

get_url = urls_getter.UrlGetter()
get_url.get_entities(root_url, page_interface, 'POST', payload)
titles = get_url.get_urls()

parse_page = page_parser.Parser()
for question_url in titles:
    parse_page.get_page(question_url)