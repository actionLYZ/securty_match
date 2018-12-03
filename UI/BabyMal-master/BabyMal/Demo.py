#! usr/bin/env python
# -*- coding: utf-8 -*-   
import os
import Global

def DoFilter(filterPath):
	'''
	1. Get api and corresponding function interpreter
	2. If both api and corresponding function interpreter have been in the
	storage, then same api and function interpreter won't be stored again
	'''
	count = 0

	with open(filterPath, 'r') as f:
		content = f.readlines()
		result = list(None for i in range(len(content)))

		for i in range(len(content)):
			# if on the last round, there is same api and function interpreter in the storage
			# then flag will be set true
			# and on the next round, flag will be reset
			flag = False
			if(content[i].find('返回地址') != -1):
				# if result is empty, then result[0] must be none
				if(result[0] == None):
					result[count] = content[i + 1]
					count += 1
				# Judge whether api and function interpreter have been in the list
				else:
					for j in range(len(result)):
						if content[i + 1] == result[j]:
							flag = True
							break;
					if flag == False:
						result[count] = content[i + 1]
						count += 1


	for i in range(count):
		Global.mainWindow.content_widget4.reportTextEdit.appendPlainText(result[i])
		Global.mainWindow.content_widget4.reportTextEdit.appendPlainText('\n')





