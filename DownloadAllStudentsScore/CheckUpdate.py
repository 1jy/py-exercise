# -*- coding:utf-8 -*-
import socket
from ResponseProcessing import RP
from DataCleaning import DC
from FileOperation import *
import time
import codecs
socket.setdefaulttimeout(3)
class CU(object):
        def __init__(self, url):
                self.__url = url
        def running(self):
                rp = RP(self.__url)
                dc = DC()
                ID_POOL, db = getFinishMissionQueue('data2.ck'), getDataBase("output_data.txt")

                for index in ID_POOL:
                        try:
                                newContent, counter = dc.getContent(str(rp.getHTMLPage(index))).split('\n')[:-1], 0
                                #print(newContent)
                        except:
                                print("oops, need hang for 1 mintue.")
                                time.sleep(60)
                                newContent = dc.getContent(str(rp.getHTMLPage(index))).split('\n')[:-1]
#
                        fd_write = codecs.open("output_data.txt", 'a+', encoding='utf-8')
                        for line in newContent:
                                if line not in db:
                                        fd_write.write(line + '\n')
                                        counter += 1
                        print(str(index) + ": There are " + ("no" if counter == 0 else str(counter))\
                              + " data update.")
                fd_write.close()

