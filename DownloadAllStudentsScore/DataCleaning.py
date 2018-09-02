# -*- coding:utf-8 -*-
import codecs
import re
from bs4 import BeautifulSoup
from FileOperation import *

class DC:
    def __init__(self):
      self.__FILTER = {
            'tr':{"bgcolor":"#DEDFDE"},
            'font':{"color":"Black"}
            }
      self.__TAG = ['html', 'tr', 'font']

    def getPoints(self, id):
            path = r"files/sdf/"
            filename = path + id + '.html'
            fd_read = codecs.open(filename, 'r+')
            content = self.getContent(fd_read.read())
            if content != None:
                    print(id + "' Extract Success.")
                    codecs.open('output_data.txt', 'a+', encoding='utf8').write(content)
            else:
                    print(id + "' Extract Filed.")
            fd_read.close()

    def getContent(self, sourse):
            content = ""
            try:
                    self.__TAG[0] = sourse
                    temps = self.__TAG[0]
                    for tag in self.__TAG[1:-1]:
                            soup = BeautifulSoup(temps, 'html.parser')
                            temps = soup.findAll(tag, self.__FILTER[tag])
                            # print(temps)

                    for temp in temps:
                            soup = BeautifulSoup(str(temp), 'html.parser')
                            text_line = soup.findAll(self.__TAG[-1], self.__FILTER[self.__TAG[-1]])
                            line = ''
                            for text in text_line:
                                    line += text.string.strip() + '\t'
                            content += line[:-1] + '\n'
            except:
                    print("Oops. got a problem.")
                    return
            return content

    def running(self):
            ID_POOL = getFinishMissionQueue('data2.ck')
            for id in ID_POOL:
                    self.__getPoints(id)
            print('have done.')
