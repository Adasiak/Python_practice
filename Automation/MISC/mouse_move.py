from clearConsole import clearConsole
import ctypes
from time import sleep

clearConsole()

SetCursorPos = ctypes.windll.user32.SetCursorPos
mouse_event = ctypes.windll.user32.mouse_event

def left_click(x, y, clicks=1):
    SetCursorPos(x, y)
    mouse_event(2, 0, 0, 0, 0)
    mouse_event(4, 0, 0, 0, 0)

while True:
    left_click(400, 400) #left clicks at 200, 200 on your screen. Was able to send 10k clicks instantly.
    sleep(5) 
    left_click(500, 500)
    sleep(5)