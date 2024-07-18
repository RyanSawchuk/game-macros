import pyautogui
from time import sleep

sleep(3)

for _ in range(100):
    pyautogui.mouseDown(button='left')
    pyautogui.mouseDown(button='right')
    sleep(0.7)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseUp(button='right')
    sleep(1)