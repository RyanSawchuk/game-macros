import pyautogui
from time import sleep


sleep(5)

for _ in range(1000/5):
	pyautogui.mouseDown()
	sleep(0.5)
	pyautogui.mouseUp()
	sleep(0.5)