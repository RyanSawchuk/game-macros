import warnings
warnings.filterwarnings("ignore")

import os
import sys
import keyboard as kb
import pyautogui
from time import sleep

pyautogui.PAUSE = 0


def usage():
	print(f"\nUsage: python3 quick-draw.py <option> '<macro key bind>' '<stop macro key bind>'")
	print(f"Example: python3 quick-draw.py 1 '~' 'esc'")
	print(f'Options:')
	print(f"1. Double Slug")
	print(f"2. Xeno + Double Slug\n")
	sys.exit(0)


def double_slug():
	quick_draw('1')
	quick_draw('2')


def xeno_double_slug():
	quick_draw('1')
	quick_draw('3')
	quick_draw('2')
	quick_draw('3')


def quick_draw(weapon_key):
	pyautogui.mouseDown(button='right')

	pyautogui.keyDown('shift')
	pyautogui.keyDown('w')

	pyautogui.press(weapon_key)

	pyautogui.keyUp('w')
	pyautogui.keyUp('shift')

	sleep(0.375)
	pyautogui.click()

	pyautogui.mouseUp(button='right')


if len(sys.argv) < 4:
	usage()

option = sys.argv[1]
key = sys.argv[2]
stopkey = sys.argv[3]

if not key or not stopkey:
	usage()

func = 0

if option == '1':
	func = double_slug
elif option == '2':
	func = xeno_double_slug
else:
	usage()

while True:
	if kb.is_pressed(key):
		func()

	if kb.is_pressed(stopkey):
		sys.exit(0)
