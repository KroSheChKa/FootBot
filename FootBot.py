import keyboard
import mss
import cv2
import numpy
from time import sleep
import win32api

# Set the window scale to 150%
# Game - https://vk.com/app8013553

# Moves the cursor to x,y coordinates
def move(x,y):
    win32api.SetCursorPos((x,y))

sleep(1.5)

# Mss is faster than PIL and even more than pyautogui
mss_ = mss.mss()

# Football field (game area)
field = {'left': 747,'top': 980,'width': 461,'height': 210}

# Read the image
ball_img = cv2.imread('Ball.png')

# Getting width and height of the image
w = ball_img.shape[1]
h = ball_img.shape[0]

# Press Q to quit the program
while keyboard.is_pressed('q') == False:

    # Limiting the cursor movement area
    win32api.ClipCursor((870,1160,1083,1161))

    # Grabbing screenshot
    screenshot = numpy.array(mss_.grab(field))

    # Delete the unnecessary alpha channel
    screenshot_removed = screenshot[:,:,:3]

    # Getting confidence and location of the ball
    ball = cv2.matchTemplate(screenshot_removed, ball_img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(ball)

    #print(f"Max Val: {max_val} Max Loc: {max_loc}")

    # Moving cursor right bellow the ball
    move((max_loc[0]+747+ w//2), 1161)
    
    # Putting a circle above the ball
    cv2.circle(screenshot, (max_loc[0] + w//2, max_loc[1]+ h//2), 20, (0,0,255), 4)

    # Showing the area
    cv2.imshow('Football', screenshot)
    cv2.waitKey(1)

else:

    # Width and height of the screen
    w_screen = win32api.GetSystemMetrics(0)
    h_screen = win32api.GetSystemMetrics(1)

    # As we set a limit area for cursor, we have to remove it
    win32api.ClipCursor((0,0,w_screen,h_screen))
