# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-07-20 05:07
@desc：  : 
"""
import os

import xmind


def main(md_file, target_file_name):
	print('main {0}'.format(md_file))

	if '.xmind' not in target_file_name:
		target_file_name += '.xmind'

	# 如果目标文件存在则删除
	target_file_path = os.path.abspath(os.path.join(os.getcwd(), target_file_name))
	# print(target_file_path)
	if os.path.exists(target_file_path):
		print('目标文件存在且已删除')
		os.remove(target_file_path)

	# 1、如果指定的XMind文件存在，则加载，否则创建一个新的
	workbook = xmind.load(target_file_name)

	# 2、获取第一个画布（Sheet），默认新建一个XMind文件时，自动创建一个空白的画布
	sheet1 = workbook.getPrimarySheet()

	# 3、在画布上生成思维导图
	handle_file(md_file, sheet1)

	# 4、保存（如果指定path参数，另存为该文件名）
	xmind.save(workbook)

	print('生成思维导图完成')


def handle_file(md_file, sheet1):
	f = open(md_file, 'r')

	topic_name = get_file_name(md_file)
	print(md_file)

	global root_topic
	global level2_topic
	global level3_topic
	global level4_topic
	global level5_topic

	root_topic = sheet1.getRootTopic()
	root_topic.setTitle(topic_name)
	level2_topic = None
	level3_topic = None
	level4_topic = None
	level5_topic = None

	line = f.readline()
	i = 1
	while line:
		line = line.strip()
		# print(line)

		if line.startswith('#'):
			if line.startswith('# '):
				title = line.replace('# ', '')
				root_topic = get_super_topic(1, root_topic, level2_topic, level3_topic, level4_topic)
				root_topic.setTitle(title)
			elif line.startswith('## '):
				title = line.replace('## ', '')
				root_topic = get_super_topic(2, root_topic, level2_topic, level3_topic, level4_topic)
				level2_topic = root_topic.addSubTopic()
				level2_topic.setTitle(title)
			elif line.startswith('### '):
				title = line.replace('### ', '')
				level2_topic = get_super_topic(3, root_topic, level2_topic, level3_topic, level4_topic)
				level3_topic = level2_topic.addSubTopic()
				level3_topic.setTitle(title)
			elif line.startswith('#### '):
				title = line.replace('#### ', '')
				level3_topic = get_super_topic(4, root_topic, level2_topic, level3_topic, level4_topic)
				level4_topic = level3_topic.addSubTopic()
				level4_topic.setTitle(title)
			elif line.startswith('##### '):
				title = line.replace('###### ', '')
				level4_topic = get_super_topic(5, root_topic, level2_topic, level3_topic, level4_topic)
				level5_topic = level4_topic.addSubTopic()
				level5_topic.setTitle(title)
			else:
				print('暂不支持更多层级展示')

		# print('level {0} topic {1}'.format(level, topic))
		else:
			print('第 {0} 行不是#开始，内容{1}'.format(i, line))

		i += 1
		line = f.readline()


def get_super_topic(level, root_topic, level2_topic, level3_topic, level4_topic):
	if level == 5:
		if level4_topic is None:
			level4_topic = get_super_topic(4, root_topic, level2_topic, level3_topic, level4_topic)
		return level4_topic

	elif level == 4:
		if level3_topic is None:
			level3_topic = get_super_topic(3, root_topic, level2_topic, level3_topic, level4_topic)
		return level3_topic

	elif level == 3:
		if level2_topic is None:
			level2_topic = get_super_topic(2, root_topic, level2_topic, level3_topic, level4_topic)
		return level2_topic

	elif level == 2:
		if root_topic is None:
			root_topic = get_super_topic(1, root_topic, level2_topic, level3_topic, level4_topic)
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


if __name__ == '__main__':
	main()
