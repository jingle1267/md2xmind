# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-07-20 05:09
@desc：  : 
"""
import os

import md2xmind


def main():
	# print('example main')
	file_path = os.path.abspath(os.path.join(os.getcwd(), 'test2.md'))

	md2xmind.start_trans_file(file_path, 'test2', 'test22')

	with open(file_path, 'r', encoding='utf-8') as f:
		md_content = f.read()
		md2xmind.start_trans_content(md_content, '222', '222')


if __name__ == '__main__':
	main()
