import pyautogui
import time
import sys
import random
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
print("Running")
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 2
else:
    numMin = int(sys.argv[1])

#j = 0
positions = 4
coordinates = []
while(True):
    coordinates.clear()  
    for i in range (0,positions):
        rn = random.randint(1, 1920)
        rn2 = random.randint(1, 1080)
        coords = tuple([rn,rn2])
        coordinates.append(coords)

    time.sleep(numMin * 60)
    pyautogui.moveTo(coordinates[0][0], coordinates[0][1],random.randint(2, 5))
    pyautogui.moveTo(coordinates[1][0], coordinates[1][1],random.randint(2, 5))
    pyautogui.moveTo(coordinates[2][0], coordinates[2][1],random.randint(2, 5))
    pyautogui.moveTo(coordinates[3][0], coordinates[3][0],random.randint(2, 5))
    #j = j + 1

    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))


