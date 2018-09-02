# -*- coding:utf-8 -*-
import requests
import re
import urllib.request
from bs4 import BeautifulSoup
from FileOperation import DownloadHTMLFile, getIndex, getFinishMissionQueue, pushInFinishMissionQueue

class RP(object):
	def __init__(self, url, session = ['16','17']):
		self.__dept, self.__url, self.__L2, self.__session = getIndex(), url, getFinishMissionQueue("data2.ck"), session,
		self.__FILTER = {
			'bgcolor': "White",
			'border': "0",
			'bordercolor': "White",
			'cellpadding': "3",
			'cellspacing': "1",
			'class': "9",
			'id': "HuoGridView",
			'width': "1000"
		}

	def __getHiddenCode(self):
		html = requests.post(self.__url)
		VIEWSTATE = re.findall(
			r'<input type="hidden" name="__VIEWSTATE" '
			r'id="__VIEWSTATE" value="(.*?)" />', html.text, re.I)
		EVENTVALIDATION = re.findall(
			r'input type="hidden" name="__EVENTVALIDATION" '
			r'id="__EVENTVALIDATION" value="(.*?)" />', html.text, re.I)
		VIEWSTATEGENERATOR = re.findall(
			r'<input type="hidden" name="__VIEWSTATEGENERATOR" '
			r'id="__VIEWSTATEGENERATOR" value="(.*?)" />', html.text, re.I)
		return VIEWSTATE[0], EVENTVALIDATION[0], VIEWSTATEGENERATOR[0]

	def __getPostData(self, id, VIEWSTATE, EVENTVALIDATION, VIEWSTATEGENERATOR):
		return {
			'__VIEWSTATE': VIEWSTATE,
			'__EVENTVALIDATION': EVENTVALIDATION,
			'__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
			'Button1': u'搜索',
			'TextBox1': id,
		}

	def getHTMLPage(self, index):
		postdata = self.__getPostData(index, *(self.__getHiddenCode()))
		postdata = urllib.parse.urlencode(postdata).encode(encoding='UTF8')
		request = urllib.request.Request(self.__url)
		response = urllib.request.urlopen(request, data=postdata, timeout=60)
		soup = BeautifulSoup(response.read(), 'html.parser')
		html = soup.findAll('table', self.__FILTER)
		return html

	def running1(self):
		for dept_id in self.__dept:
			for th in self.__session:
				class_id, border2 = 1, 0
				while class_id < 10:
					student_id, border = 1, 0
					if border2 > 2:
						print('Class number reached the boundary value.')
						break
					class_id = str('0' + str(class_id) if int(class_id) < 10 else str(class_id))

					while student_id < 60:
						student_id = str('0' + str(student_id) if int(student_id) < 10 else str(student_id))
						index = dept_id + th + class_id + student_id
						if self.L2:
							if index in self.L2:
								print(index, "is repeat student number.")
								student_id = int(student_id) + 1
								continue
						try:
							html = self.getHTMLPage(index)
							if html:
								print(index, 'Downloading...')
								pushInFinishMissionQueue(index)
								DownloadHTMLFile(index, html[0])
							else:
								border += 1
								print(index, 'is none.')
								if border > 5:
									border2 += 1
									break
						# time.sleep(1)
						except:
							print("oops! Need to hang for 20 seconds.")
							# time.sleep(60)
							student_id = int(student_id)
							continue

						student_id = int(student_id) + 1
					class_id = int(class_id) + 1
		# time.sleep(60)

	def running2(self):
		L2 = getFinishMissionQueue()
		for i in range(1, 20):
			for j in range(1, 10):
				k = 1
				while k < 15:
					index = str('0' + str(i) if i < 10 else str(i)) + '-' + str(j) + str(
						'0' + str(k) if k < 10 else str(k))
					if index in L2:
						k += 1
						print('\033[0;31;', index + "\'s 0mpage have alread downloaded.\033[0m")
						continue
					try:
						html = self.getHTMLPage(index)
						if html:
							DownloadHTMLFile(index, html[0])
							pushInFinishMissionQueue(index)
						else:
							print(index + "\033[0;31;0m is none\033[0m")
					except:
						print("oops! Need to hang for 20 seconds.")
						continue
					k += 1
					# time.sleep(1)
