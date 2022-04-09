# coding=utf-8
import requests

root_url = "http://sofasofa.io/"  # 主站地址
base_url = "http://sofasofa.io/forum_main_post.php?postid=1656072"  # 问题详情页地址


page_interface = "http://sofasofa.io/public_forum_exe.php?action=load_more"  # 分页请求接口
payload = {"start": 20, "filter": None, "type": 0}  # 接口传递参数

ret = requests.get(base_url)
print(ret.content.decode('utf-8'))