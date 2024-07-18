import pydirectinput as pdi
import keyboard as kb
import sys
import threading
import win32api
from time import sleep

pdi.PAUSE = 0
stop_key = '\\'
toggle_key = ']'
toggle_full_auto_key = '['
fire_key = 'p' # second fire key in game
active = False

def run():
    global stop_key
    global toggle_key
    global toggle_full_auto_key
    global fire_key
    global active

    fire_delay = 0.01

    while True:
        try:
            if win32api.GetKeyState(0x01) < 0 and active:
                pdi.press(fire_key)
                sleep(fire_delay)
            elif kb.is_pressed(toggle_full_auto_key):
                if fire_delay == 0.01:
                    fire_delay = 0.25
                    print("SINGLE FIRE      ", end='\r')
                else:
                    fire_delay = 0.01
                    print("FULL AUTO        ", end='\r')
                sleep(0.5)
            elif kb.is_pressed(toggle_key):
                active = not active
                print(f"ACTIVE: {active}        ", end='\r')
                sleep(0.5)
            elif kb.is_pressed(stop_key):
                sys.exit(0)
            sleep(0.01)
        except Exception as e:
            print(e)
            pass

print('START - INACTIVE')

thread = threading.Thread(target=run)
thread.start()