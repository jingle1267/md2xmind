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
	line = f.readline()
	i = 1
	while line:
		line = line.strip()
		# print(line)

		# super_topic = sheet1.getRootTopic()

		if line.startswith('#'):
			level = 0
			topic = ''
			if line.startswith('# '):
				level = 1
				topic = line.replace('# ', '')
				level1_topic = sheet1.getRootTopic()
				level1_topic.setTitle(topic)
			elif line.startswith('## '):
				level = 2
				topic = line.replace('## ', '')
				level2_topic = level1_topic.addSubTopic()
				level2_topic.setTitle(topic)
			elif line.startswith('### '):
				level = 3
				topic = line.replace('### ', '')
				level3_topic = level2_topic.addSubTopic()
				level3_topic.setTitle(topic)
			elif line.startswith('#### '):
				level = 4
				topic = line.replace('#### ', '')
				level4_topic = level3_topic.addSubTopic()
				level4_topic.setTitle(topic)
			elif line.startswith('##### '):
				level = 5
				topic = line.replace('###### ', '')
				level5_topic = level4_topic.addSubTopic()
				level5_topic.setTitle(topic)
			else:
				print('暂不支持更多层级展示')

		# print('level {0} topic {1}'.format(level, topic))
		else:
			print('第 {0} 行不是#开始，内容{1}'.format(i, line))

		i += 1
		line = f.readline()


if __name__ == '__main__':
	main()
