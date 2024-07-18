import pydirectinput as pdi
import keyboard as kb
import sys
import threading
from time import sleep

active_key = 'z'
reset_key = 'x'
stop_key = '\\'
toggle_key = ']'
active = False

# Flail must be 2 handed first
# L1 B L2 Start A A D-Pad A Start L2
def chainsaw():
    pdi.PAUSE = 0.001
    pdi.keyDown('q') # Guard
    pdi.press('shift') # Backstep
    pdi.keyUp('q')
    pdi.press('f') # Skill
    pdi.press('esc') # Menu
    pdi.press('e') # Select
    pdi.press('e') # Select
    # Spear must be directly underneath the flail in the menu
    pdi.press('Down') # Down arrow key
    pdi.press('e') # Select
    pdi.press('esc') # Close menu
    pdi.keyDown('f') # Hold skill

def reset():
    pdi.PAUSE = 0.01
    pdi.press('esc') # Menu
    pdi.press('e') # Select
    pdi.press('e') # Select
    # Spear must be directly above the flail in the menu
    pdi.press('Up') # Down arrow key
    pdi.press('e') # Select
    pdi.press('esc') # Close menu
    pdi.keyDown('e')
    pdi.press('o') # Mouse 1 kb bind
    pdi.keyUp('e')

def run():
    global stop_key
    global toggle_key
    global active

    while True:
        try:
            if kb.is_pressed(active_key) and active:
                chainsaw()
                sleep(1)
            if kb.is_pressed(reset_key) and active:
                reset()
                sleep(1)
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