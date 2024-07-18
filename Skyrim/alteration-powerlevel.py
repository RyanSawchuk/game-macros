import sys
import pyautogui
import keyboard as kb
from time import sleep

pyautogui.PAUSE = 0

sleep(5)

for _ in range(1000):
    if kb.is_pressed('='):
        sys.exit(0)
    
    pyautogui.mouseDown(button='right')
    sleep(9)
    pyautogui.mouseUp(button='right')
    sleep(1)