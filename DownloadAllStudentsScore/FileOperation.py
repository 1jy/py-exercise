# -*- coding:utf-8 -*-
import codecs

def DownloadHTMLFile(index, content):
        print(index, "\033[0;92;0mDownloading...\033[0m")
        #path = 'files/'
        path = 'files/sdf/'
        filename = path + index + '.html'
        fd = codecs.open(filename, 'w')
        fd.write(str(content))
        fd.close()

def getIndex():
        fd = codecs.open("dept_id.d", 'r')
        deptid_list = []
        while 1:
            line = fd.readline()
            if not line:
                break
            deptid_list.append(line[0:4])
        fd.close()
        return deptid_list

def getFinishMissionQueue(name):
        fd = codecs.open(name, 'r',encoding="utf-8")
        finsh_mission_list = []
        while 1:
            line = fd.readline()
            if not line:
                break
            finsh_mission_list.append(line[0:-2])
        fd.close()
        return set(finsh_mission_list)

def getDataBase(name):
          fd = codecs.open(name, 'r', encoding="utf-8")
          finsh_mission_list = []
          while 1:
            line = fd.readline()
            if not line:
              break
            finsh_mission_list.append(line[0:-1])
          fd.close()
          return set(finsh_mission_list)
		  
def pushInFinishMissionQueue(id):
        print(id + "'s \033[0;33;0m Page Download is Complete.\033[0m")
        fd = codecs.open("data2.ck", 'a')
        fd.write(id + '\n')
        fd.close()


