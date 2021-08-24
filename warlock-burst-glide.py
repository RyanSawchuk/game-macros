import warnings
warnings.filterwarnings("ignore")

import os, sys

import keyboard as kb
from pynput import mouse
from pynput.mouse import Listener
import pyautogui

pyautogui.PAUSE = 0.05

def usage():
    print(f'Usage: ')
    sys.exit(0)


def burst():
    pyautogui.press('space')
    pyautogui.press('space')
    pyautogui.press('space')
    pyautogui.press('space')
    #pyautogui.press('space')


def on_scroll(x, y, dx, dy):
    burst()


def on_click(x, y, button, pressed):
    if str(button) == 'Button.middle':
        burst()


key = sys.argv[1]
stopkey = sys.argv[2]

if not key or not stopkey:
	usage()

while False:
	if kb.is_pressed(key):
		burst()

	if kb.is_pressed(stopkey):
		sys.exit(0)

with mouse.Listener(on_click=on_click) as listener:
    listener.join()