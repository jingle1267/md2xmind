# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-07-20 05:05
@desc：  : 
"""
from md2xmind.Md2Xmind import process_file
from md2xmind.Md2Xmind import process_content


# 把 Markdown 格式的文档转换为 xmind 格式的文档
# 1. md_file 需要被转换的文档路径
# 2. target_file_name 生成的文件名称或路径。注意：如果文件已经存在则会删除重建
def start_trans_file(md_file, target_file_name):
	return start_trans_file(md_file, target_file_name, '')


# 把 Markdown 格式的文档转换为 xmind 格式的文档
# 1. md_file 需要被转换的文档路径
# 2. target_file_name 生成的文件名称或路径。注意：如果文件已经存在则会删除重建
# 3. topic_name 生成的思维导图的主题
def start_trans_file(md_file, target_file_name, topic_name):
	return process_file(md_file, target_file_name, topic_name)


# 把 Markdown 格式的文档转换为 xmind 格式的文档
# 1. md_content Markdown 格式的文本字符串
# 2. target_file_name 生成的文件名称或路径。注意：如果文件已经存在则会删除重建
# 3. topic_name 生成的思维导图的主题
def start_trans_content(md_content, target_file_name, topic_name):
	return process_content(md_content, target_file_name, topic_name)
