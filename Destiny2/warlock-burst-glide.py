import warnings
warnings.filterwarnings("ignore")

import os, sys

import keyboard as kb
import pyautogui
import time

pyautogui.PAUSE = 0.05

def usage():
    print(f'Usage: ')
    sys.exit(0)


def swordskate():
    print("swordskate()")
    #pyautogui.press('3')
    #time.sleep(0.15)
    pyautogui.press('space')
    time.sleep(0.15)
    pyautogui.click()
    time.sleep(0.15)
    pyautogui.press('space')
    time.sleep(0.15)
    pyautogui.press('h')


def on_scroll(x, y, dx, dy):
    swordskate()


def on_click(x, y, button, pressed):
    if str(button) == 'Button.middle':
        swordskate()


key = sys.argv[1]
stopkey = sys.argv[2]

if not key or not stopkey:
	usage()

while True:
	if kb.is_pressed(key):
		swordskate()

	if kb.is_pressed(stopkey):
		sys.exit(0)

# with mouse.Listener(on_click=on_click) as listener:
#     listener.join()