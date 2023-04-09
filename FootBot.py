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

def recount(n):
    #center_field = 978
    x = round((n - 231) * 0.7) + 231
    return x

sleep(1.5)

# Mss is faster than PIL and even more than pyautogui
mss_ = mss.mss()

# Football field (game area)
field = {'left': 747,'top': 990,'width': 462,'height': 200}

# Read the image
ball_img = cv2.imread('Ball.png', 0)

# Getting width and height of the image
w = ball_img.shape[1]
h = ball_img.shape[0]

# Limiting the cursor movement area
win32api.ClipCursor((870,1160,1084,1161))

# Press Q to quit the program
while keyboard.is_pressed('q') == False:

    # Grabbing screenshot
    screenshot = numpy.array(mss_.grab(field))
    screenshot_r = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # Delete the unnecessary alpha channel
    #screenshot_removed = screenshot_r[:,:,:3]

    # Getting confidence and location of the ball
    ball = cv2.matchTemplate(screenshot_r, ball_img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(ball)

    #print(f"Max Val: {max_val} Max Loc: {max_loc}")

    #new_x = recount((max_loc[0] + w//2))
    if max_val > 0.251:
    # Moving cursor right bellow the ball
    #move((new_x + 747), 1161)
        move((recount(max_loc[0]) + w//2 + 747), 1161)
    
    # Putting a circle above the ball
        #cv2.circle(screenshot_r, (max_loc[0] + w//2, max_loc[1]+ h//2), 20, (255,255,255), 4)

    # Showing the area
    #cv2.imshow('Football', screenshot_r)
    #cv2.waitKey(1)

else:

    # Width and height of the screen
    w_screen = win32api.GetSystemMetrics(0)
    h_screen = win32api.GetSystemMetrics(1)

    # As we set a limit area for cursor, we have to remove it
    win32api.ClipCursor((0,0,w_screen,h_screen))
