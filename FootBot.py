import mss
import cv2
import numpy
import ctypes
import win32api, win32con

# Set the window scale to 150%
# Game - https://vk.com/app8013553

# Check whether the key is pressed
def is_key_pressed(key):
    return ctypes.windll.user32.GetAsyncKeyState(key) & 0x8000 != 0

# Moves the cursor to x,y coordinates
def move(x,y):
    win32api.SetCursorPos((x,y))

# Function that optimizes the movement of the brick
def recount(n, half_width):
    x = round((n - half_width) * 0.73) + half_width
    return x

def main():

    # Read the image
    ball_img = cv2.imread('Ball.png')

    # Getting width and height of the image
    w = ball_img.shape[1]
    h = ball_img.shape[0]

    # Width and height of the screen
    w_screen = win32api.GetSystemMetrics(0)
    h_screen = win32api.GetSystemMetrics(1)

    # Getting width and height of the image +- resolution diff.
    h = round(ball_img.shape[0] * h_screen / 1440)
    w = round(ball_img.shape[1] * h_screen / 1440)

    # Resize the image of the ball
    ball_img = cv2.resize(ball_img, (w, h), interpolation = cv2.INTER_LANCZOS4)

    # Mss is faster than PIL and even more than pyautogui
    mss_ = mss.mss()

    # Football field (game area)
    field = {'left': 747,
             'top': 990,
             'width': 462,
             'height': 200}

    # Go to https://github.com/KroSheChKa/FootBot#how-to-run to set up it
    from_left, cursor_area = 870, 214
    width = from_left + cursor_area
    from_top = 1160

    # Limiting the cursor movement area btw soccer goalposts
    win32api.ClipCursor((from_left,
                         from_top,
                         width,
                         from_top + 1))
    
    # You may play with that coef. to make detection correct
    ball_threshold = 0.251

    # Press Q to quit the program
    while not(is_key_pressed(ord('Q'))):

        # Grabbing screenshot
        screenshot = numpy.array(mss_.grab(field))

        # Delete the unnecessary alpha channel
        screenshot_removed = screenshot[:,:,:3]

        # Getting confidence and location of the ball
        ball = cv2.matchTemplate(screenshot_removed, ball_img, cv2.TM_CCOEFF_NORMED)
        _, max_val_ball, _, max_loc_ball = cv2.minMaxLoc(ball)

        #print(f"Max Val: {max_val_ball} Max Loc: {max_loc_ball}")

        centre_ball = max_loc_ball[0] + w//2

        # Recalculating for X coord.
        new_x = recount(centre_ball, field['width'] // 2)

        # Confidence threshold
        if max_val_ball > ball_threshold:

        # Moving cursor right bellow the ball
            move(new_x + field['left'], from_top)
        
        # Putting a circle above the ball
            cv2.circle(screenshot, (max_loc_ball[0] + w//2, max_loc_ball[1]+ h//2), 20, (255,255,255), 4)

        # Showing the area
        cv2.imshow('Footbot', screenshot)
        cv2.waitKey(1)

    else:

        # As we set a limit area for cursor, we have to remove it
        win32api.ClipCursor((0,0,w_screen,h_screen))

if __name__ == "__main__":

    # Press Q to start
    while not(is_key_pressed(ord('Q'))):
        pass

    # Instantly release the button
    win32api.keybd_event(ord('Q'), 0, win32con.KEYEVENTF_KEYUP, 0)

    # Main program
    main()