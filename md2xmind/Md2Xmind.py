# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-07-20 05:07
@desc：  : 
"""
import os
import sys

import xmind


class Md2Xmind:

	def main(md_content, target_file_name, topic_name):
		# print('main {0}'.format(md_file))

		if '.xmind' not in target_file_name:
			target_file_name += '.xmind'

		# 如果目标文件存在则删除
		target_file_path = os.path.abspath(os.path.join(os.getcwd(), target_file_name))
		# print(target_file_path)
		if os.path.exists(target_file_path):
			print('\033[1;35m目标文件存在且已删除 \033[0m')
			os.remove(target_file_path)

		# 1、如果指定的XMind文件存在，则加载，否则创建一个新的
		workbook = xmind.load(target_file_name)

		# 2、获取第一个画布（Sheet），默认新建一个XMind文件时，自动创建一个空白的画布
		sheet1 = workbook.getPrimarySheet()

		# 3、在画布上生成思维导图
		Md2Xmind.handle_content(md_content, sheet1, topic_name)

		# 4、保存（如果指定path参数，另存为该文件名）
		xmind.save(workbook)

		print('\033[1;32m{0} created \033[0m'.format(target_file_name))

	def handle_content(md_content, sheet1, topic_name):
		content_arr = md_content.split('\n')

		global root_topic
		global level2_topic
		global level3_topic
		global level4_topic
		global level5_topic
		global level6_topic

		root_topic = sheet1.getRootTopic()
		root_topic.setTitle(topic_name)
		level2_topic = None
		level3_topic = None
		level4_topic = None
		level5_topic = None
		level6_topic = None

		i = 1
		for line in content_arr:
			line = line.strip()
			# print(line)

			if line.startswith('#'):
				if line.startswith('# '):
					title = line.replace('# ', '')
					root_topic = Md2Xmind.get_super_topic(1, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
					root_topic.setTitle(title)
				elif line.startswith('## '):
					title = line.replace('## ', '')
					root_topic = Md2Xmind.get_super_topic(2, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
					level2_topic = root_topic.addSubTopic()
					level2_topic.setTitle(title)
				elif line.startswith('### '):
					title = line.replace('### ', '')
					level2_topic = Md2Xmind.get_super_topic(3, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
					level3_topic = level2_topic.addSubTopic()
					level3_topic.setTitle(title)
				elif line.startswith('#### '):
					title = line.replace('#### ', '')
					level3_topic = Md2Xmind.get_super_topic(4, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
					level4_topic = level3_topic.addSubTopic()
					level4_topic.setTitle(title)
				elif line.startswith('##### '):
					title = line.replace('##### ', '')
					level4_topic = Md2Xmind.get_super_topic(5, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
					level5_topic = level4_topic.addSubTopic()
					level5_topic.setTitle(title)
				elif line.startswith('###### '):
					title = line.replace('###### ', '')
					level5_topic = Md2Xmind.get_super_topic(6, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
					level6_topic = level5_topic.addSubTopic()
					level6_topic.setTitle(title)
				else:
					print('暂不支持更多层级展示')

			else:
				print('第 {0} 行不是#开始，内容{1}'.format(i, line))

			i += 1

	def get_super_topic(level, root_topic, level2_topic, level3_topic, level4_topic, level5_topic):
		if level == 6:
			if level5_topic is None:
				level5_topic = Md2Xmind.get_super_topic(5, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
			return level5_topic
		elif level == 5:
			if level4_topic is None:
				level4_topic = Md2Xmind.get_super_topic(4, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
			return level4_topic

		elif level == 4:
			if level3_topic is None:
				level3_topic = Md2Xmind.get_super_topic(3, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
			return level3_topic

		elif level == 3:
			if level2_topic is None:
				level2_topic = Md2Xmind.get_super_topic(2, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
			return level2_topic

		elif level == 2:
			if root_topic is None:
				root_topic = Md2Xmind.get_super_topic(1, root_topic, level2_topic, level3_topic, level4_topic, level5_topic)
			return root_topic

		elif level == 1:
			return root_topic

		else:
			print(level)

	def get_file_name(path):
		[dirname, filename] = os.path.split(path)
		arr = filename.split('.')
		i = 0
		topic_name = ''
		for item in arr:
			if i < len(arr) - 1:
				topic_name += item
			i += 1

		return topic_name


def process_file(md_file, target_file_name):
	process_file(md_file, target_file_name, '')


def process_file(md_file, target_file_name, topic_name):
	if not os.path.exists(md_file):
		print('\033[1;31m文件不存在： {0} \033[0m'.format(md_file))
		return

	with open(md_file, 'r', encoding='utf-8') as f:
		md_content = f.read()

		if topic_name == '':
			topic_name = Md2Xmind.get_file_name(md_file)
		process_content(md_content, target_file_name, topic_name)


def process_content(md_content, target_file_name, topic_name):
	if md_content.strip() == '' or len(md_content.strip()) == 0:
		print('\033[1;31mMarkdown 的内容太少 \033[0m')
		return
	Md2Xmind.main(md_content, target_file_name, topic_name)


if __name__ == '__main__':
	file_path = os.path.abspath(os.path.join(os.getcwd(), '../example/test1.md'))
	process_file(file_path, 'test2', 'test22')

	# with open(file_path) as f:
	# 	md_content = f.read()
	# process_content(md_content, '111', '111topic')
	# process_content('   ', '111', '111topic')
	# process_content('a', '111', '111topic')
