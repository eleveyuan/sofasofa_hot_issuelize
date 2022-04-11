# -*- coding: utf-8 -*-
import os
import json

from jinja2 import Environment, FileSystemLoader

# 加载模板
env = Environment(loader=FileSystemLoader('../templates'))
template = env.get_template('sofa_template.html')


# 渲染模板
def render(data):
    question_id = data['id']
    question = data['question']
    question_desc = data['description']
    question_viewer = data['viewer']
    question_tags = data['tags']
    question_answer = data['answers']
    save(template.render(id=question_id,
                          question=question,
                          tags=question_tags,
                          description=question_desc,
                          answers=question_answer), question_id + '.html')


# 保存渲染数据
def save(rendered, name, path='../data/rendered'):
    with open(os.path.join(path, name), 'w', encoding='utf-8') as f:
        f.writelines(rendered)


# 加载数据
path_ = '../data/output'
for _, _, c in os.walk(path_):
    for file in c:
        file_path = os.path.join(path_, file)
        with open(file_path, 'r') as fr:
            json_data = json.load(fr)
            render(json_data)
