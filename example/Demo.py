# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author  : jingle1267
@Time    : 2019-07-20 05:09
@desc：  : 
"""
import os

from md2xmind import Main


def main():
	print('example main')
	file_path = os.path.abspath(os.path.join(os.getcwd(), 'test2.md'))

	Main.main(file_path, 'test2')


if __name__ == '__main__':
	main()
