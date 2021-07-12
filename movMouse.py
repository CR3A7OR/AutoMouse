import pyautogui
import time
import sys
import random
from datetime import datetime
import bezier
import numpy as np

pyautogui.FAILSAFE = False
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0

numMin = None
print("Running")
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 2
else:
    numMin = int(sys.argv[1])

#Change amount of coordinates ran through
positions = 4
coordinates = []
while(True):
    j = 0
    time.sleep(numMin * 60)
    print("Movement made at {}".format(datetime.now().time()))
    while(j < positions):
        coordinates.clear()  
        rn = random.randint(1, 1920)
        rn2 = random.randint(1, 1080)
        coords = tuple([rn,rn2])
        coordinates.append(coords)

        start = pyautogui.position()
        end = coordinates[0][0], coordinates[0][1]

        #Intermediate control points that may be adjusted to modify the curve.
        control1 = start[0]+random.randint(50, 125), start[1]+random.randint(25, 100)
        #control2 = start[0]+random.randint(150, 375), start[1]+random.randint(1, 50)

        # Format points to use with bezier
        control_points = np.array([start, control1, end])
        points = np.array([control_points[:,0], control_points[:,1]]) # Split x and y coordinates

        # Set the degree of the curve here, should be less than # of control points
        degree = 2
        # Create the bezier curve
        curve = bezier.Curve(points, degree)

        curve_steps = 50  # How many points the curve should be split into. Each is a separate pyautogui.moveTo() execution
        delay = 1/curve_steps  # Time between movements. 1/curve_steps = 1 second for entire curve

        for i in range(1, curve_steps+1):
            # The evaluate method takes a float from [0.0, 1.0] and returns the coordinates at that point in the curve
            # Another way of thinking about it is that i/steps gets the coordinates at (100*i/steps) percent into the curve
            x, y = curve.evaluate(i/curve_steps)
            pyautogui.moveTo(x, y) 
            pyautogui.sleep(delay)
        
        j = j + 1
        
        for i in range(0,3):
            pyautogui.press("shift")




