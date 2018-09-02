# -*- coding:utf-8 -*-
import socket
from ResponseProcessing import RP
from DataCleaning import DC
from CheckUpdate import *
#from DataVisualization import running as DV
URL = #
socket.setdefaulttimeout(3)

rp = RP(URL)
dc = DC()
cu = CU(URL)
#dc.running()
cu.running()
#rp.running2()
#DV()
