import warnings
warnings.filterwarnings("ignore")

import os
import sys
import keyboard as kb
import pyautogui
from time import sleep


def usage():
	print(f"\nUsage: python3 lament-fly.py '<macro key bind>' '<stop macro key bind>'")
	print(f"Example: python3 lament-fly.py '~' 'esc'\n")
	sys.exit(0)


def lament_fly():
	pyautogui.keyDown('w')
	pyautogui.keyDown('shift')

	pyautogui.press('space')
	sleep(0.375)

	pyautogui.press('space')

	pyautogui.keyDown('t')
	sleep(0.15) 
	
	pyautogui.click()
	pyautogui.keyUp('t')

	pyautogui.keyUp('w')
	pyautogui.keyUp('shift')


if len(sys.argv) < 3:
	usage()

key = sys.argv[1]
stopkey = sys.argv[2]

if not key or not stopkey:
	usage()

while True:
	if kb.is_pressed(key):
		lament_fly()

	if kb.is_pressed(stopkey):
		sys.exit(0)




