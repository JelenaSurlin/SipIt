#!usr/bin/python3

import datetime
import time
from datetime import datetime



class myLogging:
    def __init__ (self,logfile):
        self.logfile=logfile
    def openFile(self):
        self.now = datetime.now()
        trynum=10
        while trynum>0:
            trynum=trynum-1
            try:
                self.logfile_h=open(self.logfile,"a+")
                return True
                break
            except:
                time.sleep(0.01)
            if trynum==0:
                print(self.now.strftime("%Y.%m.%d %H:%M:%S") + " log file buzzy !")
                return False
    def debug(self,logstr):
        if self.openFile():
            self.logfile_h.write(self.now.strftime("%Y.%m.%d %H:%M:%S") + " DEBUG " + str(logstr) + "\n")
            self.logfile_h.close()
    def info(self,logstr):
        self.openFile()
        self.logfile_h.write(self.now.strftime("%Y.%m.%d %H:%M:%S") + " INFO " + str(logstr) + "\n")
        self.logfile_h.close()
    def warning(self,logstr):
        self.openFile()
        self.logfile_h.write(self.now.strftime("%Y.%m.%d %H:%M:%S") + " WARNING " + str(logstr) + "\n")
        self.logfile_h.close()
    def critical(self,logstr):
        self.openFile()
        self.logfile_h.write(self.now.strftime("%Y.%m.%d %H:%M:%S") + " CRITICAL " + str(logstr) + "\n")
        self.logfile_h.close()



