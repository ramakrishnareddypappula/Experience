import time

import os
print("hellow world")

for key, val in os.environ.items():
    if key == "NEWVAR":
        print(val)
    if key == "SLEEPTIME":
        sleeptime=val # Get values from DOCKER FILE.

time.sleep(int(sleeptime))  # sleeptime will be string.