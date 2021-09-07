import pyautogui
from time import sleep

sleep(5)

for _ in range(200):
	pyautogui.mouseDown()
	sleep(0.5)
	pyautogui.mouseUp()
	sleep(0.5)