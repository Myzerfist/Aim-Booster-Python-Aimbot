import cv2
import pyautogui
import numpy as np
import win32api, win32con
import keyboard  # Import the keyboard library
import time

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('Left Click')

# Load the reference image
reference_img = cv2.imread("reference.png")

# Function to move the mouse to the detected object's center
def move_mouse(x, y):
    win32api.SetCursorPos((x, y))

while True:
    # Check for 'q' press to quit
    if keyboard.is_pressed('q'):  # Use keyboard library to detect key press
        break

    # Take a screenshot of the screen
    screen = pyautogui.screenshot()
    screen_img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    # Perform object detection using template matching
    result = cv2.matchTemplate(screen_img, reference_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check for a match above the threshold
    if max_val >= 0.8:  # Adjust threshold if needed
        x, y = max_loc
        w, h = reference_img.shape[:2]

        # Move mouse to the object's center
        center_x = x + w // 2
        center_y = y + h // 2
        move_mouse(center_x, center_y)
        leftClick()

