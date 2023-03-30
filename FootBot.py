import keyboard
import mss
import cv2
import numpy
from time import sleep
import win32api

#scale 150%
#https://vk.com/app8013553_119411983

#2: 1057 Y: 1006 RGB: (243, 110,  34)
#1:  879 Y: 1007 RGB: (243, 110,  34)

def move(x,y):
    win32api.SetCursorPos((x,y))

sleep(1.5)

mss_ = mss.mss()

field = {'left': 747,'top': 980,'width': 461,'height': 210}

#line = (873,1161,208,100)

ball_img = cv2.imread('Ball.png')

w = ball_img.shape[1]
h = ball_img.shape[0]

while keyboard.is_pressed('q') == False:
    
    win32api.ClipCursor((870,1160,1083,1161))
    
    scr = numpy.array(mss_.grab(field))
    
    scr_removed = scr[:,:,:3]
    
    ball = cv2.matchTemplate(scr_removed, ball_img, cv2.TM_CCOEFF_NORMED)
    
    _, max_val, _, max_loc = cv2.minMaxLoc(ball)
    
    #print(f"Max Val: {max_val} Max Loc: {max_loc}")
    
    move((max_loc[0]+747+ w//2), 1161)
    
    #cv2.circle(scr, (max_loc[0] + w//2, max_loc[1]+ h//2), 20, (0,0,255), 4)

    #cv2.imshow('Football', scr)
    
    #cv2.waitKey(1)

else:
    
    win32api.ClipCursor((0,0,3440,1440))
