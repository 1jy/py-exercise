# -*- coding:utf-8 -*-
import codecs
import time
import matplotlib.pyplot as plt
import FileOperation
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def importData():
		score = []
		fd = codecs.open('output_data.txt', 'r+')
		while 1:
				line = fd.readline().decode('utf-8')
				if not line:
						break
				score.append(line)
		fd.close()
		return score

def getData():
		data, class_name, score, index, items = [], [], {}, 0, importData()
		for item in items:
				data.append(list(item.rstrip().split("\t")))
				class_name.append(data[index][5])
				index += 1
		class_name = set(class_name)

		for k in class_name:
				test = []
				for item in data:
						s = 0 if not item[-1][:-1].isdigit() else int(item[-1])
						if item[5] == k:
								test.append(s)
				score[k] = test
		return class_name, score, data

def scoreVisual(class_name, score, data):
		for k in class_name:
				plt.title(k + u' 总评成绩汇总', fontsize=18)
				plt.ylabel('分数', fontsize = 14)
				plt.xlabel('人数(总人数 ' + str(len(score[k])) + ')', fontsize = 14)
				plt.plot(sorted(score[k]))
				time.sleep(1)
				plt.show()
				#plt.savefig('files\\cvs\\'+ k + '.png') #save pic
				plt.close()

def running():
		scoreVisual(*getData())
