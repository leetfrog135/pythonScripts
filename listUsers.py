import os
import time
import datetime

now = datetime.datetime.now()

def loopF():
        os.system('who')
        time.sleep(5)

while True:
        print
        print("Time of event: " + now.strftime("%d-%m-%Y %H:%M"))
        print
        print("Users currently logged in:")
        print
        loopF()
        print

