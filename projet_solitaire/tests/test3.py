import keyboard
import time

time.sleep(4)

for e in range(50):
    [keyboard.press_and_release('backspace') for _ in range(5)]
    keyboard.press_and_release('down')
    """
    [keyboard.press_and_release('space') for _ in range(6)]
    keyboard.press('alt gr')
    keyboard.press_and_release('\\')
    keyboard.press_and_release('\\')
    keyboard.release('alt gr')
    keyboard.press_and_release('down')"""
    
    """for t in range(30+e*2):
        keyboard.press_and_release('space')
    
    keyboard.press('alt gr')
    keyboard.press_and_release('\\')
    keyboard.press_and_release('\\')
    keyboard.release('alt gr')"""