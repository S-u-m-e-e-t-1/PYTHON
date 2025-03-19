import pyautogui
import time
time.sleep(10)
count =0
while count!=1000:
    pyautogui.typewrite("how are you")
    pyautogui.press("enter")
    count=count+1
